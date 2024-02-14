import random
winning_number = int(input("Please enter a number between  1 and  20: "))
random_number = random.randint(1,  20)
while True:
   
    if winning_number == random_number:
        print("YOU JUST WON A TO MALDIVES")
        break
    else:
        print("SORRY! TRY AGAIN LATER😞")
        winning_number = int(input("Please enter a number between  1 and  20: "))
