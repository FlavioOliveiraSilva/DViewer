# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
#from .models import Document, NormativeRef, CountryDistributed, Language, DocumentType, Brand
from .models import Document, NormativeRef, CountryDistributed, DocumentType, Brand


class DocumentAdmin (admin.ModelAdmin):
    #list_display = ('documentName', 'idNumber', 'brand', 'docType', 'normRef', 'country', 'language', 'documentFile')
    list_display = ('documentName', 'idNumber', 'brand', 'docType', 'normRef', 'country', 'documentFile', 'uploaded_at')


class CountryAdmin(admin.ModelAdmin):
    list_display = ('nameCountry', 'languageCountry')

admin.site.register(Document, DocumentAdmin)
admin.site.register(NormativeRef)
admin.site.register(CountryDistributed, CountryAdmin)
admin.site.register(DocumentType)
admin.site.register(Brand)

