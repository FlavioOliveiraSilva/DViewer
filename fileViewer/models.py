# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class NormativeRef(models.Model):
    normCode = models.CharField(max_length=20)
    normDescription = models.CharField(max_length=40)

    def __unicode__(self):
        return unicode(self.normCode)


class Language(models.Model):
    nameLanguage = models.CharField(max_length=20)
    codeLanguage = models.CharField(max_length=2)

    def __unicode__(self):
        return unicode(self.nameLanguage)


class CountryDistributed(models.Model):
    nameCountry = models.CharField(max_length=40)
    languageCountry = models.ForeignKey(Language)

    def __unicode__(self):
        return unicode(self.nameCountry)


class Brand(models.Model):
    brandCode = models.CharField(max_length=2)
    brandName = models.CharField(max_length=40)

    def __unicode__(self):
        return unicode(self.brandName)


class DocumentType(models.Model):
    docType = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.docType)



class Document(models.Model):
    documentName = models.CharField(max_length=40)
    documentFile = models.FileField(upload_to='documents/')
    idNumber = models.IntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    brand = models.ForeignKey(Brand)
    docType = models.ForeignKey(DocumentType)
    normRef = models.ForeignKey(NormativeRef)
    country = models.ForeignKey(CountryDistributed)
    language = models.ForeignKey(Language)

    def __unicode__(self):
        return unicode(self.documentName)

