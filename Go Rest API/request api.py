import requests
import json
import random
import string

baseurl = "https://gorest.co.in"
auth_token = "Bearer 9b00368668d90e8e197dc7f5170d12b7a067a5e9215f49f2da9392533191eadb"


def getRequest():
    url = baseurl + "/public/v2/users"
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("The json data is ", json_str)



def post_request():
    url = baseurl + "/public/v2/users"
    headers = {"Authorization": auth_token}
    data = {
            "name": "Anand Automation",
            "email": "Automation@auto.com",
            "gender": "male",
            "status": "active"
    }
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("The json data is ", json_str)
    user_id = json_data["id"]
    assert "name" in json_data
    assert json_data["name"] == "Anand Automation"
    return user_id

#
getRequest()

#post
# post_request()




# put


#delete
