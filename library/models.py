from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    """ Модель автора """
    first_name = models.CharField(max_length=150, verbose_name=_('first name'), null=True, blank=True)
    second_name = models.CharField(max_length=150, verbose_name=_('second name'), null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'


class Book(models.Model):
    """ Модель книг """
    author = models.ManyToManyField(Author)
    title = models.CharField(max_length=50, verbose_name=_('title'))
    description = models.TextField(max_length=300, verbose_name=_('description'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={"pk": self.pk})