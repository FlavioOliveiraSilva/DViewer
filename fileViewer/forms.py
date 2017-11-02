from django import forms
#from uploads.core.models import Document
from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = (
            'documentName',
            'idNumber',
            'brand',
            'docType',
            'normRef',
            'country',
            'language',
            'documentFile'
                  )




