# Generated by Django 3.0.7 on 2020-11-14 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20201110_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='pre_order',
            field=models.BooleanField(default=False, verbose_name='Предзаказ'),
        ),
        migrations.AddField(
            model_name='product',
            name='pre_order',
            field=models.BooleanField(default=False, verbose_name='Предзаказ'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Новый'), (2, 'В обработке'), (3, 'Выполнен'), (4, 'Предзаказ'), (5, 'Отменен')], default=1, verbose_name='Статус'),
        ),
    ]