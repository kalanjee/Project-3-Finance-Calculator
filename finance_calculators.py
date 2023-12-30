#This is a finance calculator to help users understand how much they are liable to pay.
#On selecting 'investment', the user can calculate the amount earned from simple or compound interest.
#On selecting 'bond', the user can understand how much they would repay each month if borrowing against a fixed asset.
#Used f strings as this makes editing the final copy easier.
#To make it easier to read, I have added line breaks between each line and rounded to 2 decimal places.

import math

print("\n""investment - to calculate the amount of interest you'll earn on your investment")
print("\n""bond - to calculate the amount you'll have to pay on a home loan""\n")

var = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if var == "investment":
    p = int(input("\n""How much money are you depositing (USD)? "))
    r = (float(input("\n""Please enter the interest rate: "))) / 100
    t = int(input("\n""How many years would you like to invest for? "))
    interest = input("\n""Do you want simple or compound interest? Reply 'simple' or 'compound': ")
    if interest == "simple":
        amt1 = round((p * (1 + r * t)),2)
        output1 = f"You earn a total of ${amt1 - p} in interest at the end of {t} years. The total amount of your investment will be {amt1}." 
        print("\n"+ output1)
    if interest == "compound":
        amt2 = round((p * math.pow((1 + r),t)),2)
        output2 = f"You will earn a total of ${amt2 - p} in interest at the end of {t} years. The total amount of your investment will be {amt2}."
        print("\n"+ output2)
elif var == "bond":  
    pv = int(input("\n""Enter the present value of the house (USD): "))
    annual_rate = float(input("\n""Enter the interest rate: ")) / 100
    i = annual_rate / 12                                     #Dividing the annual interest rate by 12 to get the monthly rate
    n = int(float(input("\n""Enter the number of years: ")) * 12)
    repayment = round((i * pv)/(1-(1+i)**(-n)),2)
    output3 = f"You will have to repay ${repayment} every month for {n} months."
    print("\n"+ output3)
else:
    print("Incorrect selection. Refresh and try again.")    #As we have not learned how to loop yet.
    