



portion_down_payment = 0.25
current_savings = 0
investment_return = 0.04
months = 0

annual_salary = float(input("Enter your annual salary:​ "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:​ "))
total_cost = float(input("Enter the cost of your dream home:​​ "))
monthly_salary = annual_salary/12



while(current_savings <= total_cost * portion_down_payment):

    monthly_interest_of_savings = current_savings * (investment_return/12) # initially zero
    current_savings +=  monthly_interest_of_savings + (monthly_salary*portion_saved)    
    months +=1

print("Months: "+str(months))


