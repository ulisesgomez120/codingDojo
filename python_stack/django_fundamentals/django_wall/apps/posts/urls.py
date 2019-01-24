from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dash),
    url(r'^create/message/$', views.create_message),
    url(r'^create/comment/$', views.create_comment),
]