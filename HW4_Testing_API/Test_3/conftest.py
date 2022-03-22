import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://jsonplaceholder.typicode.com/",
        help="This is request url"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def schema():
    return {
        "type": "object",
        "properties": {
            "userId": {"type": "number"},
            "id": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["userId", "id", "title", "body"]
    }
