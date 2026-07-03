# #+,*
# #string operators
# first_name='John'
# last_name='Doe'
# full_name=first_name+''+last_name
# print(full_name)



#how to iterate over the string
#for(int i=0;i<=5;inti++){
  


#range(start,end,step)
#start=0
#end=5


# for i  in range (0,6):
#     print (i)

# s='this is a sentense'
# for i in range (0,len(s)):
#     print(s[i])

# for ch in s:
#     print(ch)


# #for capital
# s='vansh'
# print(s.upper())

# s='vansh'
# print(s.lower())#vansh


# s='vansh mahawar'
# print(s.capitalize())#Vansh mahawar

# name='vansh'
# #strip method
# print(name.strip())

# name='  rakshita  '
# #strip method -> strip,lstrip,rstrip
# print(name.lstrip())

# print('c'.isalpha())#true, check alphabet or not


# print('a3'.isalnum())#false, check alphabet or not


# # Password Strength Analyzer
# # Take a password as input. Using a single for loop, count:
# # uppercase letters
# # lowercase letters
# # digits
# # If all three are present, print "Strong Password"; otherwise print "Weak Password".

# # password = input("Enter password: ")

# # has_upper = False
# # has_lower = False
# # has_digit = False

# # # Single for loop to check criteria
# # for char in password:
# #     if char.isupper():
# #         has_upper = True
# #     elif char.islower():
# #         has_lower = True
# #     elif char.isdigit():
# #         has_digit = True

# # if has_upper and has_lower and has_digit:
# #     print("Strong Password")
# # else:
# #     print("Weak Password")





#     # 1. Take a password as input from the user
# password = input("Enter your password: ")

# # Initialize counters for each category
# upper_count = 0
# lower_count = 0
# digit_count = 0

# # 2. Use a single for loop to check each character

# for char in password:
#   if char.isupper():
#         has_upper = True
#   elif char.islower():
#        has_lower = True
#   elif char.isdigit():
#        has_digit = True




# 3. Check if all three conditions are met (counts are greater than 0)
# if upper_count > 0 and lower_count > 0 and digit_count > 0:
#     print("Strong Password")
# else:
#     print("Weak Password")





# #3rd
# # 1. Take a message as input from the user
# message = input("Enter your secret message: ")

# # 2. Swap the case of the string
# swapped_message = message.swapcase()

# # Initialize a counter for vowels
# vowel_count = 0

# # Define what characters count as vowels (both lowercase and uppercase)
# vowels = "aeiouAEIOU"

# # 3. Use a single for loop to check and count vowels
# for char in swapped_message:
#     if char in vowels:
#         vowel_count += 1

# # Print the final count
# print("Total vowels in the decoded message:", vowel_count)





# Employee Code Validator
# Take an employee code as input.
# If it is alphanumeric, print it in uppercase.
# Otherwise print "Invalid Employee Code".
# After conversion, use a single for loop to count how many digits are present.



# emp_code = input("Enter employee code: ")
# if emp_code.isalnum():
#     emp_code_upper = emp_code.upper()
#     print("Employee Code in Uppercase:", emp_code_upper)

#     # Initialize a counter for digits
#     digit_count = 0

#     # Use a single for loop to count digits
#     for char in emp_code_upper:
#         if char.isdigit():
#             digit_count += 1

#     print("Total digits in the employee code:", digit_count)




# s=input('enter any string')
# count_alph=0
# count_digit=0
# count_sp=0
# for el in s:
#     if ch.isalpha():
#         count_alph+=1
#     elif ch.isdigit():
#         count_digit+=1
#     elif ch.isspace():
#         count_space+=1
# if count_sp == 1:
#     print('strong string')
# else:
#     print('weak string')





s= 'apple'
rev=''
for i in range (1,len(s)+1):
    rev+=s[-i]
    print(rev)



s = 'apple'
rev = ''
for i in range(1, len(s) + 1):
     rev += s[-i]

print(rev) 

rev=''
for ch in s:
    rev=ch+rev
print(rev)



s = 'appleApple'

vow = 0
cons = 0

for char in s.lower():
    if char.isalpha():
        if char in 'aeiouAEIOU':
            vow += 1
        else:
            cons += 1

print(f"Vowels: {vow}, Consonants: {cons}")



name = "Vansh"
age = "20"
sent=f"my name is {name} . my age is {age}."
print(sent)


sent1="my name is {1} . my age is {2}.".format(name,age)
print(sent1)


text = "DataScienceWithPython"
# Character positions for reference:
#  D  a  t  a  S  c  i  e  n  c  e  W  i  t  h  P  y  t  h  o  n
#  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
#-21-20-19-18-17-16-15-14-13-12-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1




text = "DataScienceWithPython"

# – Positive Indexing
print(text[0:4])  # Output: Data
print(text[4:11])  # Output: Science
print(text[11:15])  # Output: With
print(text[15:21])  # Output: Python
print(text[4:15])  # Output: ScienceWith
print(text[:10])  # Output: DataScienc
print(text[5:16])  # Output: cienceWithP
print(text[4:])  # Output: ScienceWithPython
print(text[:15])  # Output: DataScienceWith
print(text[:])  # Output: DataScienceWithPython


text = "DataScienceWithPython"
# Character positions for reference:
#  D  a  t  a  S  c  i  e  n  c  e  W  i  t  h  P  y  t  h  o  n
#  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
#-21-20-19-18-17-16-15-14-13-12-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# Negative Indexing
print(text[-6:])  # Output: Python
print(text[-10:-6])  # Output: With
print(text[-17:-10])  # Output: Science
print(text[-5:])  # Output: ython
print(text[-10:])  # Output: WithPython
print(text[:-7])  # Output: DataScienceWithP
print(text[-11:])  # Output: nceWithPython
print(text[-1])  # Output: n
print(text[-2])  # Output: o
print(text[-21:])  # Output: DataScienceWithPython





# – Step Slicing
print(text[::2])  # Output: DtScenWiPto
print(text[::3])  # Output: DasenPh
print(text[1::2])  # Output: aaienChyhn
print(text[::4])  # Output: Dceit
print(text[::-1])  # Output: nohtyPhtiWecneicSataD
print(text[20:14:-1])  # Output: nohtyP
print(text[10:3:-1])  # Output: ecneicS
print(text[::-2])  # Output: nhyhtiencat
print(text[::-3])  # Output: ntPienD
print(text[::-2])  # Output: nhyhtiencat



#Mixed positive and negative indexing
print(text[4:-10]) #Q31
print(text[-10:21]) #Q32
print(text[-17:15]) #Q33
print(text[12:-5]) #Q34
print(text[4:-1]) #Q35
print(text[1:-1]) #Q36
print(text[5:-6]) #Q37
print(text[5:-3]) #Q38
print(text[14:10:-1]) #Q39
#Q40
print(text[:4]) #1
print(text[4:11]) #2
print(text[15:]) #3
print(text[:-7:-1]) #4
print(text[:11]) #5
print(text[11:]) #6
print(text[:4]+text[11:15]) #7
print(text[::2]) #8
print(text[::-2]) #9
print(text[2:-2]) #10



# // #initialise
# // s = 'Rakshita'
# // print(type(s))

# // #How to access the characters from the string
# // #sequence of characters
# // s = 'vansh'
# // print(s[0])
# // print(s[1])
# // print(s[2])
# // print(s[3])
# // print(s[4])/

# for the direct string count
s = 'pineapple'
print(s[len(s) - 1])

print(s[-1]) 


s='pineapple'
#slicing
print(s[0:4]) #pine
#string slicing:it is the process of extracting a portion of a string by specifying the start and end indices. The syntax for slicing is s[start:end], where 'start' is the index of the first character to include, and 'end' is the index of the first character to exclude.
#substring: A substring is a contiguous sequence of characters within a string. It can be obtained through slicing or other string manipulation methods. For example, in the string "pineapple", "pine" and "apple" are substrings.
#starting index of the particular substracting
#and endng index of the substracting
#syntax s='vikash'
# s[start_idn : end_idn]/


s='apple'
print(s[:4])

s='pineapple'
print(s[0::2])


s='pineapple'
print(s[-7:-9])

s='india'
print(s[-1:-4:-1])


