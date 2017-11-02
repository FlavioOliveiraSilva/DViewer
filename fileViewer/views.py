# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .forms import DocumentForm
from .models import Document,  Brand


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
    search_result = Document.objects.filter(brand__contains='ECorp')
    return render(request, 'fileViewer/documentSearch.html', {'search_result': search_result})


class BrandList(ListView):
    model = Brand

