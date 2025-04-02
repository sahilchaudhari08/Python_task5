# Function 3
# Check if Food Items are Vegetarian or Non-Vegetarian

def foodItems(category):
    if category == 'Vegetarian':
        return 'veg'
    else:
        return 'non veg'
    
menu = [('Paneer Tikka', 'Vegetarian'),('Chicken Biryani', 'Non-Vegetarian'),('Dal Makhani', 'Vegetarian'),('Fish Curry', 'Non-Vegetarian'),('Aloo Paratha', 'Vegetarian')]


for food, category in menu:
    print('Food =', food)
    categorys = foodItems(category)
    print('category =', categorys)
    print('____________________________')
