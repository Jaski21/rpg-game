import random 
import time
import sys
from colorama import Fore, Style


def dispHealth():
    health = ["|"] * healthnum
    ehealth = ["|"] * ehealthnum
    print("Your Health:  ", end="")
    for i in range(len(health)):
        print(Fore.GREEN+f"{health[i]}"+Style.RESET_ALL, end="")
        sys.stdout.flush()
        time.sleep(0.005)
    for i in range(100-len(health)):
        print(Fore.RED+f"|"+Style.RESET_ALL, end="")
        sys.stdout.flush()
        time.sleep(0.005)
    print("\nEnemy Health: ", end="")
    for i in range(len(ehealth)):
        print(Fore.WHITE+f"{ehealth[i]}"+Style.RESET_ALL, end="")
        sys.stdout.flush()
        time.sleep(0.005)
    for i in range(100-len(ehealth)):
        print(Fore.BLACK+f"|"+Style.RESET_ALL, end="")
        sys.stdout.flush()
        time.sleep(0.005)
    print()


def attack():
    global healthnum, ehealthnum
    atk_numbers = list(range(1, 11))
    weights = [1, 2, 4, 8, 10, 8, 4, 2, 1, 0.5]
    effectiveness = random.choices(atk_numbers, weights=weights, k=1)[0]
    damage = int(effectiveness * 3.5)
    defending = random.randint(1,5)
    script = ["You hit the enemy...",
              "The enemy barely felt anything and you accidentally hit yourself. 12 damage taken. ",
              "Your attack scratched the enemy. ",
              "You hit the enemy with full force!",
              "But you tripped and fell while attacking. 5 damage taken. ",
              "You attacked the enemy but held back. ",
              "You hit the enemy with the sharp end of your sword. ",
              "The enemy stumbled a bit when you hit it. ",
              "You sliced the enemy. ",
              "You charged at the enemy with your sword in hand. The enemy felt fear for the first time. ",
              "You threw yourself at the enemy, which caught it off guard and you attacked it with all you got. "]
    if defending == 1:
        damage -= 4
    if defence:
        damage -= 6
    if damage < 0:
        damage = 0
    if effectiveness == 1:
        print(Fore.RED + script[0] + Style.RESET_ALL)
        print(Fore.RED + script[1] + Style.RESET_ALL)
        ehealthnum -= damage
        healthnum -= 12
    elif effectiveness == 2:    
        print(Fore.RED + script[2] + Style.RESET_ALL)
        ehealthnum -= damage
    elif effectiveness == 3:    
        print(Fore.RED + script[3] + Style.RESET_ALL)
        print(Fore.RED + script[4] + Style.RESET_ALL)
        ehealthnum -= damage
        healthnum -= 5
    elif effectiveness == 4:    
        print(Fore.YELLOW + script[5] + Style.RESET_ALL)
        ehealthnum -= damage
    elif effectiveness == 5:    
        print(Fore.YELLOW + script[0] + Style.RESET_ALL)
        ehealthnum -= damage
    elif effectiveness == 6:    
        print(Fore.YELLOW + script[6] + Style.RESET_ALL)
        ehealthnum -= damage
    elif effectiveness == 7:
        print(Fore.GREEN + script[7] + Style.RESET_ALL)
        ehealthnum -= damage
    elif effectiveness == 8:    
        print(Fore.GREEN + script[3] + Style.RESET_ALL)
        print(Fore.GREEN + script[8] + Style.RESET_ALL)
        ehealthnum -= damage
    elif effectiveness == 9:    
        print(Fore.GREEN + script[9] + Style.RESET_ALL)
        ehealthnum -= damage
    elif effectiveness == 10:    
        print(Fore.GREEN + script[10] + Style.RESET_ALL)
        ehealthnum -= damage
    
    healthnum = max(0, healthnum)
    ehealthnum = max(0, ehealthnum)

    if defending == 1:
        print("But the enemy was defending. ", end="")
    print(f"{damage} damage given\n")


def defend():
    global defence
    defence = True
    print("You prepare for the enemy's attack and reduce your attack by defending")
    attack()


def nothing():
    global healthnum, ehealthnum, patience
    if healthnum == 0 and patience:
        print("The enemy brought your health all the way down... Now you unleash all the stored power onto the enemy and absorb the enemy's life energy!")
        healthnum = 100
        ehealthnum = 0
    elif healthnum > 0:
        print("You do nothing... Just standing and waiting for the enemy to attack.")


def takeDamage():
    global healthnum, defence
    base_damage = random.randint(10, 21)
    crit_roll = random.randint(1, 100)
    if crit_roll <= 15:
        base_damage += random.randint(7, 15)
        print(Fore.RED + "CRITICAL HIT! The enemy unleashes a devastating strike!" + Style.RESET_ALL)
    elif crit_roll >= 85:
        base_damage -= 10
        print(Fore.GREEN + "The enemy fumbled and dealt minimal damage." + Style.RESET_ALL)
    if defence:
        print(Fore.YELLOW + "You were defending! Damage reduced by half." + Style.RESET_ALL)
        base_damage = int(base_damage / 2)
        defence = False
    healthnum -= base_damage
    healthnum = max(0, healthnum)
    print(f"You took {base_damage} damage.\n")


def obj():
    print("Defeat the enemy before they defeat you. Manage your health, choose wisely between attacking, defending, or doing nothing")
    print("Both you and the enemy start with 100 HP.")
    print("Attack: Deals damage to the enemy")
    print("Defend: Reduces damage from the enemy's next attack and weakens your own attack")
    print("Nothing: Skip your turn. Why would you do this?")
    print("You die, you lose\n-------------------------------------------------------------------------")
    print("Starting in: ", end="")
    sec = 15
    for i in range(15):
        if sec > 8:
            print(Fore.GREEN+f"{sec}"+Style.RESET_ALL, end=" ")
        elif sec > 3:
            print(Fore.YELLOW+f"{sec}"+Style.RESET_ALL, end=" ")
        else:
            print(Fore.RED+f"{sec}"+Style.RESET_ALL, end=" ")
        sec -= 1
        sys.stdout.flush()
        time.sleep(1)
    print()



ehealthnum = healthnum = 100
ehealth = health = ["|"] * 100
defence = False
patience = True
while True:
    x = input("Pess (0) to fight or (1) to read objective: ")
    if x == '0':
        break
    elif x == '1':
        obj()
        break
    else:
        print("Enter a valid input")
print("The enemy approaches you", end="")
for i in range (3):
    print(".", end="")
    sys.stdout.flush()
    time.sleep(0.3)
print("\n")
while healthnum > 0 and ehealthnum > 0:
    dispHealth()
    print(Fore.RED+"1. Attack"+Style.RESET_ALL)
    print(Fore.BLUE+"2. Defend"+Style.RESET_ALL)
    print(Fore.GREEN+"3.Nothing"+Style.RESET_ALL)
    print(Fore.YELLOW+"Choice: "+Style.RESET_ALL, end="")
    try:
        choice = int(input())
    except ValueError:
        print("Invalid input. Defaulting to 'nothing'...\n")
        choice = 0
    if choice == 1:
        patience = False
        attack()
    elif choice == 2:
        patience = False
        defend()
    else:
        nothing()
    print("The enemy now prepares to attack you...")
    takeDamage()
    if healthnum == 0:
        nothing()

dispHealth()
print("\n--------------------------------------------------")
if ehealthnum == 0 and healthnum == 0:
    print(Fore.BLACK+"You both destroyed each other in a back to back series of attacks"+Style.RESET_ALL)
elif ehealthnum == 0:
    print(Fore.GREEN+"You defeated the enemy!!!"+Style.RESET_ALL)
elif healthnum == 0:
    print(Fore.RED+"You were defeated by the enemy..."+Style.RESET_ALL)
    