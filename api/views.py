from rest_framework.views import APIView
from rest_framework.response import Response    
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from .models import Author, Book, Publisher, Magazine
from .serializers import AuthorSerializer, BookSerializer, PublisherSerializer, MagazineSerializer


class AuthorListAPIView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListAPIView(ListCreateAPIView):
    
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        author_id = self.request.query_params.get('author_id', None)


        if author_id:
            queryset = queryset.filter(author_id = author_id)
        return queryset

class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def get(self,request):
    #     books = Book.objects.all()
    #     serializer = BookSerializer(books, many=True)
    #     return Response(serializer.data)


class PublisherListAPIView(ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class PublisherDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


    # def get(self,request):
    #     publishers = Publisher.objects.all()
    #     serializer = PublisherSerializer(publishers, many=True)
    #     return Response(serializer.data)



class MagazineListAPIView(ListCreateAPIView):

    serializer_class = MagazineSerializer

    def get_queryset(self):
        queryset = Magazine.objects.all()
        publisher_id = self.request.query_params.get('publisher_id', None)


        if publisher_id:
            queryset = queryset.filter(publisher_id = publisher_id)
        return queryset



class MagazineDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer


    # def get(self,request):
    #     magazines = Magazine.objects.all()
    #     serializer = MagazineSerializer(magazines, many=True)
    #     return Response(serializer.data)