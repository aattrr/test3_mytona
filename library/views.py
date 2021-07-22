from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from library.models import Book, Author
from django.db.models import Q


class BooksList(ListView):
    """ Вывод списка книг """
    model = Book
    paginate_by = 4


class BookDetail(DetailView):
    """ Вывод страницы детального описания книги """
    model = Book


class BookCreate(CreateView):
    """ Создание книги """
    model = Book
    fields = '__all__'
    template_name = "library/book_create.html"


class BookUpdate(UpdateView):
    """ Редактирование книги """
    model = Book
    fields = ['title', 'description', 'author']


class BookDelete(DeleteView):
    """ Удаление книги """
    model = Book
    success_url = reverse_lazy('book_list')


class AuthorList(ListView):
    """ Вывод списка авторов """
    model = Author
    paginate_by = 4


class AuthorDetail(DetailView):
    """ Вывод страницы автор-детально """
    model = Author


class AuthorCreate(CreateView):
    """ Создание автора """
    model = Author
    fields = '__all__'
    template_name = "library/author_create.html"
    success_url = reverse_lazy('author_list')


class AuthorUpdate(UpdateView):
    """ Редактирование автора """
    model = Author
    fields = ['first_name', 'second_name']
    success_url = reverse_lazy('author_list')


class AuthorDelete(DeleteView):
    """ Удаление автора """
    model = Author
    success_url = reverse_lazy('author_list')


class SearchResultsView(ListView):
    """ Поиск по книгам/описанию """
    model = Book
    template_name = 'library/search_results.html'
    success_url = reverse_lazy('author_list')

    def get_queryset(self):  # новый
        query = self.request.GET.get('descriptor')
        object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        return object_list
