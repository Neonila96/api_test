import pytest
import requests

@pytest.fixture(scope="module")
def base_url():
    base_url =  "https://petstore.swagger.io/v2"
    return base_url

@pytest.fixture(scope="module")
def pet_id():
    pet_id =  1
    return pet_id

@pytest.fixture(autouse=True, scope="module")
def setup(base_url, pet_id):

    data = {
        "id": pet_id,
        "name": "Fluffy",
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "photoUrls": [
            "http://example.com/photos/fluffy"
        ],
        "tags": [
            {
                "id": 1,
                "name": "friendly"
            }
        ],
        "status": "available"
    }
    response = requests.post(f'{base_url}/pet', json=data)
    print("Setup - Create pet response:", response.text)
    assert response.status_code == 200


    yield
    response = requests.delete(f'{base_url}/pet/{pet_id}')
    print("Teardown - Delete pet response:", response.text)
    assert response.status_code == 200

def test_pet_operations(base_url, pet_id):

    update_data = {
        "id": pet_id,
        "name": "Fluffy",
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "photoUrls": [
            "http://example.com/photos/fluffy"
        ],
        "tags": [
            {
                "id": 1,
                "name": "friendly"
            }
        ],
        "status": "sold"
    }
    response = requests.put(f'{base_url}/pet', json=update_data)
    print("Update pet response:", response.text)
    assert response.status_code == 200


    response = requests.get(f'{base_url}/pet/{pet_id}')
    print("Get pet response:", response.text)
    assert response.status_code == 404




