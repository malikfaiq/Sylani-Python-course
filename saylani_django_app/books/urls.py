from django.urls import path
from .views import BookView

urlpatterns = [
    path("", BookView.as_view(), name="book-list"),
    path("delete/<int:book_id>/", BookView.as_view(), name="book-delete"),
]
