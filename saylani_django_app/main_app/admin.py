from django.contrib import admin

from main_app.models import Author, Book, Category


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "no_of_books", "place_of_birth")
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "published_date",
        "available_copies",
        "created_at",
    )
    search_fields = ("title", "author__name")
    list_filter = ("published_date",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
