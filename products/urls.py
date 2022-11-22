from django.urls import path

from .views import ProductListView, SalesListView, SaleCreateView

app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name="product-list"),
    path('sales_list/', SalesListView.as_view(), name='sales-list'),
    path('sale_create/', SaleCreateView.as_view(), name='sale-create'),
]
