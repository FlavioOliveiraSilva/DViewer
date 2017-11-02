
from django.conf.urls import url
from fileViewer.views import BrandList
from . import views


urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^fileUpload/$', views.model_form_upload, name='fileUpload'),
    url(r'^documentOverview/$', views.document_overview, name='document_overview'),
    url(r'^documentSearch/$', views.search_document, name='search_document'),
    url(r'^BrandList/$', BrandList.as_view(), name='brand_list'),
    url(r'^$', views.home, name='home'),
        ]

