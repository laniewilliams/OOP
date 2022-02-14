#from re import T
import CellPhoneClass as cp

def main():
    man = input("What is manufacturer of your cellphone? ")

    mod = input("What is model of your cellphone? ")

    pri = float(input("What is the retail price of your cellphone? "))

    car = cp.CellPhone(man,mod,pri)

    car.set_manufact(man)
    car.set_model(mod)
    car.set_retail_price(pri)

    print("Manufacturer: ",car.get_manufact())
    print("Model: ",car.get_model())
    print("Retail Price: $",format(car.get_retail_price(),'.2f'))

main()