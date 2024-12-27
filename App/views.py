from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import CreateView,UpdateView,DetailView,ListView,DeleteView
from .models import Book


class BookListview(ListView):
    model = Book
    template_name = 'book_list.html'

class BookDetailview(DetailView):
    model = Book
    template_name = 'book_detail.html'




class BookCreateview(CreateView):
    model = Book
    fields = ['title','author','published_date']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')


class BookUpdateview(UpdateView):
    model = Book
    fields = ['title','author','published_date']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')

class BookDeleteview(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')