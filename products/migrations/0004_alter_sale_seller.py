# Generated by Django 4.1.3 on 2023-01-02 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_alter_sale_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='new_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
