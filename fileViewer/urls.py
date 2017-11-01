from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^fileUpload/', views.model_form_upload, name='fileUpload'),
    url(r'^$', views.home, name='home'),
        ]