import pytest

from main import Data

@pytest.fixture

def data():
    data = Data()
    return data


def testCanAddString():
    assert Data.strList(2)