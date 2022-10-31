import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--base_url", action="store", default="https://api.tumblr.com", help="url not corrected"
    )


@pytest.fixture
def add_url(request):
    url = request.config.getoption("--base_url")
    yield {"url": url}
