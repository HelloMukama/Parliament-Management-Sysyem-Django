import random
import string

from django.utils.text import slugify
'''
random_string_generator is located here"
http://joincfe.com/blog/random-string-generator-in-python/
'''

PROHIBITED_SLUGS = ['create', 'Create', ]  # this will help us to avoid
# url conflicting  with the create submission url in our complaints app..


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    '''
    This is for a django project and it assumes your instance,
    has a model with a slug field and a title character (char) field
    '''
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.user)

    if slug in PROHIBITED_SLUGS:  # don't allow the user to create a slug with exact slug
        # instead just add a 4 digit randstr to the end of this slug
        new_slug = "{slug}-{randstr}".format(
            slug=slug, randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug, randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
