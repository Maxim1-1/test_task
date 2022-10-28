import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--base_url", action="store", default="new_url", help="my option: type1 or type2"
    )


@pytest.fixture
def add_url(request):
    url = request.config.getoption("--base_url")
    yield {"url": url}
