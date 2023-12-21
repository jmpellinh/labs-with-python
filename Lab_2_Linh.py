#question 1
a = 8
b = a + 2
print (b)
a = b * 4
print (a)
b = a/3.14
print (b)
a = b - 8
print (a)

#question 2
down_payment = 190230
total = 502935
due = total - down_payment
print ("Amount due: ", due)

#question 3
number = 1234567.456
print (f'{number:,.1f}')

#question 4
speed = 70
time = 6
print (f'Distance when 6 hrs is {speed * time}')
time = 10
distance = speed * time
print (f'Distance when 10 hrs is {speed * time}')
time = 15
distance = speed * time
print (f'Distance when 15 hrs is {speed * time}')

#question 5
miles_driven = float(input("How many miles have you drived?: "))
gas_gallons = float(input("How many gas gallons have you used?: "))
MPG = miles_driven / gas_gallons
print ("Total MPG: ",MPG)
