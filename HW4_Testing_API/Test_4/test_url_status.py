import requests


def test_url_status(base_url, status_code):
    gotten_status = None
    try:
        response = requests.get(url=base_url)
    except requests.ConnectionError:
        gotten_status = 404
    else:
        gotten_status = response.status_code
    finally:
        assert gotten_status == status_code
