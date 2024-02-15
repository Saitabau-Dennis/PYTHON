salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))
if years_of_service >  10:
    bonus = salary *  0.10 
elif  6 <= years_of_service <=  10:
    bonus = salary *  0.08  
else:
    bonus = salary *  0.05  


total_salary = salary + bonus

print(f"Your total salary including bonus is: {total_salary}")
