from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )

def validate_email(value):
	email = value
	if ".edu" in email:
		raise forms.ValidationError("We do not accept edu email")

CATEGORIES = ['Mexican', 'Asian', 'Chinese', 'Others']

def validate_category(value):
	if not value.capitalize() in CATEGORIES:
		raise ValidationError(f"{value} not a valid category")
