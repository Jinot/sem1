#This program uses a loop to dosplay a table showing the
#numbers 1 through 10 and their squares

#print the table headings
print('Number\tSquare')
print('--------------')

#Print the numbers 1 through 10 and their squares
for number in range(1, 11):
    square=number**2
    print(f'{number}\t{square}')
    
