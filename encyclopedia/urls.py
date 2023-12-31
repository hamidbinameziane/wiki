from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry_page, name="entry_page"),
    path("wiki/create_page/", views.create_page, name="create_page"),
    path("", views.random_page, name="random_page"),
    path("wiki/edit_page/<str:title>", views.edit_page, name="edit_page"),
]
