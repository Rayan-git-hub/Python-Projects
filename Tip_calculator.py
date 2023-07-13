#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to tip calculator")

bill=float(input("what is the bill?"))
tip=int(input("what is the tip you want to give?"))
persons=int(input("How many friends are there?"))
amtper=float(bill*(1+tip*0.01)/persons)
print(round(amtper,2))