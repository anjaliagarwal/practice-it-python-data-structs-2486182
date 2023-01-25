from collections import namedtuple

def can_take_order(driver, num_package):
  return driver.car_capacity >= num_package

def main():
    #add code here
    #create a driver with a name, car type, and car capacity
    Driver = namedtuple("driver",["name","car_type","car_capacity"])
    #an example you can use to practice: "Iris", "Toyota Prius", 7
    iris = Driver("Iris","Prius",7)
    mickie = Driver("Mickie","Tuscon",15)
    witty = Driver("Witty","Honda",25)
    #check if they can take a certain order, given their car's capacity.

    print(can_take_order(witty,20))
    return

if __name__ == "__main__":
    main()