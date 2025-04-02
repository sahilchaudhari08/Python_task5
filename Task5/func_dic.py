# Opration with Dic 1

def student_info(student, name, age):
    print(name, age)
    return f'name {name}, age {age}'

students = {'Sarthak': {'age': 21}, 'vaibhav': {'age': 22}, 'Sahil': {'age': 24}}

info = (students)
print(info)

print('_____________________________________________________________________________')

# Opration with Dic 2

def add_contact(contacts, name, number):
    contacts[name] = number
    return contacts


contacts = {}  # Empty dictionary
# Add contacts
contacts = add_contact(contacts, "Anshu", "124578269")
contacts = add_contact(contacts, "sagar", "124523698")
contacts = add_contact(contacts, "vaibhav", "874512697")

print(contacts)


