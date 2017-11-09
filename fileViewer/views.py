# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .forms import DocumentForm, SearchForm
from .models import Document,  Brand, NormativeRef


def home(request):
    return render(request, 'fileViewer/home.html')


def about(request):
    return render(request, 'fileViewer/about.html')


def document_overview(request):
    documents_in_database = Document.objects.all()
    return render(request, 'fileViewer/documentOverview.html', {'documents_in_database': documents_in_database})

# DASHBOARD Expected long time to query all documents once the list is more comprehensive and resources are limited


def dashboard(request):
    query_nl_documents = Document.objects.filter(country__languageCountry__icontains='nl')
    query_fr_documents = Document.objects.filter(country__languageCountry__icontains='fr')
    total = query_nl_documents.count() + query_fr_documents.count()
    return render(request, 'fileViewer/dashboard.html', {
        'query_nl_documents': query_nl_documents,
        'query_fr_documents': query_fr_documents,
        'total': total
    })


def show_document(request):
    return render(request, 'fileViewer/documentDetail.html')

#Test function combining different models in one form

#def model_form_search(request):
#    upload_form = {
#        'uploadFormPart1': DocumentForm(request.POST),
#        'uploadFormPart2': LangForm(request.POST)
#        }
#    return render(request, 'fileViewer/fileUpload.html', upload_form)


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'fileViewer/fileUpload.html', {
        'form': form
    })


def search_document(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            ##search_term = form.cleaned_data['search_term_docName']
            #search_term = form.cleaned_data['search_term_idNumber']
            #search_term = form.cleaned_data['search_term_brand']
            #search_term = form.cleaned_data['search_term_normRef']
            search_term = form.cleaned_data['search_term_language']
            ##search_result = Document.objects.filter(documentName__icontains=search_term)
            #search_result = Document.objects.filter(idNumber__icontains=search_term)
            #search_result = Document.objects.filter(brand__brandName__icontains=search_term)
            #search_result = Document.objects.filter(NormativeRef__normCode__icontains=search_term)
            search_result = Document.objects.filter(country__languageCountry__icontains=search_term)
            return render(request, 'fileViewer/documentSearch.html', {
                'form': form, 'search_result': search_result
            })
    else:
        form = SearchForm()

    return render(request, 'fileViewer/documentSearch.html', {
        'form': form,
    })


class BrandList(ListView):
    model = Brand
    context_object_name = 'brand_list'


class NormativeRefList(ListView):
    model = NormativeRef
    context_object_name = 'NormativeRef_list'
