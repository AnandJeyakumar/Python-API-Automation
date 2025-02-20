import requests
import json
import random
import string

BASE_URL = 'https://reqres.in/api/users'

def generate_random_name():
    return "Test" + ''.join(random.choices(string.digits, k=4))

def get_users():
    url = f"{BASE_URL}?page=2"
    response = requests.get(url)
    assert response.status_code == 200
    print(json.dumps(response.json(), indent=4))

def create_user():
    data = {"name": generate_random_name(), "job": "Automation Tester"}
    response = requests.post(BASE_URL, json=data)
    assert response.status_code == 201
    user_id = response.json().get("id")
    print(f"Created User ID: {user_id}")
    return user_id

def update_user(user_id):
    url = f"{BASE_URL}/{user_id}"
    data = {"name": generate_random_name(), "job": "Updated Automation Tester"}
    response = requests.put(url, json=data)
    assert response.status_code == 200
    print("The Updated User response ", json.dumps(response.json(), indent=4))

def delete_user(user_id):
    url = f"{BASE_URL}/{user_id}"
    response = requests.delete(url)
    assert response.status_code == 204
    print(f"User {user_id} deleted successfully.")


get_users()
user_id = create_user()
update_user(user_id)
delete_user(user_id)