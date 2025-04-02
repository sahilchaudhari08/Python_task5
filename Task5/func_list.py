# func list 1
# find largest number from list

def find_largest(numbers):
    return max(numbers)

num = [52,25,45,46,54,61,35,78,66,42,]
find = find_largest(num)
print(f'lagest numbers is = {find}')

print('_______________________________')

# func list 2
def reverceList(lst):
    return lst[::-1]

values = [1,2,3,4,5,6,7,8,9]
rvers = reverceList(values)
print(rvers)

