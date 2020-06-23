import requests
from requests.exceptions import RequestException

import os

# имя файла со списком ссылок на изображения
FILE_NAME_LINKLIST = 'unicorn-oodie.txt'

# путь куда сохраняем полученные image file
MEDIA_PATH = 'C:\\Users\\KOMPotdel\\projects\\oodie\\backend\\media\\images'
# путь куда сохраняем файлы со списком ссылок спарсинных с сайта
FILE_PATH = 'C:\\Users\\KOMPotdel\\projects\\oodie\\backend\\media'

path_file = os.path.join(FILE_PATH, FILE_NAME_LINKLIST)
with open(path_file) as infile:
    data = infile.read().split('\n')


def fetch_img(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    try:
        result = requests.get(url, headers=headers)
    except RequestException:
        print(url)
    str = FILE_NAME_LINKLIST.split('.')[0]
    str_name = url.split('/')[-1]
    file_name = '{0}.{1}'.format(str, str_name.split('.')[0] + '.jpg')
    path_file = os.path.join(MEDIA_PATH, file_name)
    out = open(path_file, "wb")
    out.write(result.content)
    out.close()


for url in data:
    fetch_img(url)
