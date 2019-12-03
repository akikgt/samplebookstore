# Generated by Django 3.0 on 2019-12-03 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_productname_capitalize'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttag',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='main.ProductTag'),
        ),
    ]