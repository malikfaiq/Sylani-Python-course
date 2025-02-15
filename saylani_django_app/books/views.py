from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.urls import reverse


class BookView(View):
    template_name = "books/book_list.html"

    def get(self, request):
        books = Book.objects.all()
        print(books)
        return render(
            request, self.template_name, {"books": books, "form": self.get_form()}
        )

    def post(self, request):
        if "delete" in request.POST:
            book_id = request.POST.get("delete")
            book = get_object_or_404(Book, id=book_id)
            book.delete()
            return redirect(reverse("book-list"))

        form = self.get_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("book-list"))

        books = Book.objects.all()
        return render(request, self.template_name, {"books": books, "form": form})

    def get_form(self, data=None):
        from django.forms import ModelForm

        class BookForm(ModelForm):
            class Meta:
                model = Book
                fields = ["title", "author", "description", "published_date"]

        return BookForm(data)
