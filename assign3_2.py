string= str(input('Enter a string: '))

#print(string) print the string from user

def rev(stng):   #defining a function for the reverse of input strings
    a=stng[::-1]
    return a   
print('Reverse order of string:', rev(string))
