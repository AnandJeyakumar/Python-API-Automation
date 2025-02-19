import requests
import json
import random
import string

base_url = 'https://reqres.in/api/users'
random_number_length = 4

def generate_random_name():
    random_number = ''.join(random.choice(string.digits) for _ in range(random_number_length))
    return f"Test{random_number}"


def get_users_from_page2():
    url = f"{base_url}?page=2"
    print("The Get URL is ", url)
    response = requests.get(url)
    assert response.status_code == 200
    response.raise_for_status()
    json_data = response.json()
    result = json.dumps(json_data, indent=4)
    print("The Get Result is ", result)


def post_users():
    print("The Post URL is ", base_url)
    create_user_data = {
        "name": generate_random_name(),
        "job": "Automation Tester"
    }
    response = requests.post(base_url, json=create_user_data)
    assert response.status_code == 201
    json_data = response.json()
    result = json.dumps(json_data, indent=4)
    print("The Post Result is ", result)
    assert json_data['job'] == "Automation Tester"
    print("The ID created is ", json_data['id'])
    return json_data['id']


# post_users(base_url)

def update_user(user_id):
    url_end_point = base_url + "/" + user_id
    print("The Update URL is ", url_end_point)
    updated_name = generate_random_name()
    update_user_data = {
        "name": updated_name,
        "job": "Updated Automation Tester"
    }
    response = requests.put(url_end_point, json=update_user_data)
    assert response.status_code == 200
    json_data = response.json()
    print("The generate_random_numbers()" , updated_name)
    assert json_data["name"] == updated_name
    data = json.dumps(json_data, indent=4)
    print("The Update Result is ", data)
    print("---------The update is done-------------")


def delete_user(user_id):
    url_end_point = base_url + "/" + user_id
    print("The Delete URL is ", url_end_point)
    response = requests.delete(url_end_point)
    print("The delete status code is", response.status_code)
    assert response.status_code == 204
    print("---------The Delete is done-------------")


get_users_from_page2()
user_id = post_users()
update_user(user_id)
delete_user(user_id)
