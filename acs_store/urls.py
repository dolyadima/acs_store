from django.contrib import admin
from django.urls import path, include


app_name = 'acs_store'
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("products.urls", namespace="products")),
]
