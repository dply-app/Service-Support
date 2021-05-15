import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

data = '{ "User_email": "shinjae541969@gmail.com", "question": "string" }'

response = requests.post('http://localhost:8000/ask', headers=headers, data=data)