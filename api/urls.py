from django.urls import path
from .views import AuthorDetailAPIView, AuthorListAPIView, BookListAPIView, PublisherListAPIView, MagazineListAPIView

urlpatterns = [

    path('authors/', AuthorListAPIView.as_view(),name='authors-list'),
    path('authors/<int:pk>/', AuthorDetailAPIView.as_view(),name='authors-detail'),

    path('books/', BookListAPIView.as_view(),name='books-list'),

    path('publishers/', PublisherListAPIView.as_view(),name='authors-list'),

    path('magazines/', MagazineListAPIView.as_view(),name='authors-list')

]