# forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Document

class PDFDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'pdf_file']

    def clean_pdf_file(self):
        pdf_file = self.cleaned_data.get('pdf_file')        
        max_size = 30 * 1024 
        if pdf_file and pdf_file.size > max_size:
            raise ValidationError('File size must be 30 kb or less.')
        return "success"
