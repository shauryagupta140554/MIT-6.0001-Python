total_cost = 1000000
portion_down_payment = 0.25
starting_salary = float(input("What is your starting salary ? $"))
semi_annual_raise = 0.07
r = 0.04
down_payment = total_cost*portion_down_payment
epsilon = 100
low = 0
high = 10000
steps = 0
guess_found = False
while low <= high:
    steps += 1
    guess = (low+high)//2
    portion_saved = guess/10000
    current_Savings = 0
    annual_salary=starting_salary 
    monthly_salary = annual_salary/12
    for months in range(1,37):
        current_Savings += (current_Savings*(r/12)) + monthly_salary*portion_saved
        if months % 6 == 0:
            annual_salary = annual_salary*(1+semi_annual_raise)
            monthly_salary = annual_salary/12
    if abs(current_Savings-down_payment)<=epsilon:
        guess_found = True
        break
    elif current_Savings<down_payment:
        low = guess + 1
    else:
        high = guess -1
if guess_found:
    print("Best Saving Rate:",round(portion_saved,4))
    print("steps in bisection search:",steps)            
else:
    print("It is not possible to pay the down payment in three years.")             
                                
