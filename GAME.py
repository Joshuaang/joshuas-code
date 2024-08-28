import random
import time
name = input('Enter your name, adventurer: ')
choices = ('1. Fight\n2. Defend\n3. Inventory\n4. Special Attack\n')
hero = {'health':100, 'damage': 10, 'shield durability':3, 'mana':0, 'mana for special attack': 50}
lvl1boss = {'health': 100, 'damage': 20, 'shield durability':3, 'mana': 0, 'mana for special attack': 50}
lvl2boss = {'health': 300, 'damage': 40, 'shield durability':5, 'mana': 0,'mana for special attack': 50}
lvl3boss = {'health': 500, 'damage': 80, 'shield durability':7, 'mana': 0,'mana for special attack': 50}
inventory = ['1. Health Potion','2. Strength Potion','3. Shield Potion','4. Mana Potion']
HP = '1. Health Potion'
STP = '2. Strength Potion'
SHP = '3. Shield Potion'
MP = '4. Mana Potion'
turncount = 0
hero_dmg = hero['damage'] + random.randint(1, 10)
hero_spec_dmg = hero_dmg + 50
lvl1boss_dmg = lvl1boss['damage'] + random.randint(1, 10)
lvl1boss_spec_dmg = lvl1boss_dmg + 50
lvl1boss_defend = 1
lvl2boss_dmg = lvl2boss['damage'] + random.randint(1, 10)
lvl2boss_spec_dmg = lvl2boss_dmg + 50
lvl2boss_defend = 1
lvl3boss_dmg = lvl3boss['damage'] + random.randint(1, 10)
lvl3boss_spec_dmg = lvl3boss_dmg + 50
lvl3boss_defend = 1
mana = random.randint(10, 15)
boss_mana = random.randint(10, 15)

def intro(filename):
    print(f'Welcome adventurer {name}!')
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            print(line)
        print('1. Story mode')

def inputnumber(question):
    while True:
        answer = input(question)
        if answer.isdigit():
            answer = int(answer)
            return answer
        else:
            print("You must enter a number")

def lvl1(sprites1):
    with open(sprites1) as s1:
        s1_lines = s1.readlines()
        for s1_line in s1_lines:
            print(s1_line.strip("\n"))

def lvl2(sprites2):
    with open(sprites2) as s2:
        s2_lines = s2.readlines()
        for s2_line in s2_lines:
            print(s2_line)

def lvl3(sprites3):
    with open(sprites3) as s3:
        s3_lines = s3.readlines()
        for s3_line in s3_lines:
            print(s3_line)

def display_stats(char1, char2):
    print('-'*82)
    for stat in char1:
        print("| {:^30} : {:^5} | {:^30} : {:^5} |".format(stat.upper(), char1[stat], stat.upper(), char2[stat]))
    print('-'*82)

intro('floors.txt')
selectmode = inputnumber('\nWhat mode do you want to play: ')
if selectmode == 1:
    print('1. Floor 1\n2. Floor 2\n3. Floor 3')
    selectfloor = inputnumber("\nWhat floor do you want to choose: ")

    if selectfloor == 1:
        lvl1('floor1sprites.txt')
        time.sleep(2.5)
        print(f'Prince: Well, isnt it {name} who has entered my lair...')
        time.sleep(2.5)
        print(f'{name}: Im just here to defeat you.')
        time.sleep(2.5)
        print(f'Prince: Had it kiddo.')
        time.sleep(2.5)
        turncount = 0

        while True:
            if lvl1boss['health'] < 1:
                print('You win!')
                time.sleep(2)
                hero['health'] = 200
                hero['shield durability'] = 5
                hero['damage'] = 30
                inventory = ['1. Health Potion','2. Strength Potion','3. Shield Potion','4. Mana Potion']
                print(f"You leveled up!\nYou now have {hero['health']}HP!")
                time.sleep(1.5)
                print(f"Your damage increased to {hero['damage']}!")
                time.sleep(1.5)
                print(f"Your shield durability increased to {hero['shield durability']}!")
                time.sleep(1.5)
                print(f'Young adventurer please proceed to floor 2')
                time.sleep(3)
                print('1. Floor 1 (Cleared!)\n2. Floor 2\n3. Floor 3')
                selectfloor = inputnumber("\nWhat floor do you want to choose: ")
                break
            elif hero['health'] < 1:
                print('You lost!')
                break
            else:
                turncount += 1
                display_stats(hero, lvl1boss)
                print(f'\nROUND {turncount}')
                print(choices)
                ability = int(input(f'What are you going to do, {name}: '))

                if ability == 1:
                    time.sleep(1)
                    lvl1boss_movesets = random.choice([lvl1boss_dmg, lvl1boss_defend])
                    print(f'\n{name} Attacked!')
                    if lvl1boss['mana'] >= lvl1boss['mana for special attack']:
                        time.sleep(1)
                        print(f'Prince lost {hero_dmg}HP.')
                        hero['mana'] += mana
                        print(f'{name} gained {mana} mana.')
                        lvl1boss['health'] -= hero_dmg
                        time.sleep(1)
                        print('Prince used his special attack - Lance shot!')
                        time.sleep(1)
                        print(f"{name}' sword was bent! His damage decreased to {hero['damage'] - 5}!")
                        hero['damage'] -= 5
                        time.sleep(1)
                        print(f'{name} lost {lvl1boss_spec_dmg}HP.')
                        hero['health'] -= (lvl1boss_spec_dmg)
                        lvl1boss['mana'] -= lvl1boss['mana for special attack']
                        time.sleep(3)
                    elif lvl1boss_movesets == lvl1boss_dmg:
                        time.sleep(1)
                        print(f'Prince lost {hero_dmg}HP.')
                        time.sleep(1)
                        hero['mana'] += mana
                        print(f'{name} gained {mana} mana.')
                        lvl1boss['health'] -= hero_dmg
                        time.sleep(1)
                        print(f'Prince Attacked!')
                        time.sleep(1)
                        print(f'{name} lost {lvl1boss_dmg}HP.')
                        time.sleep(1)
                        lvl1boss['mana'] += boss_mana
                        print(f'Prince gained {boss_mana} mana.\n')
                        hero['health'] -= lvl1boss_dmg
                        time.sleep(3)
                    elif lvl1boss_movesets == lvl1boss_defend:
                        if lvl1boss['shield durability'] == 0:
                            time.sleep(1)
                            print(f'Prince lost {hero_dmg}HP.')
                            time.sleep(1)
                            hero['mana'] += mana
                            print(f'{name} gained {mana} mana.')
                            lvl1boss['health'] -= hero_dmg
                            time.sleep(1)
                            print(f'Prince Attacked!')
                            time.sleep(1)
                            print(f'{name} lost {lvl1boss_dmg}HP.')
                            time.sleep(1)
                            lvl1boss['mana'] += boss_mana
                            print(f'Prince gained {boss_mana} mana.\n')
                            hero['health'] -= lvl1boss_dmg
                            time.sleep(3)
                        elif lvl1boss['shield durability'] > 0:
                            time.sleep(1)
                            print(f'Prince used his shield!')
                            time.sleep(1)
                            print('Prince took no damage. His shield durability weakened.')
                            time.sleep(1)
                            lvl1boss['mana'] += boss_mana
                            print(f'Prince gained {boss_mana} mana.\n')
                            lvl1boss['shield durability'] -= lvl1boss_defend
                            time.sleep(3)

                elif ability == 2:
                    if hero['shield durability'] > 0:
                        time.sleep(1)
                        lvl1boss_movesets = random.choice([lvl1boss_dmg, lvl1boss_defend])
                        print(f'\n{name} used his shield!')
                        if lvl1boss['mana'] >= lvl1boss['mana for special attack']:
                            time.sleep(1)
                            print('Prince used his special attack - Lance shot!')
                            time.sleep(1)
                            print(f"{name}' sword was bent! His damage decreased to {hero['damage'] - 5}!")
                            hero['damage'] -= 5
                            time.sleep(1)
                            print(f'{name} lost {lvl1boss_spec_dmg - 40}HP. His shield durability weakened.')
                            hero['health'] -= (lvl1boss_spec_dmg - 40)
                            hero['shield durability'] -= 1
                            lvl1boss['mana'] -= lvl1boss['mana for special attack']
                            time.sleep(3)
                        elif lvl1boss_movesets == lvl1boss_dmg:
                            time.sleep(1)
                            print(f'Prince Attacked!')
                            time.sleep(1)
                            print(f'{name} took no damage. His shield durability weakened.')
                            hero['shield durability'] -= 1
                            time.sleep(1)
                            hero['mana'] += mana
                            print(f'{name} gained {mana} mana.\n')
                            time.sleep(3)
                        elif lvl1boss_movesets == lvl1boss_defend:
                            if lvl1boss['shield durability'] == 0:
                                time.sleep(1)
                                print(f'Prince lost {hero_dmg}HP')
                                time.sleep(1)
                                print(f'Prince Attacked!')
                                time.sleep(1)
                                print(f'{name} took no damage. His shield durability weakened.')
                                hero['shield durability'] -= 1
                                time.sleep(1)
                                hero['mana'] += mana
                                print(f'{name} gained {mana} mana.\n')
                                time.sleep(3)
                            elif lvl1boss['shield durability'] > 0:
                                time.sleep(1)
                                print(f'Prince used his shield!')
                                time.sleep(1)
                                print('Nothing happened...')
                                time.sleep(1)
                                print('Both of your shield durabilities weakened.\n')
                                hero['shield durability'] -= 1
                                lvl1boss['shield durability'] -= lvl1boss_defend
                                time.sleep(3)
                    elif hero['shield durability'] == 0:
                        print('You have no shields left. Do something else!')
                        time.sleep(2.5)

                elif ability == 3:
                    print(f'\n{inventory}')
                    item_choice = int(input('choose your item: '))
                    if item_choice == 1:
                        inventory.remove(HP)
                        hero['health'] += 50
                        print(f'\n{name} drank the Health Potion!')
                        time.sleep(1)
                        print(f'{name} gained 50HP!\n')
                        time.sleep(3)
                    elif item_choice == 2:
                        inventory.remove(STP)
                        hero['damage'] += 10
                        print(f'\n{name} drank the Strength Potion!')
                        time.sleep(1)
                        print(f'{name} damage increased by 10!\n')
                        hero_dmg += 10
                        time.sleep(3)
                    elif item_choice == 3:
                        inventory.remove(SHP)
                        hero['shield durability'] += 1
                        print(f'\n{name} drank the Shield Potion!')
                        time.sleep(1)
                        print(f"{name}'s shield increased by 1!\n")
                        time.sleep(3)
                    elif item_choice == 4:
                        inventory.remove(MP)
                        hero['mana'] += 25
                        print(f'\n{name} drank the Mana Potion!')
                        time.sleep(1)
                        print(f"{name}'s mana increased by 25!\n")
                        time.sleep(3)
                    elif item_choice == []:
                        print('You have no items left in your inventory. Do somethhing else!')
                        time.sleep(2.5)
                elif ability == 4:
                    if hero['mana'] >= hero['mana for special attack']:
                        hero['mana'] -= hero['mana for special attack']
                        time.sleep(1)
                        lvl1boss_movesets = random.choice([lvl1boss_dmg, lvl1boss_defend])
                        print(f'\n{name} used his special attack - Dancing sword!')
                        if lvl1boss['mana'] >= lvl1boss['mana for special attack']:
                            time.sleep(1)
                            print(f'Prince lost {hero_spec_dmg}HP.')
                            time.sleep(1)
                            hero['mana'] += mana
                            print(f'{name} gained {mana} mana.')
                            time.sleep(1)
                            print('Prince used his special attack - Lance shot!')
                            time.sleep(1)
                            print(f"{name}' sword was bent! His damage decreased to {hero['damage'] - 5}!")
                            hero['damage'] -= 5
                            time.sleep(1)
                            print(f'{name} lost {lvl1boss_spec_dmg}HP.')
                            hero['health'] -= (lvl1boss_spec_dmg)
                            lvl1boss['mana'] -= lvl1boss['mana for special attack']
                            time.sleep(3)
                        elif lvl1boss_movesets == lvl1boss_dmg:
                            time.sleep(1)
                            print(f'Prince lost {hero_spec_dmg}HP.')
                            time.sleep(1)
                            hero['mana'] += mana
                            print(f'{name} gained {mana} mana.')
                            lvl1boss['health'] -= hero_spec_dmg
                            time.sleep(1)
                            print(f'Prince Attacked!')
                            time.sleep(1)
                            print(f'{name} lost {lvl1boss_dmg}HP.')
                            time.sleep(1)
                            lvl1boss['mana'] += boss_mana
                            print(f'Prince gained {boss_mana} mana.\n')
                            hero['health'] -= lvl1boss_dmg
                            time.sleep(3)
                        elif lvl1boss_movesets == lvl1boss_defend:
                            if lvl1boss['shield durability'] == 0:
                                time.sleep(1)
                                print(f'Prince lost {hero_spec_dmg}HP.')
                                time.sleep(1)
                                hero['mana'] += mana
                                print(f'{name} gained {mana} mana.')
                                time.sleep(1)
                                print(f'Prince Attacked!')
                                time.sleep(1)
                                print(f'{name} lost {lvl1boss_dmg}HP.')
                                time.sleep(1)
                                lvl1boss['mana'] += boss_mana
                                print(f'Prince gained {boss_mana} mana.\n')
                                hero['health'] -= lvl1boss_dmg
                                time.sleep(3)
                            elif lvl1boss['shield durability'] > 0:
                                time.sleep(1)
                                print(f'Prince used his shield!')
                                time.sleep(1)
                                print(f'Prince lost {hero_spec_dmg - 40}. His shield durability weakened.')
                                lvl1boss['shield durability'] -= lvl1boss_defend
                                time.sleep(3)
                    elif hero['mana'] < hero['mana for special attack']:
                        time.sleep(1)
                        print('You dont have enough mana. Do something else!')
                        time.sleep(2.5)

    if selectfloor == 2:
        lvl2('floor2sprites.txt')
        time.sleep(2.5)
        print(f'Berseker: Who brought you here!?')
        time.sleep(2.5)
        print(f'{name}: The prince brought me here. Pretty easy fight.')
        time.sleep(2.5)
        print(f'Berseker: I swear that pathetic imbecile was too weak!')
        time.sleep(2.5)
        print(f'Berseker: I will just kill you myself!!')
        time.sleep(2.5)
        turncount = 0

        while True:
            if lvl2boss['health'] < 1:
                print('You win!')
                time.sleep(2)
                hero['health'] = 300
                hero['shield durability'] = 7
                hero['damage'] = 50
                hero_dmg += 40
                print(f"You leveled up!\nYou now have {hero['health']}HP!")
                time.sleep(1.5)
                print(f"Your damage increased to {hero['damage']}!")
                time.sleep(1.5)
                print(f"Your shield durability increased to {hero['shield durability']}!")
                time.sleep(1.5)
                print(f'Young adventurer please proceed to floor 3')
                time.sleep(3)
                print('1. Floor 1 (Cleared!)\n2. Floor 2 (Cleared!)\n3. Floor 3')
                selectfloor = inputnumber("\nWhat floor do you want to choose: ")
                break
                print
                break
            elif hero['health'] < 1:
                print('You lost!')
                break
            else:
                turncount += 1
                display_stats(hero, lvl2boss)
                print(f'\nROUND {turncount}')
                print(choices)
                ability = int(input(f'What are you going to do, {name}: '))

                if ability == 1:
                    time.sleep(1)
                    lvl2boss_movesets = random.choice([lvl2boss_dmg, lvl2boss_defend])
                    print(f'\n{name} Attacked!')
                    if lvl2boss['mana'] >= lvl2boss['mana for special attack']:
                        time.sleep(1)
                        print(f'Berseker lost {hero_dmg}HP.')
                        hero['mana'] += mana
                        print(f'{name} gained {mana} mana.')
                        lvl2boss['health'] -= hero_dmg
                        time.sleep(1)
                        print('Berseker used his special attack - Club smash!')
                        time.sleep(1)
                        print(f'{name} lost {lvl2boss_spec_dmg}HP.')
                        hero['health'] -= (lvl2boss_spec_dmg)
                        lvl2boss['mana'] -= lvl2boss['mana for special attack']
                        time.sleep(3)
                    elif lvl2boss_movesets == lvl2boss_dmg:
                        time.sleep(1)
                        print(f'Berseker lost {hero_dmg}HP.')
                        time.sleep(1)
                        hero['mana'] += mana
                        print(f'{name} gained {mana} mana.')
                        lvl2boss['health'] -= hero_dmg
                        time.sleep(1)
                        print(f'Berseker Attacked!')
                        time.sleep(1)
                        print(f'{name} lost {lvl2boss_dmg}HP.')
                        time.sleep(1)
                        lvl2boss['mana'] += boss_mana
                        print(f'Berseker gained {boss_mana} mana.\n')
                        hero['health'] -= lvl2boss_dmg
                        time.sleep(3)
                    elif lvl2boss_movesets == lvl2boss_defend:
                        if lvl2boss['shield durability'] == 0:
                            time.sleep(1)
                            print(f'Berseker lost {hero_dmg}HP.')
                            time.sleep(1)
                            hero['mana'] += mana
                            print(f'{name} gained {mana} mana.')
                            lvl2boss['health'] -= hero_dmg
                            time.sleep(1)
                            print(f'Berseker Attacked!')
                            time.sleep(1)
                            print(f'{name} lost {lvl2boss_dmg}HP.')
                            time.sleep(1)
                            lvl2boss['mana'] += boss_mana
                            print(f'Berseker gained {boss_mana} mana.\n')
                            hero['health'] -= lvl2boss_dmg
                            time.sleep(3)
                        elif lvl2boss['shield durability'] > 0:
                            time.sleep(1)
                            print(f'Berseker used his shield!')
                            time.sleep(1)
                            print('Berseker took no damage. His shield durability weakened.')
                            time.sleep(1)
                            lvl2boss['mana'] += boss_mana
                            print(f'Berseker gained {boss_mana} mana.\n')
                            lvl2boss['shield durability'] -= lvl2boss_defend
                            time.sleep(3)

                elif ability == 2:
                    if hero['shield durability'] > 0:
                        time.sleep(1)
                        lvl2boss_movesets = random.choice([lvl2boss_dmg, lvl2boss_defend])
                        print(f'\n{name} used his shield!')
                        if lvl2boss['mana'] >= lvl2boss['mana for special attack']:
                            time.sleep(1)
                            print('Berseker used his special attack - Club smash!')
                            time.sleep(1)
                            print(f'{name} lost {lvl2boss_spec_dmg - 40}HP. His shield durability weakened.')
                            hero['health'] -= (lvl2boss_spec_dmg - 40)
                            hero['shield durability'] -= 1
                            lvl2boss['mana'] -= lvl2boss['mana for special attack']
                            time.sleep(3)
                        elif lvl2boss_movesets == lvl2boss_dmg:
                            time.sleep(1)
                            print(f'Berseker Attacked!')
                            time.sleep(1)
                            print(f'{name} took no damage. His shield durability weakened.')
                            hero['shield durability'] -= 1
                            time.sleep(1)
                            hero['mana'] += mana
                            print(f'{name} gained {mana} mana.\n')
                            time.sleep(3)
                        elif lvl2boss_movesets == lvl2boss_defend:
                            if lvl2boss['shield durability'] == 0:
                                time.sleep(1)
                                print(f'Berseker lost {hero_dmg}HP')
                                time.sleep(1)
                                print(f'Berseker Attacked!')
                                time.sleep(1)
                                print(f'{name} took no damage. His shield durability weakened.')
                                hero['shield durability'] -= 1
                                time.sleep(1)
                                hero['mana'] += mana
                                print(f'{name} gained {mana} mana.\n')
                                time.sleep(3)
                            elif lvl2boss['shield durability'] > 0:
                                time.sleep(1)
                                print(f'Berseker used his shield!')
                                time.sleep(1)
                                print('Nothing happened...')
                                time.sleep(1)
                                print('Both of your shield durabilities weakened.\n')
                                hero['shield durability'] -= 1
                                lvl2boss['shield durability'] -= lvl2boss_defend
                                time.sleep(3)
                    elif hero['shield durability'] == 0:
                        print('You have no shields left. Do something else!')
                        time.sleep(2.5)

                elif ability == 3:
                    print(f'\n{inventory}')
                    item_choice = int(input('choose your item: '))
                    if item_choice == 1:
                        inventory.remove(HP)
                        hero['health'] += 50
                        print(f'\n{name} drank the Health Potion!')
                        time.sleep(1)
                        print(f'{name} gained 50HP!\n')
                        time.sleep(3)
                    elif item_choice == 2:
                        inventory.remove(STP)
                        hero['damage'] += 10
                        print(f'\n{name} drank the Strength Potion!')
                        time.sleep(1)
                        print(f'{name} damage increased by 10!\n')
                        hero_dmg += 10
                        time.sleep(3)
                    elif item_choice == 3:
                        inventory.remove(SHP)
                        hero['shield durability'] += 1
                        print(f'\n{name} drank the Shield Potion!')
                        time.sleep(1)
                        print(f"{name}'s shield increased by 1!\n")
                        time.sleep(3)
                    elif item_choice == 4:
                        inventory.remove(MP)
                        hero['mana'] += 25
                        print(f'\n{name} drank the Mana Potion!')
                        time.sleep(1)
                        print(f"{name}'s mana increased by 25!\n")
                        time.sleep(3)
                    elif item_choice == []:
                        print('You have no items left in your inventory. Do somethhing else!')
                        time.sleep(2.5)
                elif ability == 4:
                    if hero['mana'] >= hero['mana for special attack']:
                        hero['mana'] -= hero['mana for special attack']
                        time.sleep(1)
                        lvl2boss_movesets = random.choice([lvl2boss_dmg, lvl2boss_defend])
                        print(f'\n{name} used his special attack - Dancing sword!')
                        if lvl2boss['mana'] >= lvl2boss['mana for special attack']:
                            time.sleep(1)
                            print(f'Berseker lost {hero_spec_dmg}HP.')
                            time.sleep(1)
                            hero['mana'] += mana
                            print(f'{name} gained {mana} mana.')
                            time.sleep(1)
                            print('Berseker used his special attack - Club smash!')
                            time.sleep(1)
                            print(f'{name} lost {lvl2boss_spec_dmg}HP.')
                            hero['health'] -= (lvl2boss_spec_dmg)
                            lvl2boss['mana'] -= lvl2boss['mana for special attack']
                            time.sleep(3)
                        elif lvl2boss_movesets == lvl2boss_dmg:
                            time.sleep(1)
                            print(f'Berseker lost {hero_spec_dmg}HP.')
                            time.sleep(1)
                            hero['mana'] += mana
                            print(f'{name} gained {mana} mana.')
                            lvl2boss['health'] -= hero_spec_dmg
                            time.sleep(1)
                            print(f'Berseker Attacked!')
                            time.sleep(1)
                            print(f'{name} lost {lvl2boss_dmg}HP.')
                            time.sleep(1)
                            lvl2boss['mana'] += boss_mana
                            print(f'Berseker gained {boss_mana} mana.\n')
                            hero['health'] -= lvl2boss_dmg
                            time.sleep(3)
                        elif lvl2boss_movesets == lvl2boss_defend:
                            if lvl1boss['shield durability'] == 0:
                                time.sleep(1)
                                print(f'Berseker lost {hero_spec_dmg}HP.')
                                time.sleep(1)
                                hero['mana'] += mana
                                print(f'{name} gained {mana} mana.')
                                time.sleep(1)
                                print(f'Berseker Attacked!')
                                time.sleep(1)
                                print(f'{name} lost {lvl2boss_dmg}HP.')
                                time.sleep(1)
                                lvl2boss['mana'] += boss_mana
                                print(f'Berseker gained {boss_mana} mana.\n')
                                hero['health'] -= lvl2boss_dmg
                                time.sleep(3)
                            elif lvl2boss['shield durability'] > 0:
                                time.sleep(1)
                                print(f'Berseker used his shield!')
                                time.sleep(1)
                                print(f'Berseker lost {hero_spec_dmg - 40}HP. His shield durability weakened.')
                                lvl2boss['shield durability'] -= lvl2boss_defend
                                time.sleep(3)
                    elif hero['mana'] < hero['mana for special attack']:
                        time.sleep(1)
                        print('You dont have enough mana. Do something else!')
                        time.sleep(2.5)

