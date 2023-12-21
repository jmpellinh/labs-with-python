#question 1
user_str = input("Put your sentence here: ")
total = 0
for var in user_str:
    if var.isspace() == True: #check to see if the variable itself is uppercase or not
        total += 1 #if yes, add
print (total)

#question 2
user_str = input("Put your sentence here: ")
total = 0
for var in user_str:
    if var.isdigit() == True: #same with question 1, testing digits
        total += 1
print (total)

#question 3
user_str = input("Put your sentence here: ")
total = 0
for var in user_str:
    if var.islower() == True: #testing lowercases, same with quest 1+2
        total += 1
print (total)

#question 4
user_name = input("Put your first, middle, and last name here: ")
list_name = user_name.split()#i split them into variables in a list, cuz they have spacing to split
first_name = list_name[0][0].upper() #using nested list calling their index as they're in a list
middle_name = list_name[1][0].upper()#middle name has the index 1 in the list, and its inital is the first one in the "middle list"
last_name = list_name[2][0].upper()
print (f'{first_name}. {middle_name}. {last_name}.')

#question 5
user_num = input("Put your number with no space here: ")
total = 0
for var in user_num:
    total += int(var) #change to integer as the num orginially is a string
print (f'Total is {total}')

#question 6
user_str = input("Put your sentence where no space and uppercase each initals: ")
empty_list = [user_str[0].upper()] #first, put the first initial to still be an upper case in the empty list first
for var in user_str [1:]: #start with index 1 instead 0 cuz we're passing the first initials
    if var.isupper() == True: #if it's upper case
        if empty_list[-1] != ' ': #and at the end doesn't have a space, we add it so new variable can be added in with a space
            empty_list.append (' ')
        empty_list += var.lower()#add them in the list with lowercase
    else: empty_list += var
print (*empty_list, sep = '')
    



    
