
from django.conf.urls import url
from fileViewer.views import BrandList, NormativeRefList
from . import views


urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^fileUpload/$', views.model_form_upload, name='fileUpload'),
    url(r'^documentOverview/$', views.document_overview, name='document_overview'),
    url(r'^documentSearch/$', views.search_document, name='search_document'),
    url(r'^BrandList/$', BrandList.as_view(), name='brand_list'),
    url(r'^NormativeRef/$', NormativeRefList.as_view(), name='NormativeRef_list'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^$', views.home, name='home'),
        ]

