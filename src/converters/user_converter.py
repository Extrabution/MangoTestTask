from db.crud import User
from config import base_url


def convert_user_to_dto(user: User):
    return {'user_id':user.user_id,  'username':user.phone_number, 
     'about_me':user.about_me, 
     'photos':{'p50':f"{base_url}static/{user.phone_number}_50.jpeg", 
      'p100':f"{base_url}static/{user.phone_number}_100.jpeg", 
      'p400':f"{base_url}static/{user.phone_number}_400.jpeg", 
      'original':f"{base_url}static/{user.phone_number}_original.jpeg"}}
