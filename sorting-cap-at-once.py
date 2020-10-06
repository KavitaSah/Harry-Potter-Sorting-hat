import random

def sort_house():
    """Assigns random house to random person"""
    managers = ['Monica', 'Chandler', 'Phoebe', 'Rachael', 'Joey', 'Ross', 'Pikachu', 'Sheldon', 'Michael', 'Dwight', 'Toby', 'Holly']
    houses = ['gryffindor', 'hufflepuff', 'ravenclaw', 'slytherin']     
    for manager in managers:   
        print (f'{manager} goes to {random.choice(houses)} house.')
    
print (sort_house())
