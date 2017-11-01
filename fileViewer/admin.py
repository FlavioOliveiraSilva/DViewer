# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Document, NormativeRef, CountryDistributed, Language, DocumentType, Brand


class DocumentAdmin (admin.ModelAdmin):
    list_display = ('documentName', 'idNumber', 'brand', 'docType', 'normRef', 'country', 'language', 'documentFile')


admin.site.register(Document, DocumentAdmin)
admin.site.register(NormativeRef)
admin.site.register(CountryDistributed)
admin.site.register(Language)
admin.site.register(DocumentType)
admin.site.register(Brand)



#
#    def get_list_display(self, request):
#        self.user = request.user
#        return super(DocumentAdmin, self).get_list_display(request)