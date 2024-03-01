import random 

# Create strings that contain all type of letters used for pws
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = uppercase_letters.lower()
digits = '0123456789'
symbols = '()[]{},;.:-$#"&%!\|/?!+º~'

# Do we want the password to have uppercase letters? Yes | True
# Do we want the password to have lowercase letters? Yes | True
# Do we want the password to have numbers? No | False
# Do we want the password to have Symbols? Yes | True
upper, lower, nums, syms = True, True, False, True

# Create a string will all the things we are going to use
all_chars = ''

if upper: 
    all_chars += uppercase_letters
if lower:
    all_chars += lowercase_letters
if nums:
    all_chars += digits
if syms:
    all_chars += symbols

length = int(input('Enter the length you want the password to have.\n')) # Size of pw
amount = int(input('Enter the amount of characters you want the password to have.\n')) # The amount of chars that the pw will have

for i in range(amount): # Go to all the chars and randomize a password based on the length inserted by the user 
    password = ''.join(random.sample(all_chars, length))
    print(password)