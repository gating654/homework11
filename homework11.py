class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        numberOfFloors = floors
        return numberOfFloors


h1 = House()
print(h1.setNewNumberOfFloors(3))
