from django.views.generic import ListView

from .models import Product


class ProductListView(ListView):
    template_name = "products/product_list.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context["page_title"] = "Product List"
        return context
