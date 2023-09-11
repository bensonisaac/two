from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("api", views.persons, name="create-list"),
   re_path(r'^api/(?P<param>[0-9]+|[a-zA-Z]+)$', views.person_detail, name="read-update-delete"),
]

urlpatterns = format_suffix_patterns(urlpatterns)