#question 1
dct = {'james': 'bro', 'kim': 'fhjbhs', 'yon': 'uhfsf'}
if 'james' in dct:
    print (dct['james'])
else: print ('There is no key')

#question 2
dct = {'james': 'bro', 'kim': 'fhjbhs', 'yon': 'uhfsf','jim': 'uehfuw'}
if 'jim' in dct:
    del dct['jim']
print (dct)

#question 3
user_set = set()
user_input = input('Put your numbers here: ')
numbers_str = user_input.split(',')
for num_str in numbers_str:
    user_set.add(int(num_str))
    
print("Unique numbers:", end=' ')
for num in user_set:
    print(num, end=' ')
