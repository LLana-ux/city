from django.views.generic import ListView
from .models import Product


class ProductsList(ListView):

    model = Product

    ordering = 'name'

    template_name = 'products.html'

    context_object_name = 'products'

    from django.views.generic import ListView, DetailView
    from .models import Product

    class ProductsList(ListView):

        model = Product

        ordering = 'name'

        template_name = 'products.html'

        context_object_name = 'products'

    class ProductDetail(DetailView):

        model = Product

        template_name = 'product.html'

        context_object_name = 'product'

    class ProductsList(ListView):
            model = Product
            template_name = 'products.html'
            context_object_name = 'products'

    from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import Product

    class ProductsList(ListView):
        model = Product
        ordering = 'name'
        template_name = 'products.html'
        context_object_name = 'products'


        def get_context_data(self, **kwargs):

            context = super().get_context_data(**kwargs)

            context['time_now'] = datetime.utcnow()

            context['next_sale'] = None
            return context

    class ProductsList(ListView):
        model = Product
        ordering = 'name'
        template_name = 'products.html'
        context_object_name = 'products'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['time_now'] = datetime.utcnow()
            context['next_sale'] = "Распродажа в среду!"
            return context

from django.views.generic import ListView, DetailView
from .models import Product
    class ProductsList(ListView):
        model = Product
        ordering = 'name'
        template_name = 'products.html'
        context_object_name = 'products'
        paginate_by = 2

from django.views.generic import ListView, DetailView
from .models import Product
from .filters import ProductFilter

    class ProductsList(ListView):
        model = Product
        ordering = 'name'
        template_name = 'products.html'
        context_object_name = 'products'
        paginate_by = 2

        # Переопределяем функцию получения списка товаров
        def get_queryset(self):
            # Получаем обычный запрос
            queryset = super().get_queryset()
            # Используем наш класс фильтрации.
            # self.request.GET содержит объект QueryDict, который мы рассматривали
            # в этом юните ранее.
            # Сохраняем нашу фильтрацию в объекте класса,
            # чтобы потом добавить в контекст и использовать в шаблоне.
            self.filterset = ProductFilter(self.request.GET, queryset)
            # Возвращаем из функции отфильтрованный список товаров
            return self.filterset.qs

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            # Добавляем в контекст объект фильтрации.
            context['filterset'] = self.filterset
            return context

    class ProductDetail(DetailView):
        model = Product
        template_name = 'product.html'
        context_object_name = 'product'


from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView
)

from .filters import ProductFilter
from .forms import ProductForm
from .models import Product


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'



class ProductCreate(CreateView):

    form_class = ProductForm

    model = Product

    template_name = 'product_edit.html'

from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView
)

from .filters import ProductFilter
from .forms import ProductForm
from .models import Product


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


class ProductCreate(CreateView):
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'



class ProductUpdate(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'

    from django.urls import reverse_lazy
    from django.views.generic import (
        ListView, DetailView, CreateView, UpdateView, DeleteView
    )

    from .filters import ProductFilter
    from .forms import ProductForm
    from .models import Product

    class ProductsList(ListView):
        model = Product
        ordering = 'name'
        template_name = 'products.html'
        context_object_name = 'products'
        paginate_by = 2

        def get_queryset(self):
            queryset = super().get_queryset()
            self.filterset = ProductFilter(self.request.GET, queryset)
            return self.filterset.qs

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['filterset'] = self.filterset
            return context

    class ProductDetail(DetailView):
        model = Product
        template_name = 'product.html'
        context_object_name = 'product'

    class ProductCreate(CreateView):
        form_class = ProductForm
        model = Product
        template_name = 'product_edit.html'

    class ProductUpdate(UpdateView):
        form_class = ProductForm
        model = Product
        template_name = 'product_edit.html'

    # Представление удаляющее товар.
    class ProductDelete(DeleteView):
        model = Product
        template_name = 'product_delete.html'
        success_url = reverse_lazy('product_list')


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_premium'] = not self.request.user.groups.filter(name='premium').exists()
        return context

from django.core.cache import cache # импортируем наш кэш

class ProductDetailView(DetailView):
   template_name = 'sample_app/product_detail.html'
   queryset = Product.objects.all()

   def get_object(self, *args, **kwargs): # переопределяем метод получения объекта, как ни странно

      obj = cache.get(f'product-{self.kwargs["pk"]}', None) # кэш очень похож на словарь, и метод get действует так же. Он забирает значение по ключу, если его нет, то забирает None.

      #если объекта нет в кэше, то получаем его и записываем в кэш

      if not obj:
         obj = super().get_object(queryset=self.queryset)
         cache.set(f'product-{self.kwargs["pk"]}', obj)

      return obj