from random import choices
import string
import requests

def create_key():
    return ''.join(choices(string.ascii_letters+string.digits, k=50))

def send_created_key(key:str) -> str:

    r = requests.post(
        url='https://puankare-api-a9409a11e9e6.herokuapp.com/keys/add',
        headers={
            'Authorization': 'David'
        },

        json={
            'pk': key
        }

    )
    return r.status_code
