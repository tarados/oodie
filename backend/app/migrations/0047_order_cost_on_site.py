# Generated by Django 3.0.7 on 2020-12-04 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0046_auto_20201203_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cost_on_site',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Стоимость доставки, грн.'),
        ),
    ]