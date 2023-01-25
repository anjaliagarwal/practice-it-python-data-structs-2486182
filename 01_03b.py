from collections import Counter

def main():
    #Add code here
    inventory = Counter(STA001=10, SAL002=20, ENT004=13)
    #sell 5 starters, 3 salads, and 3 entrees
    #make 9 more starters and 1 more entree
    sales_inventory = Counter(STA001=5, SAL002=3, ENT004=3)
    remaining = inventory - sales_inventory
    add_inventory = {"STA001" : 9, "ENT004" : 1}
    remaining.update(add_inventory)
    print(remaining)

if __name__ == "__main__":
    main()