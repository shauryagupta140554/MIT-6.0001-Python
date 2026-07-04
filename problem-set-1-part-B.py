total_cost =float(input("What is the cost of your dream home? $"))
portion_down_payment = 0.25
portion_saved = float(input("What percentage of salary would you like to safe monthly ?(in decimal)"))
annual_salary = float(input("What is your annual salary ? $"))
semi_annual_raise = float(input("What is your semi annual raise?(in decimal) "))
current_Savings = 0
r = 0.04
down_payment = portion_down_payment*total_cost
monthly_Salary = annual_salary/12
months = 0
while current_Savings < down_payment:
    current_Savings += (current_Savings*(r/12)) + monthly_Salary*portion_saved
    months +=1
    if months % 6 ==0:
        annual_salary = annual_salary*(1+semi_annual_raise)
        monthly_Salary = annual_salary/12
print("number of months", months)    
                                
