from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.change_home_view, name="home"),
    path("second-page/", views.second_page_view, name="second_page"),
    path("authors/", views.author_list, name="author_list"),
    path("authors/<int:pk>/", views.author_detail, name="author_detail"),
    path("authors/new/", views.author_create, name="author_create"),
    # path("books/", views.book_list, name="book_list"),
    # path("books/<int:pk>/", views.book_detail, name="book_detail"),
    # path("books/new/", views.book_create, name="book_create"),
    # path("books/<int:pk>/update/", views.book_update, name="book_update"),
    # path("books/<int:pk>/delete/", views.book_delete, name="book_delete"),
]
