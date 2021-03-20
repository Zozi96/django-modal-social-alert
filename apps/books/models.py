from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    title = models.CharField(verbose_name='Titulo del libro', max_length=100)
    date_release = models.DateField(verbose_name='Fecha de estreno')

    class Meta:
        app_label = 'books'
        db_table = 'libro'
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __str__(self):
        return str(self.title)
