import pytest

# Q2: Custom CLI option
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment name (dev / qa / prod)"
    )

@pytest.fixture
def env(request):
    return request.config.getoption("--env")
