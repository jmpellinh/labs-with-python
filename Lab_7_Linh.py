#question 1
def cal_list (num_list): #function
    total = 0 #start with 0 as the base for the total
    for i in num_list: #loop to take in the list, as long as the num is in the list, it will be add in the total
        total += i
    return total #make sure to return it, or it would be invalid
def main (): #testing the function
    real_num_list = [3,4,6,20] #hypotical list
    result = cal_list (real_num_list) #use the function
    print (result)
main ()
    

#question 2
name_var = ['Aqua', 'Ruby', 'Ai', 'Hoshino', 'Star'] #list
if 'Ruby' in name_var: #condition
    print ('Hello Ruby')
else: print ('No Ruby')

#question 3
def func_list (num_list):
    num_list [0], num_list [-1] = num_list [-1], num_list [0] #switching two index 0 and -1, first and last
    return num_list
def main (): #test using main function
    real_list = [23,65,19,90]
    func_list (real_list)
    print (real_list)
main ()

#question 4
def count_x (num_list,x): #two parameters: list & x
    count_num = 0 #start count with 0, out of loop
    for i in num_list: 
        if i == x: #condition, if the i equal the x that will be put in
            count_num += 1 #only then count it
    return count_num
def main (): #test the function
    x = 9
    num_list = [1,2,3,43,7,4,2,9,2,9,3,9,5,92,5]
    result = count_x (num_list,x)
    print (result)
main()
        
#question 5
def list_sq (num_list): 
    for i in range(len(num_list)): #for the i that in the range of the list
        num_list [i] = num_list [i] ** 2 #and based on the index of the number, we take that number to square it up, and replace them
    return num_list
def main ():
    num_list = [1,2,3,3,6,2,6,3,9]
    result = list_sq (num_list)
    print (result)
main ()
    
#question 6
num_list = [3,6,8,1,5,9,2,5,20,48,385,38,20,73,27,20,49]
for i in range (len(num_list)): #similar to question 5, we use index to help with this
    if num_list [i] == 20: #if the a number has index of i equal 20 (so testing all index)
        num_list [i] = 200 #replace that index with a new number, 200
print (num_list)

