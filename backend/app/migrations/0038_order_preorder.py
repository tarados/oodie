# Generated by Django 3.0.7 on 2020-11-14 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_auto_20201114_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='preorder',
            field=models.BooleanField(default=False, verbose_name='Предзаказ'),
        ),
    ]