from django.urls import path

from .views import BookListView, BookCreateView

app_name = 'books'

urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('create/', BookCreateView.as_view(), name='create'),
]
