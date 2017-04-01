from django import forms
from .models import URL

class urlForm(forms.ModelForm):
	class Meta:
		model = URL
		fields = [

			"url"

		]