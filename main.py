import time
import random as r

class Entity:
    def __init__(self, health, initiative, attack, defense, dexterity, weapon):
        self.health = health
        self.initiative = initiative
        self.attack = attack
        self.defense = defense
        self.dexterity = dexterity
        self.weapon = weapon
class Class:
    def __init__(self, initiative, attack, defense, dexterity, weapon):
        self.initiative = initiative
        self.attack = attack
        self.defense = defense
        self.dexterity = dexterity
        self.weapon = weapon


warrior = Class(3, 5, 10, 3, 'sword')
rogue = Class(10, 8, 5, 8, 'pair of daggers')
wizard = Class(6, 9, 3, 6, 'fire spell')

Char = Entity(10, 1, 1, 1, 1, 'fists')
wolves = Entity(3, 3, 3, 3, 5, 'fangs')
skeleton_warrior = Entity(8, 6, 6, 6, 6, 'mace')
unknown_mage = Entity(25, 5, 15, 10, 10, 'ornate staff')

game_over = False

inventory = {'coin': 250, 'potions': 10}

#~~~~~Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def intro_text1():
    int_file = open("Intro_Text.txt", 'r')
    constant = int_file.readlines()

    for i in range(2, 11):
        print(constant[i])
        time.sleep(0.5)

    int_file.close()

def class_stats():
    print("warrior", '\n')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", '\n')
    print("initiative: ", warrior.initiative, '\n')
    print("attack: ", warrior.attack, '\n')
    print("defense: ", warrior.defense, '\n')
    print("dexterity: ", warrior.dexterity, '\n')
    print("weapon: ", warrior.weapon, '\n')

    print("rogue", '\n')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", '\n')
    print("initiative: ", rogue.initiative, '\n')
    print("attack: ", rogue.attack, '\n')
    print("defense: ", rogue.defense, '\n')
    print("dexterity: ", rogue.dexterity, '\n')
    print("weapon: ", rogue.weapon, '\n')

    print("wizard", '\n')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", '\n')
    print("initiative: ", wizard.initiative, '\n')
    print("attack: ", wizard.attack, '\n')
    print("defense: ", wizard.defense, '\n')
    print("dexterity: ", wizard.dexterity, '\n')
    print("weapon: ", wizard.weapon, '\n')


def intro_text2():
    int_file = open("Intro_Text.txt", 'r')
    constant = int_file.readlines()

    for i in range(15, 20):
        print(constant[i])
        time.sleep(0.5)

    int_file.close()


def intro_combat():
    print('\n')
    print("ENTERING COMBAT!")

    enemy_init = r.randint(1, 20) + (wolves.initiative*0.5)
    player_init = r.randint(1, 20) + (Char.initiative*0.5)

    if player_init >= enemy_init:
        print("As the wolves approach, you ready yourself to act.")
        while Char.health != 0 and wolves.health != 0:
            print("Your health is", Char.health, "what do you choose to do?")
            action = input("(attack, guard, use potion): ")
            Char.defense = Default_defense

            if action == 'attack':
                p_attack = r.randint(1, 20) + (Char.attack * 0.5)
                e_defense = r.randint(1, 20) + (wolves.defense * 0.5)

                print("your attack:", p_attack)
                print('enemy defense:', e_defense)

                if p_attack >= e_defense:
                    print("you attack with your", Char.weapon, "and land a blow on the enemy.")
                    wolves.health = wolves.health - 1
                    if wolves.health == 0:
                        print("The wolves lay slain on the ground before you.")
                        break
                elif p_attack < e_defense:
                    print("You attempt to attack the enemy, but miss")

            elif action == 'guard':
                print("You ready yourself for an attack bracing to minimize damage.")
                Char.defense = Char.defense * 2

            elif action == 'use potion':
                print("Your reach into your pack to pullout a potion to drink.")

                if inventory['potions'] > 0:
                    Char.health = Char.health + 5
                    inventory['potions'] -= 1
                    if Char.health >= 10:
                        Char.health = 10
                        print("while you feel better, you might not have gotten the full benefits of the potion")
                    else:
                        print("You feel much better after consuming the potion.")
                    print("You have", inventory['potions'], "potions left.")
                elif inventory['potions'] <= 0:
                    print("You don't have anymore potions.")
            else:
                print("You ponder that thought for a moment, but decide that doesn't make sense.")

            e_attack = r.randint(1, 20) + (wolves.attack * 0.5)
            p_defense = r.randint(1, 20) + (Char.defense * 0.5)

            print("enemy attack:", e_attack)
            print("your defense:", p_defense)

            if e_attack >= p_defense:
                print("the wolves lung at you to bit, landing their attack.")
                Char.health = Char.health - 1
                if Char.health == 0:
                    print("Despite your valiant efforts you fall during combat!")
                    game_over = True
                    break
            else:
                print("The wolves attempted to lunge and bit you, but you deftly evaded their attack.")


    elif player_init < enemy_init:
        print("As the wolves approach, you ready yourself to act.")
        while Char.health != 0 and wolves.health != 0:

            e_attack = r.randint(1, 20) + (wolves.attack * 0.5)
            p_defense = r.randint(1, 20) + (Char.defense * 0.5)

            print("enemy attack:", e_attack)
            print("your defense:", p_defense)

            if e_attack >= p_defense:
                print("the wolves lung at you to bit, landing their attack.")
                Char.health = Char.health - 1
                if Char.health == 0:
                    print("Despite your valiant efforts you fall during combat!")
                    game_over = True
                    break
            else:
                print("The wolves attempted to lunge and bit you, but you deftly evaded their attack.")

            print("Your health is", Char.health, "what do you choose to do?")
            action = input("(attack, guard, use potion): ")
            print('\n')

            Char.defense = Default_defense

            if action == 'attack':
                p_attack = r.randint(1, 20) + (Char.attack * 0.5)
                e_defense = r.randint(1, 20) + (wolves.defense * 0.5)

                print("your attack:", p_attack)
                print('enemy defense:', e_defense)

                if p_attack >= e_defense:
                    print("you attack with your", Char.weapon, "and land a blow on the enemy.", '\n')
                    wolves.health = wolves.health - 1
                    if wolves.health == 0:
                        print("The wolves lay slain on the ground before you.", '\n')
                        break
                elif p_attack < e_defense:
                    print("You attempt to attack the enemy, but miss", '\n')

            elif action == 'guard':
                print("You ready yourself for an attack bracing to minimize damage.", '\n')
                Char.defense = Char.defense * 2

            elif action == 'use potion':
                print("Your reach into your pack and pullout a potion to drink.", '\n')
                if inventory['potions'] > 0:
                    Char.health = Char.health + 5
                    inventory['potions'] -= 1
                    if Char.health >= 10:
                        Char.health = 10
                        print("while you feel better, you might not have gotten the full benefits of the potion")
                    else:
                        print("You feel much better after consuming the potion.")
                    print("You have", inventory['potions'], "potions left.")
                elif inventory['potion'] <= 0:
                    print("You don't have anymore potions.")
            else:
                print("You ponder that thought for a moment, but decide that doesn't make sense.")

    print("COMBAT ENDED!")
    print('\n')



def skeleton_combat():
    print('\n')
    print("ENTERING COMBAT!")

    enemy_init = r.randint(1, 20) + (skeleton_warrior.initiative*0.5)
    player_init = r.randint(1, 20) + (Char.initiative*0.5)

    if player_init >= enemy_init:
        print("As the skeleton warriors approach, you ready yourself to act.")
        while Char.health != 0 and skeleton_warrior.health != 0:
            print("Your health is", Char.health, "what do you choose to do?")
            action = input("(attack, guard, use potion): ")
            Char.defense = Default_defense

            if action == 'attack':
                p_attack = r.randint(1, 20) + (Char.attack * 0.5)
                e_defense = r.randint(1, 20) + (skeleton_warrior.defense * 0.5)

                print("your attack:", p_attack)
                print('enemy defense:', e_defense)

                if p_attack >= e_defense:
                    print("you attack with your", Char.weapon, "and land a blow on the enemy.")
                    skeleton_warrior.health = skeleton_warrior.health - 1
                    if skeleton_warrior.health == 0:
                        print("The skeleton warriors lay slain on the ground before you.")
                        break
                elif p_attack < e_defense:
                    print("You attempt to attack the enemy, but miss")

            elif action == 'guard':
                print("You ready yourself for an attack bracing to minimize damage.")
                Char.defense = Char.defense * 2

            elif action == 'use potion':
                print("Your reach into your pack to pullout a potion to drink.")

                if inventory['potions'] > 0:
                    Char.health = Char.health + 5
                    inventory['potions'] -= 1
                    if Char.health >= 10:
                        Char.health = 10
                        print("while you feel better, you might not have gotten the full benefits of the potion")
                    else:
                        print("You feel much better after consuming the potion.")
                    print("You have", inventory['potions'], "potions left.")
                elif inventory['potions'] <= 0:
                    print("You don't have anymore potions.")
            else:
                print("You ponder that thought for a moment, but decide that doesn't make sense.")

            e_attack = r.randint(1, 20) + (skeleton_warrior.attack * 0.5)
            p_defense = r.randint(1, 20) + (Char.defense * 0.5)

            print("enemy attack:", e_attack)
            print("your defense:", p_defense)

            if e_attack >= p_defense:
                print("the skeleton warriors swing there weapon, landing their attack.")
                Char.health = Char.health - 1
                if Char.health == 0:
                    print("Despite your valiant efforts you fall during combat!")
                    break
            else:
                print("The skeleton warriors attempted to attack you, but you deftly evaded their attack.")


    elif player_init < enemy_init:
        print("As the skeleton warriors approach, you ready yourself to act.")
        while Char.health != 0 and skeleton_warrior.health != 0:

            e_attack = r.randint(1, 20) + (skeleton_warrior.attack * 0.5)
            p_defense = r.randint(1, 20) + (Char.defense * 0.5)

            print("enemy attack:", e_attack)
            print("your defense:", p_defense)

            if e_attack >= p_defense:
                print("the skeleton warriors swing their weapon, landing their attack.")
                Char.health = Char.health - 1
                if Char.health == 0:
                    print("Despite your valiant efforts you fall during combat!")
                    game_over = True
                    break
            else:
                print("The skeleton warriors attempted to attack you, but you deftly evaded their attack.")

            print("Your health is", Char.health, "what do you choose to do?")
            action = input("(attack, guard, use potion): ")
            print('\n')

            Char.defense = Default_defense

            if action == 'attack':
                p_attack = r.randint(1, 20) + (Char.attack * 0.5)
                e_defense = r.randint(1, 20) + (skeleton_warrior.defense * 0.5)

                print("your attack:", p_attack)
                print('enemy defense:', e_defense)

                if p_attack >= e_defense:
                    print("you attack with your", Char.weapon, "and land a blow on the enemy.", '\n')
                    skeleton_warrior.health = skeleton_warrior.health - 1
                    if skeleton_warrior.health == 0:
                        print("The skeleton warriors lay slain on the ground before you.", '\n')
                        break
                elif p_attack < e_defense:
                    print("You attempt to attack the enemy, but miss", '\n')

            elif action == 'guard':
                print("You ready yourself for an attack bracing to minimize damage.", '\n')
                Char.defense = Char.defense * 2

            elif action == 'use potion':
                print("Your reach into your pack and pullout a potion to drink.", '\n')
                if inventory['potions'] > 0:
                    Char.health = Char.health + 5
                    inventory['potions'] -= 1
                    if Char.health >= 10:
                        Char.health = 10
                        print("while you feel better, you might not have gotten the full benefits of the potion")
                    else:
                        print("You feel much better after consuming the potion.")
                    print("You have", inventory['potions'], "potions left.")
                elif inventory['potion'] <= 0:
                    print("You don't have anymore potions.")
            else:
                print("You ponder that thought for a moment, but decide that doesn't make sense.")

    print("COMBAT ENDED!")
    print('\n')



def mage_combat():
    print('\n')
    print("ENTERING COMBAT!")

    enemy_init = r.randint(1, 20) + (unknown_mage.initiative*0.5)
    player_init = r.randint(1, 20) + (Char.initiative*0.5)

    if player_init >= enemy_init:
        print("As the robed mage approach, you ready yourself to act.")
        while Char.health != 0 and unknown_mage.health != 0:
            print("Your health is", Char.health, "what do you choose to do?")
            action = input("(attack, guard, use potion): ")
            Char.defense = Default_defense

            if action == 'attack':
                p_attack = r.randint(1, 20) + (Char.attack * 0.5)
                e_defense = r.randint(1, 20) + (unknown_mage.defense * 0.5)

                print("your attack:", p_attack)
                print('enemy defense:', e_defense)

                if p_attack >= e_defense:
                    print("you attack with your", Char.weapon, "and land a blow on the enemy.")
                    unknown_mage.health = unknown_mage.health - 1
                    if unknown_mage.health == 0:
                        print("The robed mage lay slain on the ground before you.")
                        break
                elif p_attack < e_defense:
                    print("You attempt to attack the enemy, but miss")

            elif action == 'guard':
                print("You ready yourself for an attack bracing to minimize damage.")
                Char.defense = Char.defense * 2

            elif action == 'use potion':
                print("Your reach into your pack to pullout a potion to drink.")

                if inventory['potions'] > 0:
                    Char.health = Char.health + 5
                    inventory['potions'] -= 1
                    if Char.health >= 10:
                        Char.health = 10
                        print("while you feel better, you might not have gotten the full benefits of the potion")
                    else:
                        print("You feel much better after consuming the potion.")
                    print("You have", inventory['potions'], "potions left.")
                elif inventory['potions'] <= 0:
                    print("You don't have anymore potions.")
            else:
                print("You ponder that thought for a moment, but decide that doesn't make sense.")

            e_attack = r.randint(1, 20) + (unknown_mage.attack * 0.5)
            p_defense = r.randint(1, 20) + (Char.defense * 0.5)

            print("enemy attack:", e_attack)
            print("your defense:", p_defense)

            if e_attack >= p_defense:
                print("the robed mage shots a necrotic spell at you, landing their attack.")
                Char.health = Char.health - 3
                if Char.health <= 3:
                    print("Despite your valiant efforts you fall during combat!")
                    break
            else:
                print("The robed mage attempts to cast a spell at you, but you deftly evaded their attack.")


    elif player_init < enemy_init:
        print("As the robed mage approach, you ready yourself to act.")
        while Char.health != 0 and unknown_mage.health != 0:

            e_attack = r.randint(1, 20) + (unknown_mage.attack * 0.5)
            p_defense = r.randint(1, 20) + (Char.defense * 0.5)

            print("enemy attack:", e_attack)
            print("your defense:", p_defense)

            if e_attack >= p_defense:
                print("the robed mage shoots a necrotic spell at you, landing their attack.")
                Char.health = Char.health - 3
                if Char.health <= 3:
                    print("Despite your valiant efforts you fall during combat!")
                    break
            else:
                print("The robed mage attempts to cast a spell at you, but you deftly evaded their attack.")

            print("Your health is", Char.health, "what do you choose to do?")
            action = input("(attack, guard, use potion): ")
            print('\n')

            Char.defense = Default_defense

            if action == 'attack':
                p_attack = r.randint(1, 20) + (Char.attack * 0.5)
                e_defense = r.randint(1, 20) + (unknown_mage.defense * 0.5)

                print("your attack:", p_attack)
                print('enemy defense:', e_defense)

                if p_attack >= e_defense:
                    print("you attack with your", Char.weapon, "and land a blow on the enemy.", '\n')
                    unknown_mage.health = unknown_mage.health - 1
                    if unknown_mage.health == 0:
                        print("The Robed mage lay slain on the ground before you.", '\n')
                        break
                elif p_attack < e_defense:
                    print("You attempt to attack the enemy, but miss", '\n')

            elif action == 'guard':
                print("You ready yourself for an attack bracing to minimize damage.", '\n')
                Char.defense = Char.defense * 2

            elif action == 'use potion':
                print("Your reach into your pack and pullout a potion to drink.", '\n')
                if inventory['potions'] > 0:
                    Char.health = Char.health + 5
                    inventory['potions'] -= 1
                    if Char.health >= 10:
                        Char.health = 10
                        print("while you feel better, you might not have gotten the full benefits of the potion")
                    else:
                        print("You feel much better after consuming the potion.")
                    print("You have", inventory['potions'], "potions left.")
                elif inventory['potion'] <= 0:
                    print("You don't have anymore potions.")
            else:
                print("You ponder that thought for a moment, but decide that doesn't make sense.")

    print("COMBAT ENDED!")
    print('\n')

def intro_text3():
    int_file = open("Intro_Text.txt", 'r')
    constant = int_file.readlines()

    for i in range(24, 30):
        print(constant[i])
        time.sleep(0.5)

    int_file.close()

def town_intro():
    int_file = open("Town_Text.txt", 'r')
    constant = int_file.readlines()

    for i in range(2, 12):
        print(constant[i])
        time.sleep(0.5)

    int_file.close()


def town():
    in_town = True
    inter_t_owner = False
    inter_a_owner = False
    inter_c_leader = False
    tavern_info = False
    apothecary_info = False
    chapel_info = False
    first_time = False
    day = False
    town_intro()
    while in_town:

        while day == False:

            print("where would you like to go?", '\n')
            choice = input("(tavern, apothecary, chapel): ")

            if choice == 'tavern':
                in_tavern = True

                int_file = open("Town_Text.txt", 'r')
                constant = int_file.readlines()

                for i in range(18, 21):
                    print(constant[i])
                    time.sleep(0.5)

                int_file.close()

                while in_tavern == True:

                    print("What would you like to do in the tavern?")
                    choice = input("(speak to patrons, speak to tavern owner, leave tavern): ")

                    if choice == 'speak to patrons':
                        int_file = open("Town_Text.txt", 'r')
                        constant = int_file.readlines()

                        for i in range(22, 24):
                            print(constant[i])
                            time.sleep(0.5)

                        int_file.close()

                    elif choice == 'speak to tavern owner':
                        speak_owner = True
                        while speak_owner == True:
                            if inter_t_owner == False:
                                int_file = open("Town_Text.txt", 'r')
                                constant = int_file.readlines()

                                for i in range(26, 28):
                                    print(constant[i])
                                    time.sleep(0.5)

                                int_file.close()

                                inter_t_owner = True

                            elif inter_t_owner == True:
                                int_file = open("Town_Text.txt", 'r')
                                constant = int_file.readlines()

                                for i in range(29, 30):
                                    print(constant[i])
                                    time.sleep(0.5)

                                int_file.close()

                            print("What would you like to do.")
                            choice = input("(order food and drink, rent a room, ask about dark rumors, walk away): ")
                            if choice == 'order food and drink':
                                int_file = open("Town_Text.txt", 'r')
                                constant = int_file.readlines()

                                for i in range(31, 35):
                                    print(constant[i])
                                    time.sleep(0.5)

                                int_file.close()

                                inventory['coin'] = inventory['coin'] - 10
                                print("You have", inventory['coin'], "coin left.")

                            elif choice == 'ask about dark rumors':
                                if tavern_info == False:
                                    int_file = open("Town_Text.txt", 'r')
                                    constant = int_file.readlines()

                                    for i in range(36, 39):
                                        print(constant[i])
                                        time.sleep(0.5)

                                    int_file.close()

                                    tavern_info = True
                                elif tavern_info == True:
                                    print("It seems there's not much more they can add.")

                            elif choice == 'rent a room':
                                int_file = open("Town_Text.txt", 'r')
                                constant = int_file.readlines()

                                for i in range(40, 43):
                                    print(constant[i])
                                    time.sleep(0.5)

                                int_file.close()
                                day = True
                                speak_owner = False
                                in_tavern = False

                                inventory['coin'] = inventory['coin'] - 25
                                print("You have", inventory['coin'], "coin left.")

                            elif choice == 'walk away':
                                print("You tell the tavern owner farewell, and step away from the counter.")
                                speak_owner = False

                            else:
                                print("You ponder that thought, eventually deciding it doesn't make sense.")

                    elif choice == 'leave tavern':
                        print("You head for the door and exit into the center of the village")
                        in_tavern = False

                    else:
                        print("You ponder that thought, eventually deciding it doesn't make sense.")

            elif choice == 'apothecary':
                print("You approach the apothecary, but it seems to be closed for the evening.")

            elif choice == 'chapel':
                print("You approach the chapel, but it seems to be closed for the evening.")

            else:
                print("You ponder that thought, eventually deciding it doesn't make sense.")

        int_file = open("Town_Text.txt", 'r')
        constant = int_file.readlines()

        for i in range(46, 48):
            print(constant[i])
            time.sleep(0.5)

        int_file.close()

        while day == True:

            if tavern_info == True and apothecary_info == True and chapel_info == True:
                print("where would you like to go?", '\n')
                choice = input("(tavern, apothecary, chapel, ruins): ")

            else:
                print("where would you like to go?", '\n')
                choice = input("(tavern, apothecary, chapel): ")

            if choice == 'tavern':
                in_tavern = True
                print("You head into the tavern.", '\n')

                while in_tavern == True:

                    print("What would you like to do in the tavern?")
                    choice = input("(speak to tavern owner, leave tavern): ")

                    if choice == 'speak to tavern owner':
                        speak_owner = True
                        while speak_owner == True:

                            int_file = open("Town_Text.txt", 'r')
                            constant = int_file.readlines()

                            for i in range(29, 30):
                                print(constant[i])
                                time.sleep(0.5)

                            int_file.close()

                            print("What would you like to do.")
                            choice = input("(order food and drink, ask about dark rumors, walk away): ")
                            if choice == 'order food and drink':
                                int_file = open("Town_Text.txt", 'r')
                                constant = int_file.readlines()

                                for i in range(31, 35):
                                    print(constant[i])
                                    time.sleep(0.5)

                                int_file.close()

                                inventory['coin'] = inventory['coin'] - 10
                                print("You have", inventory['coin'], "coin left.")

                            elif choice == 'ask about dark rumors':
                                if tavern_info == False:
                                    int_file = open("Town_Text.txt", 'r')
                                    constant = int_file.readlines()

                                    for i in range(36, 39):
                                        print(constant[i])
                                        time.sleep(0.5)

                                    int_file.close()

                                    tavern_info = True
                                elif tavern_info == True:
                                    print("It seems there's not much more they can add.")

                            elif choice == 'walk away':
                                print("You tell the tavern owner farewell, and step away from the counter.")
                                speak_owner = False

                            else:
                                print("You ponder that thought, eventually deciding it doesn't make sense.")

                    elif choice == 'leave tavern':
                        print("You head for the door and exit into the center of the village")
                        in_tavern = False

                    else:
                        print("You ponder that thought, eventually deciding it doesn't make sense.")

            elif choice == 'apothecary':
                if inter_a_owner == False:
                    int_file = open("Town_Text.txt", 'r')
                    constant = int_file.readlines()

                    for i in range(49, 53):
                        print(constant[i])
                        time.sleep(0.5)

                    int_file.close()

                if inter_a_owner == True:
                    print("You enter the apothecary and the owner asks,\"What else can I do for you?\"")

                speak_owner = True

                while speak_owner == True:
                    choice = input("(buy potions, ask about rumors, leave): ")

                    if choice == 'buy potions':
                        amount = int(input("How many do you want to buy: "))

                        if amount > 0:
                            if amount * 5 <= inventory['coin']:
                                inventory['potions'] = inventory['potions'] + amount
                                inventory['coin'] = inventory['coin'] - amount * 5

                            else:
                                print("You don't have enough coin for that amount.")

                        else:
                            print("you can't do that amount.")

                    elif choice == 'ask about rumors':
                        if apothecary_info == False:
                            int_file = open("Town_Text.txt", 'r')
                            constant = int_file.readlines()

                            for i in range(54, 57):
                                print(constant[i])
                                time.sleep(0.5)

                            int_file.close()

                            apothecary_info = True

                        elif apothecary_info == True:
                            print("It seems there's not much more they can add.")

                    elif choice == 'leave':
                        print("You tell the apothecary owner farewell and leave the shop.")

                        speak_owner = False

                    else:
                        print("You ponder that thought, eventually deciding it doesn't make sense.")

            elif choice == 'chapel':
                in_chapel = True

                if first_time == False:
                    int_file = open("Town_Text.txt", 'r')
                    constant = int_file.readlines()

                    for i in range(58, 61):
                        print(constant[i])
                        time.sleep(0.5)

                    int_file.close()

                    first_time = True
                elif first_time == True:
                    print("You reenter the chapel.", '\n')

                while in_chapel == True:
                    print("what would you like to do in the chapel?")
                    choice = input("(speak to visitors, speak to priest, leave): ")

                    if choice == 'speak to visitors':
                        int_file = open("Town_Text.txt", 'r')
                        constant = int_file.readlines()

                        for i in range(62, 64):
                            print(constant[i])
                            time.sleep(0.5)

                        int_file.close()

                    elif choice == 'speak to priest':
                        if inter_c_leader == False:
                            int_file = open("Town_Text.txt", 'r')
                            constant = int_file.readlines()

                            for i in range(65, 67):
                                print(constant[i])
                                time.sleep(0.5)

                            int_file.close()

                            inter_c_leader = True

                        elif inter_c_leader == True:

                            print("The priest asks, \"Is there anything else I can help you with?\"",'\n')

                        speak_owner = True

                        while speak_owner == True:
                            print("what would you like to do?")
                            choice = input("(ask for blessing, ask about rumors, leave): ")

                            if choice == 'ask for blessing':
                                int_file = open("Town_Text.txt", 'r')
                                constant = int_file.readlines()

                                for i in range(68, 71):
                                    print(constant[i])
                                    time.sleep(0.5)

                                int_file.close()

                                Char.health = 10

                            elif choice == 'ask about rumors':
                                if chapel_info == False:
                                    int_file = open("Town_Text.txt", 'r')
                                    constant = int_file.readlines()

                                    for i in range(72, 78):
                                        print(constant[i])
                                        time.sleep(0.5)

                                    int_file.close()

                                    chapel_info = True

                                elif chapel_info == True:
                                    print("It seems there's not much more they can add.")

                            elif choice == 'leave':
                                print("You bid the priest farewell, and walk away from the pulpit.",'\n')
                                speak_owner = False
                            else:
                                print("You ponder that thought, eventually deciding it doesn't make sense.")

                    elif choice == 'leave':
                        print("you head for the exit of the chapel, leaving into the center of the village.")
                        in_chapel = False
                    else:
                        print("You ponder that thought, eventually deciding it doesn't make sense.")

            elif choice == 'ruins':
                int_file = open("Town_Text.txt", 'r')
                constant = int_file.readlines()

                for i in range(79, 82):
                    print(constant[i])
                    time.sleep(0.5)

                int_file.close()
                day = False
                in_town = False

            else:
                print("You ponder that thought, eventually deciding it doesn't make sense.")


#~~~~~RUINS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def ruin():
    game_over = False
    int_file = open("Ruin_Text.txt", 'r')
    constant = int_file.readlines()

    for i in range(0, 3):
        print(constant[i])
        time.sleep(0.5)

    int_file.close()

    skeleton_combat()

    if game_over == False:
        int_file = open("Ruin_Text.txt", 'r')
        constant = int_file.readlines()

        for i in range(4, 13):
            print(constant[i])
            time.sleep(0.5)

        int_file.close()

        mage_combat()

        int_file = open("Ruin_Text.txt", 'r')
        constant = int_file.readlines()

        for i in range(14, 18):
            print(constant[i])
            time.sleep(0.5)

        int_file.close()

        game_over = True

    if game_over == True:
        print("GAME OVER")


#~~~~~Game~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while not game_over:

    intro_text1()

    class_stats()

    Class_Choice = input("warrior, rogue, wizard: ")

    if (Class_Choice == 'warrior'):
        Char.initiative = warrior.initiative
        Char.attack = warrior.attack
        Char.defense = warrior.defense
        Char.weapon = warrior.weapon

    elif (Class_Choice == 'rogue'):
        Char.initiative = rogue.initiative
        Char.attack = rogue.attack
        Char.defense = rogue.defense
        Char.weapon = rogue.weapon

    elif (Class_Choice == 'wizard'):
        Char.initiative = wizard.initiative
        Char.attack = wizard.attack
        Char.defense = wizard.defense
        Char.weapon = wizard.weapon

    else:
        print("that is not a proper class.")

    print('\n')
    Default_defense = Char.defense

    intro_text2()

    intro_combat()

    if Char.health == 0:
        game_over = True
        break
    else:
        game_over = False

    intro_text3()

    town()

    ruin()

    break



while game_over:
    print("Despite your valiant efforts you fall during combat!")
