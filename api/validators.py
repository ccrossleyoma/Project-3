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

# Check to see if vehicle year is 1900-2016, the supported vehicle model years
def checkYear(value):
	print value
	if (value >= 1900) and (value <= 2016):
		return True
	return False

# Check to see if model is in list of known models, return true if so
def checkModels(value):
	brands = ['Acura', 'Alfa-Romeo', 'Aston Martin', 'Bentley', 'BMW', 'Bugatti', 'Buick', 'Cadillac', 
	'Chevrolet', 'Chrysler', 'Citroen', 'Dodge', 'Ferrari', 'Fiat', 'Ford', 'Geely', 'GMC', 'Honda',
	'Hyundai', 'Infiniti', 'Jaguar', 'Jeep', 'Kia', 'Koenigsegg', 'Lamborghini', 'Land Rover', 'Lexus',
	'Maserati', 'Mazda', 'McLaren', 'Mercedes-Benz', 'Mini', 'Mitsubishi', 'Nissan', 'Pagani', 'Peugeot',
	'Porsche', 'Renault', 'Rolls Royce', 'Saab', 'Saturn', 'Subaru', 'Suzuki', 'Tata', 'Tesla', 'Toyota', 
	'Volkswagen','Volvo']

	if value in brands:
		return True
	return False

# Check to see if miles/distance traveled is above 0
def checkDistance(value):
	if (value > 0):
		return True
	return False

# Check to see if volume is above 0
def checkVolume(value):
	if (value > 0):
		return True
	return False

# Check to see if price is above 0
def checkPrice(value):
	if (value > 0):
		return True
	return False

