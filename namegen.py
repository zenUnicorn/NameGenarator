import random, string

vowel = 'aeiou'
consonant = 'qwrtypsdfghjklzxcvbnm'
others = string.ascii_lowercase

input_1 = input("Enter your character - 'v','c','l':  ")
input_2 = input("Enter your character - 'v','c','l':  ")
input_3 = input("Enter your character - 'v','c','l':  ")
number_of_names = int(input("Enter the number of names you want to generate? "))

def generate():

    #first input
    if input_1 == 'v':
       letter1 = random.choice(vowel)
    elif input_1 == 'c':
        letter1 = random.choice(consonant)
    elif input_1 == 'l':
        letter1 = random.choice(others)
    else:
        letter1 = input_1
    
    #second input
    if input_2 == 'v':
       letter2 = random.choice(vowel)
    elif input_2 == 'c':
        letter2 = random.choice(consonant)
    elif input_2 == 'l':
        letter2 = random.choice(others)
    else:
        letter2 = input_2
    
    #third input
    if input_3 == 'v':
       letter3 = random.choice(vowel)
    elif input_3 == 'c':
        letter3 = random.choice(consonant)
    elif input_3 == 'l':
        letter3 = random.choice(others)
    else:
        letter3 = input_3
    
    return(letter1+letter2+letter3)

#looping to get n number of names
for i in range(number_of_names):
    print(generate())


    

