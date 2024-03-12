from rest_framework import serializers
from .models import Author, Book, Publisher, Magazine

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['id','title','publication_date','genre','pages','language','author']

class PublisherSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Publisher
        fields = '__all__'


class MagazineSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()

    class Meta:
        model = Magazine
        fields = ['id', 'title', 'publication_date', 'category', 'price', 'editor', 'publisher' ]