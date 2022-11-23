from django.urls import reverse
from django.views.generic import ListView, CreateView

from .models import Product, Sale


class ProductListView(ListView):
    template_name = "products/product_list.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context["page_title"] = "Product List"
        return context


class SalesListView(ListView):
    model = Sale
    template_name = "products/sales_list.html"


class SaleCreateView(CreateView):
    model = Sale
    fields = '__all__'
    template_name = 'products/sale_create.html'

    def get_success_url(self):
        return reverse('products:sales-list')
