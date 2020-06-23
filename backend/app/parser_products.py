import requests
import os

# имя файла со списком ссылок на изображения
FILE_NAME_LINKLIST = 'oodie-family-pack.txt'

# путь куда сохраняем полученные image file
MEDIA_PATH = '/home/sergey/projects/oodie/backend/media/images/'
# путь куда сохраняем файлы со списком ссылок спарсинных с сайта
FILE_PATH = '/home/sergey/projects/oodie/backend/media/'


link_list = []
path_file = os.path.join(FILE_PATH, FILE_NAME_LINKLIST)
with open(path_file) as infile:
	data = infile.read()
	link_list.append(data)


def fetch_img(url):
	headers = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
	result = requests.get(url, headers=headers)
	file_name = url.split('/')[len(url.split('/')) - 1].split('.')[0] + '.jpg'
	# path_file = os.path.join(MEDIA_PATH, file_name)
	out = open(file_name, "wb")
	out.write(result.content)
	out.close()


# for url in link_list:
# 	print(url)
fetch_img('https://cdn.shopify.com/s/files/1/0023/7427/1029/products/reindeer_snowman_110x110@2x.jpg?v=1591944171')