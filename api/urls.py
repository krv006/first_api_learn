from django.urls import path
from .views import AuthorListAPIView, BookListAPIView, PublisherListAPIView, MagazineListAPIView

urlpatterns = [
    path('authors/', AuthorListAPIView.as_view(),name='authors-list'),
    path('books/', BookListAPIView.as_view(),name='books-list'),
    path('publishers/', PublisherListAPIView.as_view(),name='authors-list'),
    path('magazines/', MagazineListAPIView.as_view(),name='authors-list')
]