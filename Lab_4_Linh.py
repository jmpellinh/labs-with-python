#question 1
answer = 'Yes'
while answer == 'Yes':
    first_num = float(input ('Put your first number: '))
    second_num = float(input ('Put your second number: '))
    sum_ans = first_num + second_num
    print (sum_ans)
    answer = input ("Do you want to repeat? Yes or No?: ")

#question 2
i = 0
total = 0
while i < 10:
    number = int(input('Input your number: '))
    total += number
    i = i+1
print (f' The total is: {total}')
    

#question 3
number = 20
while number >= 20 and number <= 30:
    if number == 30:
        print (number)
    else: print (number, end = ',') 
    number = number + 1

#question 4
for i in range(20,31):
    if i == 30:
        print (i)
    else: print (i, end = ',') 

#question 5
for i in range(10,91,5):
    if i == 90:
        print (i)
    else: print (i, end = ',') 

#question 6
number = 10
while number >= 10 and number <= 90:
    if number == 90:
        print (number)
    else: print (number, end = ',') 
    number = number + 5

#question 7
for i in range(80,49,-2):
    if i == 50:
        print (i)
    else: print (i, end = ',') 

#question 8
number = 80
while number >= 50 and number <= 80:
    if number == 50:
        print (number)
    else: print (number, end = ',') 
    number = number - 2

#question 9
total = 0
for i in range (100,1,-2):
    total += i
    if i == 2:
        print (i)
    else: print (i, end = ',')
print (f'The total is: {total}')

#question 10
total = 0
number = 102
while number >= 4:
    number = number - 2
    total += number
    if number == 2:
        print (number)
    else: print (number, end = ',')
print (f'The total is: {total}')

#question 11
i = 1
total = 0
while i < 6:
    number = int(input('Input number of bugs collected: '))
    total += number
    i = i+1
print (f'The total bugs has collected is: {total}')
