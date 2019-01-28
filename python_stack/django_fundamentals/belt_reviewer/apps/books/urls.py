from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^new/$', views.new, name="new"),
    url(r'^create_book/$', views.create_book, name="create_book"),
    url(r'^add_review/(?P<book_id>\d+)/$', views.add_review, name="add_review"),
    url(r'^(?P<book_id>\d+)/$', views.show, name="show"),
    
]