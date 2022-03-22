from jsonschema import validate
import pytest
import requests


@pytest.mark.parametrize("resource_id", range(1, 11))
def test_get_resource_by_id(base_url, schema, resource_id):
    response = requests.get(url=base_url + f"posts/{resource_id}")
    assert response.status_code == 200
    json = response.json()
    assert len(json) > 0
    validate(instance=json, schema=schema)


@pytest.mark.parametrize("user_id", range(1, 11))
def test_filter_resources(base_url, schema, user_id):
    response = requests.get(url=base_url + f"posts?userId={user_id}")
    assert response.status_code == 200
    json = response.json()
    assert len(json) > 0
    for resource in json:
        validate(instance=resource, schema=schema)
        assert resource["userId"] == user_id


@pytest.mark.parametrize("user_id, title, body", [
    (11, "title_11", "body_11"),
    (12, "title_12", "body_12"),
    (13, "title_13", "body_13")
])
def test_create_resource(base_url, user_id, title, body):
    resource = {
        "userId": user_id,
        "title": title,
        "body": body
    }
    response = requests.post(url=base_url + f"posts", json=resource)
    assert response.status_code == 201
    json = response.json()
    assert len(json) > 0
    assert resource == {key: json[key] for key in ("userId", "title", "body")}


@pytest.mark.parametrize("resource_id, user_id, title, body", [
    (11, 1, "title_11_updated", "body_11_updated"),
    (12, 2, "title_12_updated", "body_12_updated"),
    (13, 3, "title_13_updated", "body_13_updated")
])
def test_update_resource(base_url, resource_id, user_id, title, body):
    resource = {
        "userId": user_id,
        "title": title,
        "body": body
    }
    response = requests.put(url=base_url + f"posts/{resource_id}", json=resource)
    assert response.status_code == 200
    json = response.json()
    assert len(json) > 0
    resource.update({"id": resource_id})
    assert resource == json


@pytest.mark.parametrize("resource_id, title, body", [
    (11, "title_11_patched", "body_11_patched"),
    (12, "title_12_patched", "body_12_patched"),
    (13, "title_13_patched", "body_13_patched")
])
def test_patch_resource(base_url, resource_id, title, body):
    response = requests.get(url=base_url + f"posts/{resource_id}")
    assert response.status_code == 200
    json = response.json()
    assert len(json) > 0
    user_id = json["userId"]
    resource_patch = {
        "title": title,
        "body": body
    }
    response = requests.patch(url=base_url + f"posts/{resource_id}", json=resource_patch)
    assert response.status_code == 200
    json = response.json()
    assert len(json) > 0
    resource_patch.update({"id": resource_id, "userId": user_id})
    assert resource_patch == json


@pytest.mark.parametrize("user_id", [11, 12, 13])
def test_delete_resource(base_url, user_id):
    response = requests.delete(url=base_url + f"posts/{user_id}")
    assert response.status_code == 200
