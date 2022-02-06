import datetime
import os
import json
from backend.settings import BASE_DIR
from app.models import Localization

filename = os.path.join(BASE_DIR, 'static', 'locales.json')


def export_locales():
    localizations = Localization.objects.all()
    locale = {}
    for el in localizations:
        val_el = [el.value, el.value_ua]
        locale.update({
            el.key: val_el
        })
    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(locale, outfile, ensure_ascii=False, indent=4)


def delete_localization():
    Localization.objects.all().delete()


def import_locales():
    locale = {}
    with open(filename, 'r', encoding='utf-8') as outfile:
        locale.update(json.load(outfile))
    for key, val in locale.items():
        locales = Localization(
            key=key,
            value=val[0],
            value_ua=val[1]
        )
        locales.save()


"""Экспорт локалей из БД производим по схеме:
 1. В терминале выполяем  python manage.py export
  """