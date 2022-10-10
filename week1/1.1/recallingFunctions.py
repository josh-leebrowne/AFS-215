
class DataTypes():
    def __init__(self, newInt, newStr):
        self.value = []
        self.newInt = newInt
        self.newStr = newStr

    def addItem(self, newItem):
        self.value.append(newItem)
    
    def makeInt(newInt):
        outputInt = int(newInt)
        print(outputInt)

    def makeString(newStr):
        outputStr = str(newStr)
        print(outputStr)
    
    def makeDictionary(newInt, newStr):
        outputDict = dict(yourNumber = newInt, yourStr = newStr)
        print(outputDict)

    def makeTuple(newInt,newStr):
        outputTuple = (newInt, newStr)
        print(outputTuple)
        
# newInt = 0
# newStr = 'null'



# dataTypes = DataTypes(newInt,newStr)

# newInt = input('Please input a number: ')
# dataTypes.makeInt(newInt)
# newStr = input('Please input an animal: ')
# dataTypes.makeString(newStr)
newInt, newStr = input('Enter a number followed by an animal: ').split()
print("int: ", newInt)
print('str: ', newStr)


dataTypes = DataTypes(newInt, newStr)
dataTypes.makeInt(newInt)
dataTypes.makeString(newStr)






