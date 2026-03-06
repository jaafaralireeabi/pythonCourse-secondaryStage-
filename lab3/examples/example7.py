keep_going = "y"

while keep_going == "y":
    sales = float(input("enter the amount of sales: "))
    comm_rate = float(input("enter the commission rate: "))
    commission = sales * comm_rate
    print("the commission is$",format(commission,".2f"))
    keep_going = input("do you have another commission (y for yes): ")