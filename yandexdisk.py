import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        response = requests.get(
            'https://cloud-api.yandex.net/v1/disk/resources/upload',
            params={'path': file_path},
            headers={'Authorization': f'OAuth {self.token}'},
        )
        url = response.json()['href']
        files = {'file': open(os.path.split(file_path)[1], 'rb')}
        result = requests.put(url, files=files)
        return f'{result.status_code}\nФайл был успешно загружен на Яндекс-диск.'


if __name__ == '__main__':
    uploader = YaUploader(input('Введите токен: '))
    result = uploader.upload(input('Введите путь до файла: '))

print(result)
