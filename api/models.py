from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    country = models.CharField(max_length=100)
    biography = models.TextField()
    website = models.URLField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    genre = models.CharField(max_length=100)
    pages = models.PositiveIntegerField()
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Publisher(models.Model):
    name = models.CharField(max_length=150)
    established_date = models.DateField()
    country = models.CharField(max_length=100)
    website = models.URLField()
    headquarters_location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Magazine(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    editor = models.CharField(max_length=150)

    def __str__(self):
        return self.title