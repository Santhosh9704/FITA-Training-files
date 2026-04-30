#bike bheaviour

'''speed=120
wheels=2
mileage=50
capacity=130

def moveforward():
    print("Bike moving forward direction")

def backward():
    print("Bike moving backward direction")


speed_1=90
wheels_1=2
mileage_1=60
capacity_1=130

def moveforward():
    print("Bike moving forward direction")

def backward():
    print("Bike moving backward direction")
    
moveforward()
backward()'''


class Bike:
    
    speed=120
    wheels=2
    mileage=50
    capacity=130
    def moveforward(self):
        print("Bike moving forward direction")

    def backward(self):
        print("Bike moving backward direction")

splender=Bike()
print("Bike Wheels:",splender.wheels)
print("Splender speed:",splender.speed)

pluser=Bike()
pluser.speed=130
pluser.mileage=40
print("PLUSER SPEED:",pluser.speed)
print("PLUSER Mileage:",pluser.mileage)

NS=Bike()
NS.speed=200
NS.mileage=25

print(f"NS Mileage:{NS.moveforward()}")
print("NS Mileage:",NS.mileage,NS.speed)
print("NS speed:",NS.speed)
NS.moveforward()
print()
