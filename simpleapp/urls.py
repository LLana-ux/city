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