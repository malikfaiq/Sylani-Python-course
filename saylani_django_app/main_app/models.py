from django.db import models


# Create your models here.
class Rocket(models.Model):
    name = models.CharField(max_length=100)
    speed = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    place_of_birth = models.CharField(max_length=100, null=True, blank=True)
    no_of_books = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # author_name = models.CharField(max_length=100)
    # category_name = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    available_copies = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
