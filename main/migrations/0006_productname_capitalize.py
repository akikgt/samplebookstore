# Generated by Django 3.0 on 2019-12-03 04:47

from django.db import migrations

def capitalize(apps, schema_editor):
    Product = apps.get_model('main', 'Product')
    # why use get_model?
    # because at the point of execution of the migration, the database schema will be different
    # than the schema declared in the models file
    for product in  Product.objects.all():
        product.name = product.name.capitalize()
        product.save()

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191203_0107'),
    ]

    operations = [
        migrations.RunPython(
            capitalize,
            migrations.RunPython.noop
        )
    ]
