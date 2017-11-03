# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .forms import DocumentForm, SearchForm
from .models import Document,  Brand, NormativeRef


def home(request):
    return render(request, 'fileViewer/home.html')


def document_overview(request):
    documents_in_database = Document.objects.all()
    return render(request, 'fileViewer/documentOverview.html', {'documents_in_database': documents_in_database})


def show_document(request):
    return render(request, 'fileViewer/documentDetail.html')


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
            search_term = form.cleaned_data['search_term_docName']
            search_result = Document.objects.filter(documentName__icontains=search_term)
            #resultquery = Document.objects.filter(brand__brandName__icontains='ECorp')
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
