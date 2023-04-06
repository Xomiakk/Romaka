from django.urls import re_path
from core import views



urlpatterns = [
	re_path(r'^$', views.table, name='home'),
    re_path(r'^integrity/$', views.integrity, name='integrity'),
    re_path(r'^accessibility/$', views.accessibility, name='accessibility'),
    re_path(r'^privacy/$', views.privacy, name='privacy'),
]

