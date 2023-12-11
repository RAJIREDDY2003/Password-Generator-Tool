import random
import string

def password(length_string):
    ch=string.ascii_letters+string.digits+string.punctuation
    output="".join(random.choice(ch) for i in range(length_string))
    return output
length=int(input("enter the length of the password:"))
number=int(input("number of passwords to generate:"))
for i in range(number):
    print(password(length))    

