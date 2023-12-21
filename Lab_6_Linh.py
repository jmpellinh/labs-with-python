#question 1
def max(num1,num2): #num1,num2 will be the parameters in this case
    if num1 > num2:
        return num1 #return num1 as the statement inside max()
    else: return num2
def main ():
    val1 = int(input("Put your number: "))
    val2 = int(input("Put your number: "))
    print (f'The largest number is: {max (val1,val2)}') #val1,val2 will be tested in max func, replacing num1 + num2
main ()

#question 2
def determine_grade (grade): #testing the grade
    if grade > 89 and grade < 101:
        grade = "A"
    elif grade > 79 and grade < 90:
        grade = "B"
    elif grade > 69 and grade < 80:
        grade = "C"
    elif grade > 59 and grade < 70:
        grade = "D"
    else: grade = "F"
    return grade #return the right result as statement inside determine_grade
def calc_average (cal_grade): #calculate the grade
    return cal_grade / 5 #and will take cal_grade from main then return the statement divided with 5 (because we're calculating 5 at the moment)
def main ():
    i = 0 #start loop
    cal_grade = 0 #to have a start to sum all grade 
    for i in range (0,5):
        all_grade = int(input ("What is your grade: "))
        print (all_grade)
        print(determine_grade (all_grade))#plugging variable in the determine function
        cal_grade += all_grade #sum
        i += 1
    print (f'Average score is: {calc_average (cal_grade)}')
main ()

#question 3
def is_prime (num):
    if num <= 1:
        return False
    for i in range (2,num): #condition from lab 5
        if num % i == 0:
            return False
    return True #return the right status
def main ():
    put_num = int(input("Put your number: "))
    if is_prime(put_num) == True: #if it's the right condition 
        print ("This is a prime number")
    else: print ("This is not a prime number")
main ()

#question 4
def is_prime (num): #still the same condition with lab5 and previous question, just different print
    if num <= 1:
        return False
    for i in range (2, num):
        if num % i == 0:
            return False
    return True
def main ():
    for num in range (2,100): #another loop
        if is_prime(num) == True:
            print (num)
main()

#question 5
import random #import the module

def math_num (): #generate both numbers then put statements in it
    num1 = random.randint (1,1000)
    num2 = random.randint (1,1000)
    return num1, num2 #statements will be put
def math_cal (num1, num2): #two variables we want to transfer from math_num
    correct_ans = num1 + num2 #sum
    print (f'Here are your numbers: {num1} {num2}')#print these out for students to see
    return correct_ans #return this back inside the math_cal or won't be able to determind the answer
def main ():
    var1, var2 = math_num () #vars inside the main that replace num1,num2
    correct_ans = math_cal(var1,var2) #same here but for math_cal function
    stu_ans = int(input(f"What the sum of these two? "))
    if stu_ans == correct_ans: #condition
        print (f'{correct_ans} is the right answer!')
    else: print (f'That is the wrong answer. Correct answer: {correct_ans}')
main ()
