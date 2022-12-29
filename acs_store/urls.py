from django.contrib import admin
from django.urls import path, include

app_name = 'acs_store'
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("products.urls", namespace="products")),
    path('accounts/', include(('django.contrib.auth.urls', 'accounts'), namespace="accounts")),
    path('auth/', include('authentication.urls', namespace="auth")),
]
