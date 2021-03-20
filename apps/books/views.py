from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages

from .models import Book
from .forms import BookForm


class BookListView(ListView):
    model = Book
    template_name = 'books/list.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['books'] = self.get_queryset()
        context['title'] = 'Lista de libros'
        return context


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books:list')
    template_name = 'books/includes/modal_create.html'

    def get_context_data(self, **kwargs):
        context = super(BookCreateView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['title'] = 'Registrar libro'
        return context


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books:list')
    template_name = 'books/includes/modal_edit.html'

    def get_context_data(self, **kwargs):
        context = super(BookUpdateView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['title'] = 'Registrar libro'
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/detail.html'


def delete_book(request, pk):
    obj = get_object_or_404(Book, pk=pk)
    obj.delete()
    messages.success(request, 'Libro eliminado correctamente')
    return redirect(to='books:list')
