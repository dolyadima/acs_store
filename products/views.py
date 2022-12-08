from django.urls import reverse
from django.views.generic import ListView, CreateView, TemplateView

from .filters import ProductFilter
from .models import Product, Sale, Category, Shop


class IndexView(TemplateView):
    template_name = 'products/index.html'


class ProductsListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/product_list.html"
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Product List"
        context["form"] = self.filterset.form
        context["object_list"] = Product.objects.all()
        return context


class SalesListView(TemplateView):
    template_name = "products/sales_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.all()
        context['shops'] = Shop.objects.all()
        sales = Sale.objects.all()

        sale_cat_form_select = self.request.GET.get('sale_cat', '')
        sale_shop_form_select = self.request.GET.get('sale_shop', '')

        context['cat_pk'] = -1
        context['shop_pk'] = -1

        if sale_cat_form_select.isdigit() and sale_cat_form_select != '-1':
            sales = sales.filter(product__category_id=sale_cat_form_select)
            context['cat_pk'] = int(sale_cat_form_select)

        if sale_shop_form_select.isdigit() and sale_shop_form_select != '-1':
            sales = sales.filter(product__shop_id=sale_shop_form_select)
            context['shop_pk'] = int(sale_shop_form_select)

        context['sales'] = sales

        return context


class SaleCreateView(CreateView):
    model = Sale
    fields = '__all__'
    template_name = 'products/sale_create.html'

    def get_success_url(self):
        return reverse('products:sales-list')
