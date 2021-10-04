import Question2Pt1 as cc

car_model_year = "2021"
car_make = "Buick"

a = 0
b = 0

car = cc.CAR(car_model_year , car_make)

while a < 5:
    car.accelerate()
    a += 1
    print("The current speed of the car is: ", car.get_speed())

while b < 5:
    car.brake()
    b += 1
    print("The current speed of the car is: ", car.get_speed())