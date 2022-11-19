import pytest

from main import Data

@pytest.fixture
def data():
    data = Data()
    return data.strList(2)


def testCanAddString(data):
    assert Data.strList(2)