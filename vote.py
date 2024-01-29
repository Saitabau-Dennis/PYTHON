age =int(input("Enter your age:"))
country =input("Enter your country:")
if age>=18 and country.lower() in ["kenya","uganda","tanzania"]:
 print("You are eligible to vote")
else:
 print ("you are not eligible to vote")