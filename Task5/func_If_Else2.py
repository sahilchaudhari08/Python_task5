# Function 2
# Check if age are Adult or Teenage

def People(age):
    if age >= 19:
        return 'Adult'
    else:
        return 'Teenage'

details = [('sunny', 18), ('pranay', 20), ('sarthak', 21), ('anshu', 20), ('Pankaj', 17)]

for name, age in details:
    print(f'name= {name}, age= {age}')
    category = People(age)
    print(f'Category {category}')

