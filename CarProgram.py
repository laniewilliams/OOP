import CarClass as c 

my_car = c.Car(2016,'Toyota',0)

for i in range(5):
    my_car.accelerate()
    print('Current Speed: ',my_car.get_speed(),"mph")

for i in range(5):
    my_car.brake()
    print('Current Speed: ',my_car.get_speed(),'mph')

