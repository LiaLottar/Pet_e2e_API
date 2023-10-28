import json
import requests
from data import LoginData

LD = LoginData()
class Pets:
    """api библиотека для Swagger'a url http://34.141.58.52:80/#/"""

    def __init__(self):
        self.base_url = "http://34.141.58.52:8000/"

    def login_user(self) -> json:
        """запрос к Swagger'y, чтобы получить токен пользователя из request, используя валидный логин и пароль"""
        data = {
            "email": LD.VALID_EMAIL,
            "password": LD.VALID_PASSWORD
        }
        response = requests.post(self.base_url + "login", data=json.dumps(data))
        user_token = response.json()["token"]
        user_id = response.json()["id"]
        status_code = response.status_code
        return user_token, user_id, status_code

    def create_pet(self) -> json:
        """для эндпоинта метода POST Pet Save"""
        user_id = self.login_user()[1]
        user_token = self.login_user()[0]
        headers = {"Authorization": f'Bearer {user_token}'}
        data = {
            "name": "PetXo",
            "type": "dog",
            "age": 1,
            "gender": "Male",
            "owner_id": user_id
        }
        response = requests.post(self.base_url + "pet", data=json.dumps(data), headers=headers)
        pet_id = response.json()["id"]
        status_code = response.status_code
        return pet_id, status_code

    def get_users(self) -> json:
        user_token = self.login_user()[0]
        headers = {"Authorization": f'Bearer {user_token}'}
        response = requests.get(self.base_url + "users", headers=headers)
        user_id = response.json()
        status_code = response.status_code
        return user_id, status_code

    def update_pet(self) -> json:
        user_token = self.login_user()[0]
        headers = {"Authorization": f'Bearer {user_token}'}
        data = {
            "name": "petXoXo",
            "type": "cat",
            "age": 8,
            "gender": "Female",
            "owner_id": 0,
            "pic": "string",
            "owner_name": "string",
            "likes_count": 0
            }
        response = requests.patch(self.base_url + "pet", data=json.dumps(data), headers=headers)
        pet_id = response.json()["id"]
        status_code = response.status_code
        return pet_id, status_code

    def upload_image(self) -> json:
        pet_id = self.create_pet()[0]
        user_token = self.login_user()[0]
        headers = {"Authorization": f'Bearer {user_token}'}
        files = {'pic': ('pet1.jpg', open('C:/Users/lialo/PycharmProjects/PetAPI/Picture/pet1.jpg', 'rb'), 'image/jpg' )}
        response = requests.post(self.base_url + f'pet/{pet_id}/image', files=files, headers=headers)
        link = response.json()['link']
        status_code = response.status_code
        return link, status_code

    def pet_like(self) -> json:
        pet_id = self.create_pet()[0]
        user_token = self.login_user()[0]
        headers = {"Authorization": f'Bearer {user_token}'}
        response = requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
        status_code = response.status_code
        return status_code

    def pet_comment(self) -> json:
        pet_id = self.create_pet()[0]
        user_token = self.login_user()[0]
        headers = {"Authorization": f'Bearer {user_token}'}
        data = {
            "message": "so beautiful"
        }
        response = requests.put(self.base_url + f'pet/{pet_id}/comment', data=json.dumps(data), headers=headers)
        id_like = response.json()["id"]
        status_code = response.status_code
        return id_like, status_code

    def delete_pet(self) -> json:
        user_token = self.login_user()[0]
        pet_id = self.create_pet()[0]
        headers = {"Authorization": f'Bearer {user_token}'}
        response = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status_code = response.status_code
        return pet_id, status_code

    def delete_user(self) -> json:
        user_token = self.login_user()[0]
        user_id = self.login_user()[1]
        headers = {"Authorization": f'Bearer {user_token}'}
        response = requests.delete(self.base_url + f'users/{user_id}', headers=headers)
        status_code = response.status_code
        return status_code


Pets().login_user()
Pets().create_pet()
Pets().get_users()
Pets().update_pet()
Pets().upload_image()
Pets().pet_like()
Pets().pet_comment()
Pets().delete_pet()
Pets().delete_user()