from django.test import TestCase
from django.core.files import File

import requests
import os
import io

# Create your tests here.

KEY = 'ZTlt9Kqd2sFHqdwKiaR4TaDxU2vVCIFMhmCnb7Qk5WRzWJEc14y'

def test_gpt():
    
    r = requests.post(
        url='https://puankare-api-a9409a11e9e6.herokuapp.com/gpt',
        headers={
            'Authorization': KEY
        },

        json={
            "model": "gpt-4o",
            "messages": [
            {
            "role": "system",
            "content": [
                {
                "type": "text",
                "text": "You are a helpful assistant that answers programming questions in the style of a southern belle from the southeast United States."
                }
            ]
            },
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": "Are semicolons optional in JavaScript?"
                }
            ]
            }
            ]
        }
    )

    print(r.text)

def test_dalle():
    
    r = requests.post(
        url='https://puankare-api-a9409a11e9e6.herokuapp.com/dalle',
        headers={
            'Authorization': KEY
        },

        json={
            "prompt": "Spartans",
            "size": "1024x1024",
            "quality": "standard"
        }
    )

    print(r.text)

def test_stt():
    
    file = open('ttr1.mp3', 'rb')

    r = requests.post(
        url='https://puankare-api-a9409a11e9e6.herokuapp.com/stt',
        headers={
            'Authorization': KEY
        },

        data={
            'model': "whisper-1"
        },
        files={
            'file': file
        }
    )

    print(r.text)

def test_tts():

    r = requests.post(
        url='https://puankare-api-a9409a11e9e6.herokuapp.com/tts',
        headers={
            'Authorization': KEY
        },

        json={
            'model': 'tts-1',
            'voice': "echo",
            'input': 'Фото́н (от др.-греч. φῶς, фос — свет) — фундаментальная частица, квант электромагнитного излучения (в узком смысле — света) в виде поперечных электромагнитных волн и переносчик электромагнитного взаимодействия. Это безмассовая частица, способная существовать, только двигаясь со скоростью света. Электрический заряд фотона равен нулю. Фотон может находиться только в двух спиновых состояниях с проекцией спина на направление движения (спиральностью) ±1. В физике фотоны обозначаются буквой γ.'
        }
    )

    with open('audio.mp3', 'wb') as file:
        file.write(r.content)

    return None
