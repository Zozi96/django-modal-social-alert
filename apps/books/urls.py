from django.urls import path

from .views import BookListView, BookCreateView, BookUpdateView

app_name = 'books'

urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('create/', BookCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='update'),
]
