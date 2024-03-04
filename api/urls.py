from django.urls import path
from .views import *

urlpatterns = [

    path('authors/', AuthorListAPIView.as_view(),name='authors-list'),
    path('authors/<int:pk>/', AuthorDetailAPIView.as_view(),name='authors-detail'),

    path('books/', BookListAPIView.as_view(),name='books-list'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(),name='books-detail'),

    path('publishers/', PublisherListAPIView.as_view(),name='publishers-list'),
    path('publishers/<int:pk>/', PublisherDetailAPIView.as_view(),name='publishers-detail'),

    path('magazines/', MagazineListAPIView.as_view(),name='magazines-list'),
    path('magazines/<int:pk>/', MagazineDetailAPIView.as_view(),name='magazines-detail'),

]