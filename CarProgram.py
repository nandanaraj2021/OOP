import CarClass as cc

year_model = 2010
make = 'Nissan'

nissan = cc.Car(year_model, make)

num = 5

for x in num:
    nissan.accelerate()
    print("Car's speed is:", nissan.get_speed())

for x in num:
    nissan.brake()
    print("Car's speed is:", nissan.get_speed())