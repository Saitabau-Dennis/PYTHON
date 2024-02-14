# Ask the user for their salary and years of service
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

# Calculate the bonus based on years of service
if years_of_service >  10:
    bonus = salary *  0.10  #  10% bonus for more than  10 years
elif  6 <= years_of_service <=  10:
    bonus = salary *  0.08  #  8% bonus for  6 to  10 years
else:
    bonus = salary *  0.05  #  5% bonus for less than  6 years

# Calculate the total salary including bonus
total_salary = salary + bonus

# Print the total salary including bonus
print(f"Your total salary including bonus is: {total_salary}")
