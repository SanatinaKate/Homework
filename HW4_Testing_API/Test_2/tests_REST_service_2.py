import pytest
import requests


@pytest.mark.parametrize("query", ["Boston", "Chicago", "Denver", "Houston", "Portland"])
def test_autocomplete(base_url, query):
    response = requests.get(url=base_url + f"/autocomplete?query={query}")
    assert response.status_code == 200
    json = response.json()
    assert len(json) > 0
    query = query.lower()
    for brewery in json:
        assert list(brewery.keys()) == ["id", "name"]
        assert (query in brewery["id"].lower()) or (query in brewery["name"].lower())


@pytest.mark.parametrize("city", ["Boston", "Chicago", "Denver", "Houston", "Portland"])
def test_list_breweries_by_city(base_url, city):
    response = requests.get(url=base_url + f"?by_city={city}")
    assert response.status_code == 200
    json = response.json()
    assert len(json) > 0
    for brewery in json:
        assert city in brewery["city"]


@pytest.mark.parametrize("brewery_type", ["bar", "brewpub", "large", "micro", "nano", "regional"])
def test_list_breweries_by_type(base_url, brewery_type):
    response = requests.get(url=base_url + f"?by_type={brewery_type}")
    assert response.status_code == 200
    json = response.json()
    assert len(json) > 0
    for brewery in json:
        assert brewery["brewery_type"] == brewery_type


@pytest.mark.parametrize("page_size", [1, 5, 10, 25, 50])
def test_list_breweries_per_page(base_url, page_size):
    response = requests.get(url=base_url + f"?per_page={page_size}")
    assert response.status_code == 200
    json = response.json()
    assert len(json) == page_size


@pytest.mark.parametrize("page", range(1, 11))
@pytest.mark.parametrize("order", ["asc", "desc"])
def test_sort_by_id(base_url, page, order):
    response = requests.get(url=base_url + f"?page={page}&sort=id:{order}")
    assert response.status_code == 200
    json = response.json()
    assert len(json) > 0
    ids = [brewery["id"] for brewery in json]
    assert ids == sorted(ids, reverse=(order == "desc"))
