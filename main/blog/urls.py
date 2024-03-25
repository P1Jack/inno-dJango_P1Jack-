from django.urls import path

from . import views

urlpatterns = [
    path("home", views.home_page, name="home_page"),
    path("aboutme", views.aboutme_page, name="aboutme_page")
]
