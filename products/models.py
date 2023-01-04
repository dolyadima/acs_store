from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Product(models.Model):
    title = models.CharField(verbose_name=_("Product title"), max_length=255, blank=False, null=False)
    category = models.ForeignKey("Category", verbose_name=_("Product category"), blank=False, null=False, related_name="product_category", on_delete=models.PROTECT)
    amount = models.PositiveIntegerField(verbose_name=_("Product amount"), blank=False, null=False)
    price = models.FloatField(verbose_name=_("Product price"), blank=False, null=False)
    shop = models.ForeignKey("Shop", verbose_name=_("Product shop"), blank=False, null=False, related_name="product_shop", on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):
    title = models.CharField(verbose_name=_("Category title"), max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return f"{self.title}"


class Shop(models.Model):
    address = models.CharField(verbose_name=_("Shop address"), max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = _("Shop")
        verbose_name_plural = _("Shops")

    def __str__(self):
        return f"{self.address}"


class Sale(models.Model):
    date_time = models.DateTimeField(verbose_name=_("Sale date and time"), auto_now_add=True)
    product = models.ForeignKey("Product", verbose_name=_("Sale product"), blank=False, null=False, related_name="sale_product", on_delete=models.PROTECT)
    amount = models.PositiveIntegerField(verbose_name=_("Sale amount"), blank=False, null=False)
    price = models.FloatField(verbose_name=_("Sale price"), blank=False, null=False)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("Sale")
        verbose_name_plural = _("Sales")

    def __str__(self):
        return f"{self.product}"
