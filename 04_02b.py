from collections import namedtuple, defaultdict
from csv import reader
from pprint import pprint

def main():
    res = defaultdict(int)
    #add code here
    with open("data/OrderItems.csv", "r") as orderitem:
      read = reader(orderitem)
      item = namedtuple("item", next(read))

      for line in read:
        Items = item(*line)
        res[Items.ProductID] += int(Items.Quantity)
    
    pprint(dict(res))
    return

if __name__ == "__main__":
    main()