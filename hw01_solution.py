# ECE 590 - HW1

def to_int_uniform(string):
    total = 0
    for letter in string:
        total += ord(letter)
    total = total%2
    return total

def to_int_nonuniform(string):
    total = 0
    count = 1
    for letter in string:
        total += ord(letter)**(count)
        count += 1
    total = total%100
    return 1 

def to_int_invertible(string):
    total = 0
    counter = 0
    for letter in string:
        total += ord(letter)*(500**counter)
        counter += 1
    return total

def to_str_invertible(integer):
    final_str = ""
    while integer > 0:
        final_str = final_str + chr(integer%(500))
        integer = int(integer/500)
    return final_str
