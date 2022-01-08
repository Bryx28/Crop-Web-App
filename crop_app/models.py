from crop_app import login_manager
from flask_login import UserMixin
import requests

@login_manager.user_loader
def load_user(user_id):
    if type(user_id) is not None:
        data = requests.get(f'http://127.0.0.1:5000/load_user/{user_id}')
    else:
        data = None
    return User(data)

class User(UserMixin):
    def __init__(self, user_json):
        self.user_json = user_json
        self.user_data = self.user_json.json()
        self.get_current_user_data()

    def get_id(self):
        object_id = self.user_data['user_id']
        return str(object_id)

    def get_current_user_data(self):
        self.user_id = self.user_data['user_id']
        self.user_image = self.user_data['user_image']
        self.user_fname = self.user_data['user_fname']
        self.user_mname = self.user_data['user_mname']
        self.user_lname = self.user_data['user_lname']
        self.username = self.user_data['username']
        self.email = self.user_data['email']