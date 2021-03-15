import pytest


@pytest.fixture(scope="function", autouse=True)
def resource_setup():
    print("Test start")
    yield
    print("Test finished")


@pytest.fixture(scope="class", autouse=True)
def resource_tear_down():
    yield
    print("All tests in TestFirst finished")