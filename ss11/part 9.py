person = {
    "name": "light",
    "age": 17,
    "strenght": 8,
    "defense": 10,
    "HP": 100,
    "backpack":["shield","bread loaf"],
    "gold":100,
    "level": 2,
}
print(person)
skill =[ {
    "skill": 1,
    "name": "Tackle",
    "Minimum level": 1,
    "damage" : 5,
    "Hit rate": 0.3
},
{
    "skill": 2,
    "name": "quick attack",
    "minimum level": 2,
    "damage": 3,
    "Hit rate": 0.5
},
{
    "skill": 3,
    "name": "strong kick",
    "minimum level": 4,
    "damage": 9,
    "Hit rate": 0.2
}
]
import random
c = random.randint(0,100)/100    
b = input('Skill ban muon dung: ')
if b == 1  and character['Level:'] >= skill['Skill 1:']['Minimum level']:
    if c > skill['Skill 1:']['Hit rate']:
        print('HIT!!','sat thuong ban gay ra la:',skill['Skill 1:']['damage']) 
    else:
        print('Skill cua ban da truot')     
elif b == 2  and character['Level:'] >= skill['Skill 2:']['Minimum level']:
    if c > skill['Skill 2:']['Hit rate']:
        print('HIT!!','sat thuong ban gay ra la:',skill['Skill 2:']['damage']) 
    else:
        print('Skill cua ban da truot')
elif b == 3 and character['Level:'] >= skill['Skill 3:']['Minimum level']:
    if c > skill['Skill 3:']['Hit rate']:
        print('HIT!!','sat thuong ban gay ra la:',skill['Skill 3:']['damage']) 
    else:
        print('Skill cua ban da truot')
else:
    print('Skill chua xac dinh!')