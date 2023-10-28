import json
import requests
from data import LoginData
import uuid

LD = LoginData()

class E2e:

    def __init__(self):
        self.base_url = "http://34.141.58.52:8000/"

    def full_story(self) -> json:
        """POST register user"""
        email = uuid.uuid4().hex
        data_register = {
            "email": f"{email}@gmail.com",
            "password": LD.VALID_PASSWORD_1,
            "confirm_password": LD.CONFIRM_PASSWORD_1
        }
        response = requests.post(self.base_url + "register", data=json.dumps(data_register))
        user_token_register = response.json()["token"]
        user_email_register = response.json()["email"]
        user_id_register = response.json()["id"]
        status_code_register = response.status_code
        """POST login user"""
        data_login = {
            "email": user_email_register,
            "password": LD.VALID_PASSWORD_1
       }
        response = requests.post(self.base_url + "login", data=json.dumps(data_login))
        user_token_login = response.json()["token"]
        user_email_login = response.json()["email"]
        user_id_login = response.json()["id"]
        status_code_login = response.status_code
        """POST pet Save (create pet)"""
        headers = {"Authorization": f'Bearer {user_token_login}'}
        data_create_pet = {
            "name": "PetXoly",
            "type": "dog",
            "age": 1,
            "gender": "Male",
            "owner_id": user_id_login
        }
        response = requests.post(self.base_url + "pet", data=json.dumps(data_create_pet), headers=headers)
        pet_id_create_pet = response.json()["id"]
        status_code_create_pet = response.status_code
        """PATCH pet Update"""
        headers = {"Authorization": f'Bearer {user_token_login}'}
        data_update_pet = {
            "id": pet_id_create_pet,
            "name": "Cute pet",
            "type": "hamster",
            "age": 5,
            "gender": "Male",
            "owner_id": user_id_login,
            "likes_count": 0
        }
        response = requests.patch(self.base_url + "pet", data=json.dumps(data_update_pet), headers=headers)
        pet_id_update_pet = response.json()["id"]
        status_code_update_pet = response.status_code
        """POST Upload image pet"""
        headers = {"Authorization": f'Bearer {user_token_login}'}
        files = {'pic': ('pet1.jpg', open('C:/Users/lialo/PycharmProjects/PetAPI/Picture/pet1.jpg', 'rb'), 'image/jpg')}
        response = requests.post(self.base_url + f'pet/{pet_id_update_pet}/image', files=files, headers=headers)
        link_upload_image = response.json()['link']
        status_code_upload_image = response.status_code
        """PUT add like"""
        headers = {"Authorization": f'Bearer {user_token_login}'}
        response = requests.put(self.base_url + f'pet/{pet_id_update_pet}/like', headers=headers)
        status_code_like = response.status_code
        """PUT add comment"""
        headers = {"Authorization": f'Bearer {user_token_login}'}
        data_comment = {
            "message": "so beautiful"
        }
        response = requests.put(self.base_url + f'pet/{pet_id_update_pet}/comment', data=json.dumps(data_comment), headers=headers)
        id_comment = response.json()["id"]
        status_code_comment = response.status_code
        """DELETE pet"""
        headers = {"Authorization": f'Bearer {user_token_login}'}
        response = requests.delete(self.base_url + f"pet/{pet_id_update_pet}", headers=headers)
        status_code_delete_pet = response.status_code
        """DELETE user"""
        headers = {"Authorization": f'Bearer {user_token_login}'}
        response = requests.delete(self.base_url + f'users/{user_id_login}', headers=headers)
        status_code_delete_user = response.status_code

        return user_token_register, user_email_register, user_id_register, status_code_register, user_token_login,\
            user_email_login, user_id_login, status_code_login, pet_id_create_pet, status_code_create_pet,\
            pet_id_update_pet, status_code_update_pet, link_upload_image, status_code_upload_image, status_code_like, \
            id_comment, status_code_comment, status_code_delete_pet, status_code_delete_user

E2e().full_story()