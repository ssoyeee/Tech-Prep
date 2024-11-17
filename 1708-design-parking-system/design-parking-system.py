class ParkingSystem:
    

    def __init__(self, big: int, medium: int, small: int):
        # big, medium, small ( fixed num of slots for each )
        # only park in its carType
        # carType 1, 2, 3
        self.spaces = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        # check whether there is space of carType or not
        # if no space, return False
        # else, return True
        if self.spaces[carType - 1] > 0:
            self.spaces[carType - 1] -= 1
            return True
        return False



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)