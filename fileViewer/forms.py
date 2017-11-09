from django import forms
#from uploads.core.models import Document
from .models import Document, CountryDistributed


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
            'documentFile'
        )

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['country'].label = "Country - lang"


class SearchForm(forms.Form):
    search_term_docName = forms.CharField(label="Document name")
    search_term_idNumber = forms.CharField(label="idNumber")
    search_term_brand = forms.CharField(label="brand")
    search_term_normRef = forms.CharField(label="normRef")
    search_term_language = forms.CharField(label="language")

