

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import random


cred = credentials.Certificate('key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://itcnov-6b7cc-default-rtdb.firebaseio.com"
})

USER_DB={}

def populate():
    data_base= db.reference('/users').get()
    
    for data in data_base.values():
        print(data)
        USER_DB[data['email']]=data
        



def get_udid():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(16))


def check(username,password):
    uname=USER_DB.get(username)
    if uname is None:
        return False
    if(uname.get('uid'))==password:
        return True
    else:
        return False



def insert(fullname,email,new_username,new_password):
    ref = db.reference('/users')
    data={get_udid(): {'email': email, 'name': fullname, 'role': {'val': 'customer'}, 'uid': new_password}}
    ref.update(data)
    populate()

populate()