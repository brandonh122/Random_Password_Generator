#Ask them to pick a pass len
#Ask them to add or include all special characters
#Possibly have the user give us a work and have a secure pass be generated

from tkinter import *
from tkinter import messagebox
import string
import random

pl = 6
s_chars = list(string.punctuation)
l_letters = list(string.ascii_lowercase)
u_letters = list(string.ascii_uppercase)
num = list(string.digits)

random.shuffle(s_chars)
random.shuffle(l_letters)
random.shuffle(u_letters)
random.shuffle(num)

password = []

part1 = round(pl * (60/100))
part2 = round(pl * (35/100))

for x in range(part1):
 
    password.append(l_letters[x])
    password.append(u_letters[x])
 
for x in range(part2):
 
    password.append(s_chars[x])
    password.append(num[x])


print(f"List of random Characters that will be used to create your password:\n",password)
random.shuffle(password)

f_pass = "".join(password)
print("Your randomly generated password is:\n",f_pass)