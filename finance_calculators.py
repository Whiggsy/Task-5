# simple financial calculator
import math
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

user_choice = input("Either enter 'investment' or 'bond' from the menu above.\n").lower()

# investment choice at initial input
if user_choice == "investment".lower():
    deposit = float(input("How much money are you depositing?\n"))
    interest_rate = float(input("what is the percentage rate as a figure only?\n"))
    interest_rate_float = float(interest_rate / 100)
    years = float(input("How many years do you want to invest for?\n"))
    interest_type = input("Will it be simple or compound interest?\n").lower()
    
# simple interest choice
    if interest_type == "simple":
        money_back = deposit * (1 + (interest_rate_float * years))
        print(f"Money returned to you would be {money_back}")
    
# compound interest choice
    elif interest_type == "compound":
         money_back_compound = deposit * math.pow((1 + interest_rate_float), years)
         money_back_compound_2dec = float("{:.2f}".format(money_back_compound))
         print(f"Money returned to you would be £{money_back_compound_2dec}")
    else:
        breakpoint

# bond choice at initial input
elif user_choice == "bond".lower():
     house_value = float(input("what is the house value?\n"))
     bond_interest = float(input("whats is the current interest rate?\n"))
     bond_interest_monthly = float((bond_interest /12) / 100)
     time_to_repay = float(input("How many months do you need to pay bond back?\n"))
     repayment = (bond_interest_monthly * house_value) / (1 - (1 + bond_interest_monthly)**(- time_to_repay))
     repayment_2decimals = float("{:.2f}".format(repayment))
     print(f"Monthly repyament would be £{repayment_2decimals}")

else:
    print("Wrong choice entered")