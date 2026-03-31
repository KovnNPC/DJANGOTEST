### BASE HARDCODING URLS FOR POLLS APP, REWRITE LATER TO USE GENERIC VIEWS
"""
from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    # /polls/
    path("", views.index, name="index"),
    # /polls/#/
    path("<int:question_id>/", views.detail, name="detail"),
    # /polls/#/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # /polls/#/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # /polls/ 
    # /polls/ 
    # /polls/ 
]

"""

### REWRITTEN TO USE GENERIC VIEWS

from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
