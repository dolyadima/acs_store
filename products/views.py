from django.urls import reverse
from django.views.generic import CreateView, TemplateView

from .models import Product, Sale, Category, Shop


class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductsListView(TemplateView):
    template_name = "products/product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context['categories'] = Category.objects.all()
        context['shops'] = Shop.objects.all()
        prod_title = self.request.GET.get('title', '')

        category = self.request.GET.get('category', '')
        shop = self.request.GET.get('shop', '')

        context['category_pk'] = -1
        context['shop_pk'] = -1
        price1 = self.request.GET.get('min_price', 0.0)
        price2 = self.request.GET.get('max_price', 0.0)

        if prod_title or category or shop or price1 or price2:
            product_set = products
            if prod_title != '':
                product_set = products.filter(title__icontains=prod_title)
            if category != '-1':
                product_set = product_set.filter(category_id=category)
                context['category_pk'] = int(category)
            if shop != '-1':
                product_set = product_set.filter(shop_id=shop)
                context['shop_pk'] = int(shop)
            if price2 != '' and price1 != '':
                product_set = product_set.filter(price__range=(price1, price2))
            context['products'] = product_set
        else:
            context['products'] = products
        return context


class SalesListView(TemplateView):
    template_name = "products/sales_list.html"

    def get_context_data(self, **kwargs):
        print('one', 'two')
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
