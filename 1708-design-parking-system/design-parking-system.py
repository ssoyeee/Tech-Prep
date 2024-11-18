class ParkingSystem:
    

    def __init__(self, big: int, medium: int, small: int):
        # Initialize the parking slots for big, medium, and small cars
        # Spaces are stored as a list for easy access: [big, medium, small]
        self.spaces = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        # Check if there is an available slot for the given carType
        # carType corresponds to:
        #   1 -> Big car
        #   2 -> Medium car
        #   3 -> Small car
        if self.spaces[carType - 1] > 0: # If there are slots available
            self.spaces[carType - 1] -= 1 # Park the car (decrease the slot count)
            return True # Return True to indicate success
        return False # Return False if no slots are available

# Test Case
# create parking lot: big = 1, medium = 1, small = 0
# parking = ParkingSystem(1, 1, 0)

#print(parking.addCar(1))  # True (Big car가 주차됨, big slot 1 -> 0)
#print(parking.addCar(2))  # True (Medium car가 주차됨, medium slot 1 -> 0)
#print(parking.addCar(3))  # False (Small slot이 없음)
#print(parking.addCar(1))  # False (Big slot이 이미 꽉 찼음)

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)