list = input('Enter the numbers for the list: ').split()
#print(list)  print the input strings

list1= []
for i in list:
    list1.append(int(i))

print(list1) #print the input strings as integers in a list


def sum_list(num):
    sum = 0
    for i in num:
        sum += i    #adding the numbers in the list
    return sum
print('Sum of the numbers in the list: ',sum_list(list1))
