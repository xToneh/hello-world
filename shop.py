#shop.py
#
#Antonio Perez
#October 20, 2020
#
can_pay = "Thank you for shopping."
def check_money(total_cost, customer_money):
    if total_cost > customer_money:
        print("False")
    else total_cost < customer_money:
        print("True")


#This should print False
can_pay = check_money(107, 49)
print(can_pay)

#This should print True
can_pay = check_money(6, 88)
print(can_pay)
