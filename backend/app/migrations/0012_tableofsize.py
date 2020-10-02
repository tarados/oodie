# Generated by Django 3.0.7 on 2020-10-02 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200930_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableOfSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Название модели')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Таблица размеров')),
            ],
        ),
    ]