import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_FILE = os.path.join(BASE_DIR, 'static')
FILE_NAME = PATH_FILE + '/photosFromInstagram.json'


def parse_insta():
	with open(FILE_NAME, "r", encoding='utf-8') as f:
		data = json.load(f)
	return data
