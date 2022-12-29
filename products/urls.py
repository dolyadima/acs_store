from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import IndexView, ProductsListView, SalesListView, SaleCreateView

app_name = 'products'
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('products-list/', ProductsListView.as_view(), name="products-list"),
    path('sales-list/', login_required(SalesListView.as_view()), name='sales-list'),
    path('sale-create/', SaleCreateView.as_view(), name='sale-create'),
]
