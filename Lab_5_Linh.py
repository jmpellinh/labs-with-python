#question 1:
for r in range (1,6):
    for c in range (1,6):
        if (c <= r):
            print ('*', end = '')
        else:
            print ('', end = '')
    print ()

#question 2:
r = 1
while (r<= 5):
    c = 1
    while (c <= 5):
        if c <= r:
            print ('*', end = '')
        else:
            print ('', end = '')
        c += 1
    r += 1
    print ()

#question 3
r = 7
while r > 0:
    c=r
    while c > 0:
        print ("#", end = '')
        c -= 1
    print ()
    r -= 1

#question 4
c = 1
while r < 6:
    c = r
    while c >= 1:
        print(r, end ="")
        c -= 1
    print ()
    r += 1

#question 5
number = int(input("Put your number here: "))
while number >= 0 and number <= 100:
    if number % 2 != 0:
        print ("The number is not valid")
        number = int(input ("Please try again: "))
    else:
        print ("The number is valid")
        break 

#question 6
prime_num = int(input("Put your testing number here: "))
prime_con = True 
for i in range (2,prime_num):
    if prime_num % i == 0:
        prime_con = False
if prime_con == False:
    print ("This is not a prime number")
else:
    print ("This is a prime number")

#question 7
def times_ten ():
    num = float(input("Put your num: "))
    print (num * 10)
times_ten ()
                
#question 8
def main ():
    distance = float(input("Distance in Kilometers: "))
    snow_miles (distance)
def snow_miles (kilometers):
    miles = kilometers * 0.6214
    print (f'This is your miles: {miles}')

main ()
