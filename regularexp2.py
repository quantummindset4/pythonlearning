import re; #importing regular experessions

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #compile() function with regex pattern
mo = phoneNumRegex.search('My number is 415-555-4242.') #search() function with phonenumregex instance
print('Phone number found: ' + mo.group()) #The group() method of the match object returns the matched text.

