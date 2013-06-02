# Coded By Kronos
# Last Updated 6/1/2013
# Version 1.0

import random
import os
import itertools

# What the password will be used for
s = raw_input("What will the password be used for:")

# The username/email the password will go with
a = raw_input("What username will you use this with:")

# The Length of the password
q = raw_input("How long would you like the password to be:")

# The characters to choose from
stuff = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         "A","B",'C',"D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V",'W',"X","Y","Z",
         '1','2','3','4','5','6','7','8','9','0']

# Randomly choose a character
m = ''.join(random.choice(stuff) for x in xrange(int(q)))
print s
print a
print m


# Creates the file
path = "C:\Documents"
if not os.path.exists(path):
    os.makedirs(path)

filename = "passwords.txt"

# Write the password to a file
with open(os.path.join(path, filename),'a+') as passwords:
    passwords.write(s + ":\n")
    passwords.write(a + " = Username\n")
    passwords.write(m + " = Password\n")
                    
    print ("Passwords are located at:" + str(os.path.join(path, filename)))
   


