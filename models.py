from django.db import models
from django.core.validators import MinValueValidator



class Product(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )

    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='products', # все продукты в категории будут доступны через поле products
    )
    price = models.FloatField(
        validators=[MinValueValidator(0.0)],
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'



class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()

from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='products',
    )
    price = models.FloatField(
        validators=[MinValueValidator(0.0)],
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:10]}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()

from django.contrib.auth.mixins import PermissionRequiredMixin


class MyView(PermissionRequiredMixin, View):
    permission_required = ('<app>.<action>_<model>',
                           '<app>.<action>_<model>')

from django.views.generic.edit import CreateView

class AddProduct(PermissionRequiredMixin, CreateView):
    permission_required = ('shop.add_product', )
 