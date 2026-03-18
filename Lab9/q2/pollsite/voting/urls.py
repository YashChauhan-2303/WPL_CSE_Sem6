from django.urls import path

from .views import result_view, vote_view

urlpatterns = [
    path("", vote_view, name="vote"),
    path("result/", result_view, name="result"),
]
