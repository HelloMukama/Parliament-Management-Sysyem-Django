from django.http import HttpResponseRedirect, HttpResponse

from .utils import generate_pdf


class PdfResponseMixin(object, ):
    pdf_name = "outputXXX"

    def get_pdf_name(self):
        return self.pdf_name

    def render_to_response(self, context, **response_kwargs):
        context=self.get_context_data()
        template=self.get_template_names()[0]
        resp = HttpResponse(content_type='application/pdf')
        resp['Content-Disposition'] = 'attachment; filename="{0}.pdf"'.format(self.get_pdf_name())
        result = generate_pdf(template, file_object=resp, context=context)
        return result
