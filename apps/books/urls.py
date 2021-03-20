from django.urls import path

from .views import BookListView, BookCreateView, BookUpdateView, delete_book, BookDetailView

app_name = 'books'

urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('create/', BookCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', delete_book, name='delete'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='detail'),
]
