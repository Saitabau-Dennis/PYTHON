#Define function for each operation
def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
#prompt the user to select operator
print("Please select operator -\n"
     "1.Add\n" 
     "2.Subtract\n"
     "3.Multiply\n"
     "4.Divide\n")
#takes user selection as an input
select=int(input("Select operators form 1,2,3,4 :"))
#prompts the user to enter the number
number_1=int(input("Enter first number:"))
number_2=int(input("Enter second number:"))

if select==1:
   print(number_1, "+" ,number_2, "=" ,add(number_1,number_2))
elif select==2:
  print(number_1,"-" ,number_2, "="  , subtract(number_1,number_2))
elif select==3:
  print(number_1,"*" ,number_2, "="  , multiply(number_1,number_2))
elif select==4:
  print(number_1,"-" ,number_2, "/"  , divide(number_1,number_2))
else:
   print("Invalid Input")