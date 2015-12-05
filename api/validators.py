from django.core.exceptions import ValidationError

def removeJavascriptKeyword(value):
    if "javascript:" in value:
        raise ValidationError(('String contains javascript'), code='invalid')
    if "javascript" in value:
        raise ValidationError(('String contains javascript'), code='invalid')