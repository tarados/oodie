# Generated by Django 3.0.7 on 2020-11-01 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_orderitem_quantity_breakpoint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='quantity_breakpoint',
        ),
    ]
