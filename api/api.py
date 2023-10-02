import requests
import json

base_url = "https://jsonplaceholder.typicode.com/posts"

def validate_get_response(response):
    assert response.status_code == 200
    data = response.json()[0]
    assert isinstance(data['userId'], int)
    assert isinstance(data['id'], int)
    assert isinstance(data['title'], str)
    assert isinstance(data['body'], str)
    print("GET request successful. Response data types validated.")
    print("Response:")
    print(json.dumps(data, indent=4))

def validate_post_response(response, payload):
    assert response.status_code == 201
    response_data = response.json()
    expected_response = {**payload, "id": response_data["id"]}
    assert response_data == expected_response
    print("POST request successful. Response validated.")
    print("Response:")
    print(json.dumps(response_data, indent=4))

def send_get_request():
    response = requests.get(base_url)
    validate_get_response(response)

def send_post_request():
    payload = {
        "title": "recommendation",
        "body": "motorcycle",
        "userId": 12
    }
    response = requests.post(base_url, json=payload)
    validate_post_response(response, payload)

send_get_request()
send_post_request()
