
# Function 1
# Check whether the train is an express train or a local train by its number.

def train(number):
    if len(number) != 5:
        print('Error - Train Number length should have only 5 Characters')
        return None
    if number.startswith('12'):
        print(f'Train {number} is Express train')
        return 'Express Train'
    else:
        print(f'Train {number} is local train')
        return 'Local Train'
    
print('-------------------------------------')
numbers = (input('enter a train number = '))
train_type = train(numbers)
print('-------------------------------------')


