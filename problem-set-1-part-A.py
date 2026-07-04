total_cost = float(input("What is the cost of your dream house? $"))
portion_down_payment = 0.25*total_cost
annual_salary = float(input("What is your annual salary ? $"))
portion_saved = float(input("What amount of your salary would u like to save(in decimal)? "))
monthly_salary = annual_salary/12
r = 0.04
current_savings = 0.00
months = 0
while current_savings < portion_down_payment:
    current_savings +=  (current_savings*(r/12)) + monthly_salary*portion_saved
    months += 1

print("number of months = ", months)
    