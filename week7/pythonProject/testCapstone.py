import pytest

from Capstone import MyList

@pytest.fixture()
def mylist():
    mylist = MyList()
    return mylist

def testCallMyList(mylist):
    mylist



def testCanAddItems(mylist):
    mylist.addItems('Corn')
    assert mylist.addItems('Corn') == 'Corn'

def testCanAddMultiple(mylist):
    items = ['Peppers', 2, True, {'dog food' : 'purina'}]
    assert mylist.addItems(items) == ['Peppers', 2, True, {'dog food': 'purina'}]

def testRemoveFirstItem(mylist):
    assert mylist.removeItem('corn')
    items = ['Peppers', 2, True, {'dog food' : 'purina'}]
    mylist.addMultipleItems(items)
    assert mylist.removeFirsItem() == [2, True, {'dog food': 'purina'}]

def testRemoveLastItem(mylist):
    items = ['Peppers', 2, True, {'dog food': 'purina'}]
    mylist.addMultipleItems(items)
    assert mylist.removeLastItem() == ['Peppers', 2, True]

def testRemoveItem(mylist):
    items = ['Peppers', 2, True, {'dog food': 'purina'}]
    mylist.addMultipleItems(items)
    assert mylist.removeItem('Peppers') == [2, True, {'dog food': 'purina'}]
