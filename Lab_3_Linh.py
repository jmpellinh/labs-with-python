#question 1
var_speed = float(input ("Input your speed: "))
if var_speed >= 0 and var_speed <= 200:
    print ("The number is valid")
else:
    print ("The number is not valid")

#question 2
a = float(input ("put number here: "))
if a < 10:
          b = 0
          print (b)
else:
    b = 99
    print (b)

#question 3
number = float(input ("put your number here: "))
result = number % 4
if result == 0:
    print (f'The number is divisible by 4 and result: {(number/4):.0f}')
else:
    print ('The number is not divisible by 4')
    print ("The quotient:", int(number // 4))
    print ("Remainder:", int(number % 4))

#question 4
age = float(input ("What is your age: "))
if age <= 1:
    print ("infant")
elif age > 1 and age < 13:
    print ("child")
elif age <= 13 and age < 20:
    print ("teenager")
elif age >= 20:
    print ("adult")

#question 5
amount1 = float(input("Number 1: "))
amount2 = float(input("Number 2: "))
if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print ("Number 1 is larger: ",amount1)
    if amount2 > amount1:
        print ("Number 2 is larger: ",amount2)
else: print ("Not applicable")

    
