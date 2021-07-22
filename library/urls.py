from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *


urlpatterns = [
    path('', BooksList.as_view(), name='book_list'),
    path('<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('authors', AuthorList.as_view(), name='author_list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author_detail'),
    path('<int:pk>/update_book', login_required(BookUpdate.as_view()), name='update_book'),
    path('authors/<int:pk>/update_author', login_required(AuthorUpdate.as_view()), name='update_author'),
    path('create_book/', login_required(BookCreate.as_view()), name='create_book'),
    path('authors/create_author/', login_required(AuthorCreate.as_view()), name='create_author'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('<int:pk>/delete_book/', login_required(BookDelete.as_view()), name='delete_book'),
    path('authors/<int:pk>/delete_author/', login_required(AuthorDelete.as_view()), name='delete_author'),
]
