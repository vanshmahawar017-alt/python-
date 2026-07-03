#+,*
#string operators
first_name='John'
last_name='Doe'
full_name=first_name+''+last_name
print(full_name)

#*
print('vansh' * 4)

#membership operators
text='this is a sentense '
print('t' in text)

#how to iterate over the string
#for(int i=0;i<=5;inti++){
  


#range(start,end,step)
#start=0
#end=5


for i  in range (0,6):
    print (i)

s='this is a sentense'
for i in range (0,len(s)):
    print(s[i])

for ch in s:
    print(ch)


#for capital
s='vansh'
print(s.upper())

s='vansh'
print(s.lower())#vansh


s='vansh mahawar'
print(s.capitalize())#Vansh mahawar

name='vansh'
#strip method
print(name.strip())

name='  rakshita  '
#strip method -> strip,lstrip,rstrip
print(name.lstrip())

print('c'.isalpha())#true, check alphabet or not


print('a3'.isalnum())#false, check alphabet or not


# Password Strength Analyzer
# Take a password as input. Using a single for loop, count:
# uppercase letters
# lowercase letters
# digits
# If all three are present, print "Strong Password"; otherwise print "Weak Password".

# password = input("Enter password: ")

# has_upper = False
# has_lower = False
# has_digit = False

# # Single for loop to check criteria
# for char in password:
#     if char.isupper():
#         has_upper = True
#     elif char.islower():
#         has_lower = True
#     elif char.isdigit():
#         has_digit = True

# if has_upper and has_lower and has_digit:
#     print("Strong Password")
# else:
#     print("Weak Password")





    # 1. Take a password as input from the user
password = input("Enter your password: ")

# Initialize counters for each category
upper_count = 0
lower_count = 0
digit_count = 0

# 2. Use a single for loop to check each character

for char in password:
  if char.isupper():
        has_upper = True
  elif char.islower():
       has_lower = True
  elif char.isdigit():
       has_digit = True




# 3. Check if all three conditions are met (counts are greater than 0)
if upper_count > 0 and lower_count > 0 and digit_count > 0:
    print("Strong Password")
else:
    print("Weak Password")





#3rd
# 1. Take a message as input from the user
message = input("Enter your secret message: ")

# 2. Swap the case of the string
swapped_message = message.swapcase()

# Initialize a counter for vowels
vowel_count = 0

# Define what characters count as vowels (both lowercase and uppercase)
vowels = "aeiouAEIOU"

# 3. Use a single for loop to check and count vowels
for char in swapped_message:
    if char in vowels:
        vowel_count += 1

# Print the final count
print("Total vowels in the decoded message:", vowel_count)





# Employee Code Validator
# Take an employee code as input.
# If it is alphanumeric, print it in uppercase.
# Otherwise print "Invalid Employee Code".
# After conversion, use a single for loop to count how many digits are present.



emp_code = input("Enter employee code: ")
if emp_code.isalnum():
    emp_code_upper = emp_code.upper()
    print("Employee Code in Uppercase:", emp_code_upper)

    # Initialize a counter for digits
    digit_count = 0

    # Use a single for loop to count digits
    for char in emp_code_upper:
        if char.isdigit():
            digit_count += 1

    print("Total digits in the employee code:", digit_count)




    s=input('enter any string')
    count_alph=0
    count_digit=0
    count_space=0
    for el in s:
        if ch.isalpha():
            count_alph+=1
        elif ch.isdigit():
            count_digit+=1
        elif ch.isspace():
            count_space+=1
    if count_sp += 1:
    print('strong string')
else:
    print('weak string')