# Generated by Django 3.0.7 on 2021-11-27 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0054_remove_localization_value_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_locale',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='name_translate', to='app.Localization', verbose_name='перевод категории'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, verbose_name='название категории'),
        ),
    ]