def isPhoneNumber(text):                # we have defined function
    if len(text) != 12:                 #here in if condition used len() function and finding the length of text to 12
        return False                    #if about condition is satisfied then return false
    for i in range(0, 3):               #for loop till 3 which means 4th place in string and checking with isdecimal() function
        if not text[i].isdecimal():
            return False                
        if text[3] != '-':
            return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
        if text[7] != '-':
            return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

#this program is brief about every letter in the string checking whether its a decimal and checking 3rd and 7th position of the string is -

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))