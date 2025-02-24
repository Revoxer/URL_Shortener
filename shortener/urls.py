from django.urls import path

from .views import IndexView, redirect_url

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<str:short_code>", redirect_url, name="redirect_url"),
]
