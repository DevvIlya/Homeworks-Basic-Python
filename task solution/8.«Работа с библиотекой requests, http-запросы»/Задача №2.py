import requests

with open('token.txt', 'r') as file_object:
    TOKEN = file_object.read().strip()

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

def upload_file(loadfile, savefile, replace=False):
    res = requests.get(f'{URL}/upload?path={savefile}&overwrite={replace}', headers=headers).json()
    with open(loadfile, 'rb') as f:
        try:
            requests.put(res['href'], files={'file':f})
        except KeyError:
            print(res)

upload_file(r'G:\photo_2022-05-08_16-37-26.jpg', 'photo_2022-05-08_16-37-26.jpg')