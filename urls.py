from django.urls import path

from .views import ProductsList


urlpatterns = [

   path('', ProductsList.as_view()),
]

from django.urls import path

from .views import ProductsList, ProductDetail

urlpatterns = [

   path('', ProductsList.as_view()),

   path('<int:pk>', ProductDetail.as_view()),
]


from django.urls import path
from .views import (
    ProductsList, ProductDetail, ProductCreate
)

urlpatterns = [
    path('', ProductsList.as_view(), name='product_list'),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('create/', ProductCreate.as_view(), name='product_create'),
]

from django.urls import path
from .views import (
    ProductsList, ProductDetail, ProductCreate, ProductUpdate
)

urlpatterns = [
    path('', ProductsList.as_view(), name='product_list'),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
]

from django.urls import path
from .views import (
    ProductsList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete
)

urlpatterns = [
    path('', ProductsList.as_view(), name='product_list'),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
]

from django.contrib import admin
from django.urls import path, include
from news.views import BecomeAnAuthor, profile, ChangePasswordView # , ShowProfilePageView, CreateProfilePageView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('accounts/', include('allauth.urls')),
    path('success/', BecomeAnAuthor.as_view(), name = 'success'),
    path('profile/', profile, name='users-profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from .views import Products, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', Products.as_view()),
    path('<int:pk>/', cache_page(60 * 10)(ProductDetailView.as_view()), name='product_detail'),
    # добавим кэширование на детали товара. Раз в 10 минут товар будет записываться в кэш для экономии ресурсов.
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
]