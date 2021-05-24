import random
import string

from django.conf import settings

SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 45)

# from shortener.models import KirrURL


def random_code_generator(size=SHORTCODE_MIN,
                          chars=string.ascii_lowercase+string.hexdigits+string.ascii_uppercase+string.digits):
    '''this is the function we are going to use for generating the random code
    for email activation.. from above, we want the code to contain lower, uppercase
    and digits note that we MUST make sure that the code is as unique as it can get.
    therefore, using lowercase, uppercase, digits and more string formats can do us good

    # e.g 8H01oZ2BjzaaE7u8TEanZDLeR2EBK3sGfr9PZ40E95RO4 is what has been generated for us to
    use in our first profile example...
    '''

    # new_code = ''
    # for _ in range(size):
    #     new_code += random.choice(chars)
    # return new_code

    # # the line below does what the above 4 lines of code do
    return ''.join(random.choice(chars) for _ in range(size))

# example codes....
# 8H01oZ2BjzaaE7u8TEanZDLeR2EBK3sGfr9PZ40E95RO4
# ky6X7ET8Di1fqde2wjWz5bDoF9o04la6n1ETvEIe7m3fr
# ApBcqABxv1oxsuhMeZF6FPAO0c5o4s78JsaEUVkYAdEeX
