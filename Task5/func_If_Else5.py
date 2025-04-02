# Function 5
# Check if Product ID Ends with an Odd or Even Number

def product(ID):

    id = int(ID[-1]) #define
    if id % 2 == 0:
        return 'An Even Id'
    else:
        return 'An Odd Id'
    

productIDs = ('prod101','prod202','prod303','prod404','prod505','prod606')    

for ID in productIDs:
    print('________________')
    print(f'ProductID = {ID}')
    EvenOdd = product(ID)
    print(f'ID is {EvenOdd}')

