import datetime
import os
import json
from backend.settings import BASE_DIR
from app.models import Localization

filename = os.path.join(BASE_DIR, 'static', 'locales.json')


def export_locales():
    localizations = Localization.objects.all()
    locale = {}
    key_ru = {}
    key_ua = {}
    key_en = {}
    for el in localizations:
        key_ru.update({el.key: el.value})
        key_ua.update({el.key: el.value_ua})
        key_en.update({el.key: el.value_en})
    locale.update({
        'ru-RU': key_ru,
        'ua-UA': key_ua,
        'en-US': key_en
    })
    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(locale, outfile, ensure_ascii=False, indent=4)


def delete_localization():
    Localization.objects.all().delete()


def import_locales():
    print('fg')
    # with open(filename, 'r', encoding='utf-8') as outfile:
    #     print(json.load(outfile))


"""Экспорт локалей из БД производим по схеме:
 1. В терминале выполяем  python manage.py export
  """
