# Generated by Django 4.0.5 on 2022-06-08 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_tag_options_product_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='created_dt',
            new_name='created_at',
        ),
    ]
