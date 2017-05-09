from django import forms
from .models import CustomSku

class CustomSkuForm(forms.ModelForm):
	customSku = forms.CharField(max_length=13, min_length=13, label="Scan or type in barcode", widget=forms.TextInput(attrs={
		'class' : 'form-control'
		}))

	class Meta:
		model = CustomSku
		exclude = []