print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

#Bill amount
bill = 0

#Checking the size of the pizza
if size == "S":
    bill +=15
elif size == "M":
    bill +=20
else:
    bill+=25

#checking for pepperoni on pizza
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
else:
    bill = bill

#checking if the customer wants extra cheese
if extra_cheese == "Y":
    bill += 1
else:
    bill = bill

#printing using f-string
print(f"Your final bill is: ${bill}")
