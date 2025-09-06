#Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))
current_year = 2025
age = current_year - year_of_birth
print("Hello", name + "!", "You are", age, "years old.")
#Extract car names from the following text:
txt = 'LMaasleitbtui'
a=txt[0::2]
b=txt[1::2]
' '.join(['Car names:',a,b])
#Extract car names from the following text:
txt = 'MsaatmiazD'
a=txt[0::2]
b=txt[-1::-2]
' '.join(['Car names:',a,b])
#Extract the residence area from the following text:
txt = "I'am John. I am from London"
a=txt[17::]
' '.join(['Residence area:',a])
#Write a Python program that takes a user input string and prints it in reverse order.
user_input = input("Enter a string: ")
reversed_string = user_input[::-1]
print("Reversed string:", reversed_string)
#Write a Python program that counts the number of vowels in a given string.
input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in input_string:
    if char in vowels:
        count += 1
print("Number of vowels:", count)
#Write a Python program that takes a list of numbers as input and prints the maximum value.
numbers = [3, 5, 2, 8, 1]
max_value = max(numbers)
print("Maximum value:", max_value)
#Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
word = input("Enter a word: ")
if word == word[::-1]:
    print(word, "is a palindrome.")
#Write a Python program that extracts and prints the domain from an email address provided by the user.
email = input("Enter your email address: ")
domain = email.split('@')[-1]
print("Domain:", domain)
#Write a Python program to generate a random password containing letters, digits, and special characters.
import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password_length = int(input("Enter the desired password length: "))
print("Generated password:", generate_random_password(password_length))