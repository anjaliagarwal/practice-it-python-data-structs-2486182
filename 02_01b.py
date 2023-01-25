from collections import deque
def main():
    #add code here
    create_db = deque(maxlen=5)
    create_db.append("Starter01")
    orderlist = ["MainCourse","Chinese","Beverages","Italian"]
    create_db.extend(orderlist)
    create_db.append("Deseart")
    create_db.appendleft("JalPaan")
    print(create_db)
    return create_db

if __name__ == "__main__":
    main()