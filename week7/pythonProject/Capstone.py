class MyList():
    def __init__(self):
        self.items = []

    def addItems(self, item):
        self.items.append(item)
        return item

    def addMultipleItems(self, items):
        self.list.extend(items)
        return items

    def removeFirstItem(self):
        self.items.pop(0)
        return self.items

    def removeLastItem(self):
        return self.list.pop()

    def removeItem(self, item):
        self.items.remove(item)
        return self.items

