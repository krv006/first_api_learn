from django.urls import path
from .views import AuthorDetailAPIView, AuthorListAPIView, BookListAPIView, PublisherListAPIView, MagazineListAPIView

urlpatterns = [

    path('authors/', AuthorListAPIView.as_view(),name='authors-list'),
    path('authors/<int:pk>/', AuthorDetailAPIView.as_view(),name='authors-detail'),

    path('books/', BookListAPIView.as_view(),name='books-list'),
    path('books/<int:pk>/', BookListAPIView.as_view(),name='books-detail'),

    path('publishers/', PublisherListAPIView.as_view(),name='publishers-list'),
    path('publishers/<int:pk>/', PublisherListAPIView.as_view(),name='publishers-detail'),

    path('magazines/', MagazineListAPIView.as_view(),name='magazines-list'),
    path('magazines/<int:pk>/', MagazineListAPIView.as_view(),name='magazines-detail'),

]