def cal_str():
    string= input('Enter a sentence with upper and lower case: ') #user enters the string
    sum1 = 0 
    sum2 = 0
    for i in string:
        if i.isupper():  #checks if a letter is upper case
            sum1 += 1
        elif i.islower(): #checks if a letter is lower case
            sum2 += 1
            
    return (sum1,sum2) #returns the no of upper and lower case letters
        
count= cal_str() 
#print(count)
print('Number of Upper case letters: ',count[0])
print('Number of Lower case letters: ',count[1])