import random 
import string
string.ascii_letters
"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

a,b,c = random.choice(string.ascii_letters),random.choice(string.ascii_letters),random.choice(string.ascii_letters)
x,y,z = random.randint(1,50),random.randint(1,50),random.randint(1,90)

randomPassword = a+str(x)+b+str(z-1)+str(y)+c+str(z)
print("Your random generated password of "+ str(len(randomPassword)) + " characters is: " + randomPassword)