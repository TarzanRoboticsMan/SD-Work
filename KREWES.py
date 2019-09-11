import random

KREWES = {
            'orpheus': ['Emily', 'Kevin', 'Vishwaa', 'Eric', 'ray', 'Jesse',
        'Tiffany', 'Amanda', 'Junhee', 'Jackie', 'Tyler', 'Emory',
        'Ivan', 'Elizabeth', 'Pratham', 'Shaw', 'Eric', 'Yaru',
        'Kelvin', 'Hong Wei', 'Michael', 'Kiran', 'Amanda', 'Joseph',
        'Tanzim', 'David', 'Yevgeniy'],
            'rex': ['William', 'Joseph', 'Calvin', 'Ethan', 'Moody', 'Mo',
        'Big Mo', 'Peihua', 'Saad', 'Benjamin', 'Justin', 'Alice', 'Hilary',
        'Ayham', 'Micheal', 'Matthew', 'Jionghao', 'Devin', 'David', 'Jacob',
        'Will', 'Hannah', 'Alex'],
            'endymion': []
        }

team = input("What team? ")
print(random.choice(KREWES[team]))
