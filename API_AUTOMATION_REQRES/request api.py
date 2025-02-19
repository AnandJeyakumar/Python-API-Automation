import requests
import json
import random
import string

baseurl = "https://gorest.co.in"
auth_token = "Bearer 9b00368668d90e8e197dc7f5170d12b7a067a5e9215f49f2da9392533191eadb"


def generate_random_string():
    domain = "automation.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for i in range (email_length))
    email = random_string +"@"+ domain
    print("The random email is ", email)
    return email


def getRequest():
    url = baseurl + "/public/v2/users"
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("The GET json data is ", json_str)



def post_request():
    url = baseurl + "/public/v2/users"
    headers = {"Authorization": auth_token}
    print("The POST URL is ",url)
    data = {
            "name": "Anand Automation",
            "email": generate_random_string(),
            "gender": "male",
            "status": "active"
    }
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("The POST json data is ", json_str)
    user_id = json_data["id"]
    assert "name" in json_data
    assert json_data["name"] == "Anand Automation"
    return user_id


def put_request(user_id):
    url = baseurl + f"/public/v2/users/{user_id}"
    headers = {"Authorization": auth_token}
    print("The PUT URL is ",url)
    data = {
        "name": "Anand Automation Tester",
        "email": generate_random_string(),
        "gender": "male",
        "status": "inactive"
    }
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("The PUT json data is ", json_str)
    assert json_data["name"]== "Anand Automation Tester"
    assert json_data["id"] == user_id


def delete_request(user_id):
    url = baseurl + f"/public/v2/users/{user_id}"
    headers = {"Authorization": auth_token}
    print("The DELETE URL is ", url)
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print("User deleted successfully")


#get
getRequest()
#post
user_id = post_request()
# put
put_request(user_id)

# Delete
delete_request(user_id)
