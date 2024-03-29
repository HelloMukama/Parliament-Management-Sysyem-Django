# https://github.com/xhtml2pdf/django-xhtml2pdf/blob/master/django_xhtml2pdf/utils.py

import django
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.response import TemplateResponse
from xhtml2pdf import pisa # TODO: Change this when the lib changes.
from django.conf import settings

try:
    from StringIO import BytesIO
except:
    from io import BytesIO

import os
import posixpath
from django.contrib.staticfiles import finders

# import os
# from django.conf import settings
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa
# from django.contrib.staticfiles import finders


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
            if not isinstance(result, (list, tuple)):
                    result = [result]
            result = list(os.path.realpath(path) for path in result)
            path=result[0]
    else:
            sUrl = settings.STATIC_URL        # Typically /static/
            sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
            mUrl = settings.MEDIA_URL         # Typically /media/
            mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

            if uri.startswith(mUrl):
                    path = os.path.join(mRoot, uri.replace(mUrl, ""))
            elif uri.startswith(sUrl):
                    path = os.path.join(sRoot, uri.replace(sUrl, ""))
            else:
                    return uri

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                    'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path


#===============================================================================
# HELPERS
#===============================================================================
class UnsupportedMediaPathException(Exception):
    pass


def fetch_resources(uri, rel):
    """
    Callback to allow xhtml2pdf/reportlab to retrieve Images,Stylesheets, etc.
    `uri` is the href attribute from the html link element.
    `rel` gives a relative path, but it's not used here.
    """

    if uri.startswith("http://") or uri.startswith("https://"):
        return uri

    if settings.DEBUG:
        newpath = uri.replace(settings.STATIC_URL, "").replace(settings.MEDIA_URL, "")
        normalized_path = posixpath.normpath(newpath).lstrip('/')
        absolute_path = finders.find(normalized_path)  
        if absolute_path:    
            return absolute_path
        
    if settings.MEDIA_URL and uri.startswith(settings.MEDIA_URL):
        path = os.path.join(settings.MEDIA_ROOT,
                            uri.replace(settings.MEDIA_URL, ""))
    elif settings.STATIC_URL and uri.startswith(settings.STATIC_URL):
        path = os.path.join(settings.STATIC_ROOT,
                            uri.replace(settings.STATIC_URL, ""))
        if not os.path.exists(path):
            for d in settings.STATICFILES_DIRS:
                path = os.path.join(d, uri.replace(settings.STATIC_URL, ""))
                if os.path.exists(path):
                    break
    else:
        raise UnsupportedMediaPathException('media urls must start with %s or %s' % (settings.MEDIA_URL, settings.STATIC_URL))
    return path


def generate_pdf_template_object(template_object, file_object, context, link_callback=fetch_resources):
    """
    Inner function to pass template objects directly instead of passing a filename
    """
    html = template_object.render(context)       
    pisa.CreatePDF(html.encode("UTF-8"), file_object , encoding='UTF-8', link_callback=link_callback)
    return file_object


#===============================================================================
# Main
#===============================================================================
def generate_pdf(template_name, file_object=None, context=None, link_callback=fetch_resources): # pragma: no cover

    """
    SINCE 'from django_xhtml2pdf.utils import generate_pdf' DOES NOT WORK ANYMORE IN PYTHON3*
    WE ARE MANUALLY DEFINING THE FUNCTION BELOW OURSELVES TO LATER USE IN THE CBV THAT FOLLOWS

    Uses the xhtml2pdf library to render a PDF to the passed file_object, from the
    given template name.
    This returns the passed-in file object, filled with the actual PDF data.
    In case the passed in file object is none, it will return a BytesIO instance.
    """

    if not file_object:
        file_object = BytesIO()
    if not context:
        context = {}
    tmpl = get_template(template_name)
    generate_pdf_template_object(tmpl, file_object, context, link_callback=link_callback)
    return file_object


def render_to_pdf_response(template_name, context=None, pdfname=None, link_callback=fetch_resources):
    file_object = HttpResponse(content_type='application/pdf')
    
    if not pdfname:
        pdfname = '%s.pdf' % os.path.splitext(os.path.basename(template_name))[0]
    file_object['Content-Disposition'] = 'attachment; filename=%s' % pdfname
    return generate_pdf(template_name, file_object, context, link_callback=link_callback)


def pdf_decorator(function=None, pdfname="file.pdf"):
    def _dec(view_func):
        def _view(*args, **kwargs):
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s'%(pdfname)
            result_func = view_func(*args, **kwargs).getvalue()
            pisa.CreatePDF(
                result_func,
                dest=response,
                link_callback=fetch_resources)
            return response

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec       
    return _dec(function)


class PdfResponse(TemplateResponse):
    def render(self):
        retval = super(PdfResponse, self).render()
        result = BytesIO()
        pisa.CreatePDF(
            self.rendered_content,
            dest=result,
            link_callback=fetch_resources)
        self.content = result.getvalue()
        return retval
