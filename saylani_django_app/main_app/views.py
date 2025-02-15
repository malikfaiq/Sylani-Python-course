import json
from django.shortcuts import get_object_or_404, get_list_or_404, render

# Create your views here.
from django.http import HttpResponse, JsonResponse

from main_app.models import Author, Book, Category


def change_home_view(request):
    return HttpResponse("Rocket is in space now!")


def second_page_view(request):
    return HttpResponse("Rocket is crashed!")


def author_list(request):
    authors = Author.objects.values()
    return JsonResponse(list(authors), safe=False)


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return JsonResponse(
        {
            "id": author.id,
            "name": author.name,
            "bio": author.bio,
            "created_at": author.created_at,
        }
    )


def author_create(request):
    if request.method == "POST":
        print(request.body)
        data = json.loads(request.body)
        print(data)
        name = data.get("name")
        bio = data.get("bio")
        no_of_books = data.get("no_of_books")
        print(name, bio)
        author = Author.objects.create(name=name, bio=bio, no_of_books=no_of_books)

        return JsonResponse(
            {
                "id": author.id,
                "name": author.name,
                "bio": author.bio,
                "created_at": author.created_at,
            }
        )
    return HttpResponse(status=405)


def book_list(request):
    books = Book.objects.values()
    print(list(books))
    return JsonResponse(list(books), safe=False)


def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        # book_list = Book.objects.filter(no_of_copies__lt=[pk, pk2, pk3])
        print(book_list)
        return JsonResponse(
            {
                "id": book.id,
                "title": book.title,
                "author": book.author.name,
                "published_date": book.published_date,
                "isbn": book.isbn,
                "available_copies": book.available_copies,
                "created_at": book.created_at,
            }
        )
    except:
        error_message = f"Book not found with id {pk}"
        return JsonResponse({"error": error_message}, status=404)


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return JsonResponse({"message": "Book deleted successfully"})


def book_update(request, pk):
    if request.method == "PUT":
        print(pk, "0101--1")
        book = get_object_or_404(Book, pk=pk)
        data = json.loads(request.body)
        title = data.get("title")
        published_date = data.get("published_date")
        isbn = data.get("isbn")
        available_copies = data.get("available_copies")
        # update if the value is not None
        if title:
            book.title = title
        if published_date:
            book.published_date = published_date
        if isbn:
            book.isbn = isbn
        if available_copies:
            book.available_copies = available_copies
        book.save()

        # for field in ["title", "published_date", "isbn", "available_copies"]:
        #     if field in data:
        #         setattr(book, field, data[field])

        return JsonResponse(
            {
                "id": book.id,
                "title": book.title,
                "author": book.author.name,
                "published_date": book.published_date,
                "isbn": book.isbn,
                "available_copies": book.available_copies,
                "created_at": book.created_at,
            }
        )
    return HttpResponse(status=405)


def book_create(request):
    if request.method == "POST":
        print(request.body)
        data = json.loads(request.body)
        title = data.get("title")
        author_id = data.get("author")
        category_id = data.get("category")
        published_date = data.get("published_date")
        isbn = data.get("isbn")
        available_copies = data.get("available_copies")
        author = get_object_or_404(Author, pk=author_id)
        category = get_object_or_404(Category, pk=category_id)
        book = Book.objects.create(
            category=category,
            title=title,
            author=author,
            published_date=published_date,
            isbn=isbn,
            available_copies=available_copies,
        )
        return JsonResponse(
            {
                "id": book.id,
                "title": book.title,
                "author": book.author.name,
                "published_date": book.published_date,
                "isbn": book.isbn,
                "available_copies": book.available_copies,
                "created_at": book.created_at,
            }
        )
    return HttpResponse(status=405)
