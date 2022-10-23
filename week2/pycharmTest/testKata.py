# userInput = int(input('Please input a number 1-5: '))


def sendDataTest(userInput):
    if userInput == 1:
        return '1'
    elif userInput == 2:
        return '2'
    elif userInput == 3:
        return 'Pepsi'
    elif userInput == 4:
        return 'FOUR!!'
    elif userInput == 5:
        return 'Coke'
    else:
        return 'error'


# sendDataTest(userInput)

# moreInput = int(input('Please enter a number divisible by 3, 5 or both: '))


def moreDataTest(moreInput):
    if moreInput % 3 == 0 and moreInput % 5 == 0:
        return 'PepsiCoke'
    elif moreInput % 5 == 0:
        return 'Coke'
    elif moreInput % 3 == 0:
        return 'Pepsi'
    else:
        return 'error'


# moreDataTest(moreInput)

def test_getOne():
    assert sendDataTest(1) == "1"

def test_getTwo():
    assert sendDataTest(2) == "2"

def test_getPepsi():
    assert sendDataTest(3) == "Pepsi"

def test_getFour():
    assert sendDataTest(4) == "FOUR!!"

def test_getCoke():
    assert sendDataTest(5) == "Coke"




def test_try15():
    assert moreDataTest(15) == "PepsiCoke"

def test_try10():
    assert moreDataTest(10) == "Coke"

def test_try6():
    assert moreDataTest(6) == "Pepsi"