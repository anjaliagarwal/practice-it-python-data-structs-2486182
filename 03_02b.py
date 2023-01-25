from collections import namedtuple
from csv import reader

def main():
    #add code here
    #read data/Customer.csv
    with open("data/Customer.csv", "r") as f:
      read = reader(f)
      person = namedtuple("Person",next(read))
      for line in read:
         Person = person(*line)
         print(Person.CustomerID, Person.FirstName, Person.LastName)
    #Create workable objects with each line
    return

if __name__ == "__main__":
    main()