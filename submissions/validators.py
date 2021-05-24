from django.core.exceptions import ValidationError


def validate_submission(value):
    content = value
    if len(content) > 60:
        raise ValidationError("Title can't be more than 60 characters.")
    return value


def validate_description(value):
    content = value
    if len(content) > 500:
        raise ValidationError("Description can't be more than 500 characters.\n Current length is {} characters.".format(len(content)))
    return value
