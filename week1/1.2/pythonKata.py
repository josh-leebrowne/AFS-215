userInput = int(input('Please input a number 1-5: '))

def sendData(userInput):
    if userInput == 1:
        print('1')
    elif userInput == 2:
        print('2')
    elif userInput == 3:
        print('Pepsi')
    elif userInput == 4:
        print('FOUR!!')
    elif userInput == 5:
        print('Coke')
    else: print('error')

sendData(userInput)

moreInput = int(input('Please enter a 6, 10, or 15: '))

def moreData(moreInput):
    if moreInput == 6:
        print('Pepsi')
    elif moreInput == 10:
        print('Coke')
    elif moreInput == 15:
        print('PepsiCoke')
    else: print('error')

moreData(moreInput)