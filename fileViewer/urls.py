
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^fileUpload/$', views.model_form_upload, name='fileUpload'),
    url(r'^documentOverview/$', views.document_overview, name='document_overview'),
    #url(r'^media/(?P<document_document>\d+)/$', views.show_document, name='show_document'),
    url(r'^$', views.home, name='home'),
        ]

