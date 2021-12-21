import string 
import random
password = [] 
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

char_num = input('how many characters for the password?: ')
while True:
    try:
        char_num = int(char_num)
        if char_num<6:
            char_num = input('you need at least 6 char: ')
        else:
            break
    except:   
        char_num = input('please enter a valid answer: ')

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(char_num*(30/100))
part2 = round(char_num*(20/100))

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])
for i in range(part2):
    password.append(s3[i])
    password.append(s3[i])

random.shuffle(password)
password = ''.join(password)
print(f'the generated password is : {password}')
