from api_e2e import E2e
from data import LoginData

pet = E2e()
LD = LoginData()
result = pet.full_story()

def test_e2e():
    """POST register user"""
    user_token_register = result[0]
    user_email_register = result[1]
    user_id_register = result[2]
    status_code_register = result[3]
    """POST login user"""
    user_token_login = result[4]
    user_email_login = result[5]
    user_id_login = result[6]
    status_code_login = result[7]
    """POST pet Save (create pet)"""
    pet_id_create_pet = result[8]
    status_code_create_pet = result[9]
    """PATCH pet Update"""
    pet_id_update_pet = result[10]
    status_code_update_pet = result[11]
    """POST Upload image pet"""
    link_upload_image = result[12]
    status_code_upload_image = result[13]
    """PUT add like"""
    status_code_like = result[14]
    """PUT add comment"""
    id_comment = result[15]
    status_code_comment = result[16]
    """DELETE pet"""
    status_code_delete_pet = result[17]
    """DELETE user"""
    status_code_delete_user = result[18]
    assert user_token_register
    assert user_email_register
    assert user_id_register
    assert status_code_register == 200
    assert user_token_login
    assert user_email_login
    assert user_id_login
    assert status_code_login == 200
    assert pet_id_create_pet
    assert status_code_create_pet == 200
    assert pet_id_update_pet
    assert status_code_update_pet == 200
    assert link_upload_image
    assert status_code_upload_image == 200
    assert status_code_like == 200
    assert id_comment
    assert status_code_comment == 200
    assert status_code_delete_pet == 200
    assert status_code_delete_user == 200
