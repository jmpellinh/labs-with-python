#question 1
my_file = open ('my_name.txt','w')
my_file.write('Linh Dinh')
my_file.close()

#question 2
my_file = open ('my_name.txt','r')
name_file = my_file.read()
print (name_file)

#question 3
my_file = ('names.txt','r')
count_name = 0
for item in my_file:
    count_name += 1
print (count_name)

#question 4
import random #import randomint package
num_file = open ('numbers.txt', 'w') #open in writing mode
user_num = int(input('How many number: '))
for i in range (user_num): #then let the loop automaticly put the numbers in
    random_number = random.randint(1, 500)
    num_file.write(str(random_number))
num_file.close() #close it, or it will not work
num_file = open('numbers.txt', 'r') #then reopen in read mode
read_file = num_file.read()
print (read_file) #print the read!

#question 5
count = 0
sum_num = 0
num_file = open('numbers.txt', 'r')
for item in num_file:
    num = int(item.strip())
    count += 1
    sum_num += num
if count != 0:
    average = sum_num / count
    print("Count:", count)
    print("Sum:", sum_num)
    print("Average:", average)
