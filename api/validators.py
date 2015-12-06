from django.core.exceptions import ValidationError

# Before saving to database, check to make sure there is no Javascript. Throw ValidationError if Javascript is detected.
def removeJavascriptKeyword(value):
    if "javascript:" in value:
        raise ValidationError(('String contains javascript'), code='invalid')
    if "document.write" in value:
        raise ValidationError(('String contains javascript'), code='invalid')
    if "alert(" in value:
        raise ValidationError(('String contains javascript'), code='invalid')
    if "</SCRIPT>" in value:
        raise ValidationError(('String contains javascript'), code='invalid')
    if "<SCRIPT>" in value:
        raise ValidationError(('String contains javascript'), code='invalid')
    if "exec(" in value:
        raise ValidationError(('String contains javascript'), code='invalid')
    if "<IMG SRC=" in value:
        raise ValidationError(('String contains javascript'), code='invalid')
    if "<iframe src=" in value:
        raise ValidationError(('String contains javascript'), code='invalid')
    if "<SCRIPT SRC=" in value:
        raise ValidationError(('String contains javascript'), code='invalid')
    if "<SCRIPT/SRC=" in value:
        raise ValidationError(('String contains javascript'), code='invalid')
    if "<BODY onload" in value:
        raise ValidationError(('String contains javascript'), code='invalid')
    if "<BODY ONLOAD=" in value:
        raise ValidationError(('String contains javascript'), code='invalid')
    if "<<SCRIPT>" in value:
        raise ValidationError(('String contains javascript'), code='invalid')
    if "<<SCRIPT>" in value:
        raise ValidationError(('String contains javascript'), code='invalid')
    if "<STYLE>" in value:
        raise ValidationError(('String contains javascript'), code='invalid')
    if "<A HREF=" in value:
        raise ValidationError(('String contains javascript'), code='invalid')
        
        

# def (value):
# 	if "script" in value
# 		return
# 	else
# 		retu

def checkModels(value):
	brands = ['Acura', 'BMW', 'Volvo']
	if any(x in value for x in brands):
		return True
	return False