from django.core.exceptions import ValidationError


def validate_phone_number(value):
    content = value
    if not len(content) == 10:
        raise ValidationError("Phone number MUST be 10 digits long.")
    return value
