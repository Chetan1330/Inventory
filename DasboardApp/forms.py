from django import forms
from .models import Stock

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()
