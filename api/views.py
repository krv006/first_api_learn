from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from .models import Author, Book, Publisher, Magazine
from .serializers import AuthorSerializer, BookSerializer, PublisherSerializer, MagazineSerializer
# BookSerializer


#test branch

class AuthorListAPIView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListAPIView(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class PublisherListAPIView(APIView):
    def get(self,request):
        publishers = Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)
        return Response(serializer.data)


class MagazineListAPIView(APIView):
    def get(self,request):
        magazines = Magazine.objects.all()
        serializer = MagazineSerializer(magazines, many=True)
        return Response(serializer.data)

