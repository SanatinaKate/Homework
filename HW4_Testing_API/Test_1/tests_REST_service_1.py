import pytest
import requests


def is_image_valid(image, value=""):
    index = image.rfind(".")
    image_type = image[index:].lower()
    return (f"//images.dog.ceo/breeds/{value}" in image) and (image_type in (".png", ".jpg", ".jpeg"))


def test_list_all_breeds(base_url):
    response = requests.get(url=base_url + "breeds/list/all")
    assert response.status_code == 200
    json = response.json()
    assert list(json.keys()) == ["message", "status"]
    assert len(json["message"]) > 0
    assert json["status"] == "success"


@pytest.mark.parametrize("breed, sub_breeds", [
    ("bulldog", ["boston", "english", "french"]),
    ("dalmatian", []),
    ("mountain", ["bernese", "swiss"]),
    ("retriever", ["chesapeake", "curly", "flatcoated", "golden"]),
    ("springer", ["english"]),
])
def test_list_sub_breeds(base_url, breed, sub_breeds):
    response = requests.get(url=base_url + f"breed/{breed}/list")
    assert response.status_code == 200
    json = response.json()
    assert list(json.keys()) == ["message", "status"]
    assert json["message"] == sub_breeds
    assert json["status"] == "success"


def test_random_image(base_url):
    response = requests.get(url=base_url + "breeds/image/random")
    assert response.status_code == 200
    json = response.json()
    assert list(json.keys()) == ["message", "status"]
    assert is_image_valid(json["message"])
    assert json["status"] == "success"


@pytest.mark.parametrize("num_images", [1, 5, 10, 25, 50])
def test_multiple_random_images(base_url, num_images):
    response = requests.get(url=base_url + f"breeds/image/random/{num_images}")
    assert response.status_code == 200
    json = response.json()
    assert list(json.keys()) == ["message", "status"]
    message = json["message"]
    assert len(message) == num_images
    for image in message:
        assert is_image_valid(image)
    assert json["status"] == "success"


@pytest.mark.parametrize("breed", ["boxer", "doberman", "husky", "labrador", "samoyed"])
def test_images_by_breed(base_url, breed):
    response = requests.get(url=base_url + f"breed/{breed}/images")
    assert response.status_code == 200
    json = response.json()
    assert list(json.keys()) == ["message", "status"]
    message = json["message"]
    assert len(message) > 0
    for image in message:
        assert is_image_valid(image, value=breed)
    assert json["status"] == "success"
