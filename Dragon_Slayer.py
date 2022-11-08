from colorama import init, Fore, Back, Style
init()

import random

armor = ["Leather_Helmet","Leather_Boots","Leather_Breastplate"]
weapons = ["Wooden_Sword","Wooden_Shield"]
items = ["Health_Potion"]

tutorial =Fore.MAGENTA + '''Let me explain how combat works since this is your first time
You will take turns fighing each other by attacking or defending
You win by making the enemies health points reach zero and vice versa lose if you health points hit zero
observing who you are fighting and what actions they will take will be key to victory
You start with 20 health btw and after every battle you will be told your remaining health
Good luck in battle and cant wait to talk again soon~'''

print(Fore.GREEN + "CHAPTER 0: THE BEGINNING")

print()

print(Fore.WHITE + "You wake up in an unfamiliar land")
print("You look around seeing you are in a forest of some sort with only a single path ahead of you")
input("Before you figure out what to do you start to hear a voice...")

print()

print(Fore.BLUE + "Hello Hero!")
print("I have summoned you to this world to save us from the evil dragon")
print("If you ever want to return to your world you must do as I tell you")
print("I have given you the basic equipment to start your quest")
print("The path forward will have you facing many challenges that will prepare you for the finale fight against the evil dragon!")
input("Now go forth Hero I will continue watching you from afar")

print()

print(Fore.WHITE + "With a brief explanation from an unknown being you stand up and prepare for your quest")
print("You notice you have been given equipment not very suited for a so called Hero")
print(armor)
print(weapons)
print(items)

print()

print("Hopefully you find some better equipment before you have to fight an evil dragon")
print("But with little choice but to move forward and slay the evil dragon to return yourself to your world you take your first step forward")
input("Not knowing the difficulties you are about to face...")

print()

print(Fore.GREEN + "CHAPTER 1: A FORK IN THE ROAD")

print()

print(Fore.WHITE + "As your walking you start to look around at a fimilar yet differnt environment")
print("Many trees with leaves bright blue instead of green")
print("Small creatures resembling rats have wings on their backs jumping from tree to tree")
print("When you look to the sky you see not 1 but 2 suns shining brightly in the distance")
print("You start to think about what other differences there could be between this world and yours")
input("But before you can continue that thought you are stopped with a fork in the road... ")

print()

print("You look down the left path and see the leaves on the trees drying up and the dirt road changing from dirt to sand")
print("You feel a dry heat blowing from the left path and notice a small sign pointing in that direction")
print("The sign reads: CAUTION EXTREME HEAT AND POISONOUS ANIMALS")
input("Now who doesnt love poisonous animals? Hopefully the right path will be a bit more welcoming...")

print()

print("You look down the right path and to your suprise see almost the exact opposite as the left path")
print("The trees become taller and you see what looks like snow falling from the leaves onto the dirt path")
print("You feel a frosty gust of wind blow from the right path and notice yet another sign pointing in that diresction")
print("The sign reads: CAUTION EXTREME COLD AND WILD WOLF HARES")
input("Wolf Hares...like a wolf/rabbit hybrid? sounds adorable...")

print()

print("You take a step back to mull over your choices")
print("You must continue forward if you ever want to return to your world again")
print("But both choices are dangerous in different ways")

choice_1 = ()

while choice_1 not in ["left","Left","right","Right"]:
    choice_1 = input(Fore.YELLOW + "So which path will you choose left or right?: ")

hero_health = 20
hero_action = ""

if choice_1 == "Left" or choice_1 == "left":
    print()
    print(Fore.WHITE + "You decide to take the left path")
    print("Heat and poison have never held you back before so im sure you will be fine")
    print("You start walking forward on a sandy path and where there were once trees are now replaced by strangly shaped red cacti")
    print("The heat from the 2 suns in the sky intensifies and with no trees to give you shade the suns rays heat your skin like you have never felt before")
    input("You trudge forward as the sand beneath your feet starts to humble...")

    print()

    print("You stop as the shaking intensifies")
    print("In front of you the hot sand blast into the air and a creature emerges from the ground")
    print("A giant dark red scorpion stands on its 8 legs staring at you with its 4 giant pitch black eyes")
    print("About half the size of you and instead of having 2 pincers like a scorpion from your world has it has claws with sharp long nails made for digging and slashing")
    input("It hisses at you and scurries towards you....")

    print()

    print(Fore.RED + "PREPARE FOR BATTLE!!!")
    scorpion_health = 3

    print()
    print(tutorial)

    print(Fore.WHITE + "")

    while hero_health > 0:
        print("The scorpion readies his claws to attack!")
        hero_action = input("Would you like to attack or defend?: ")

        if hero_action == "Attack" or hero_action == "attack":
            print("You slash the scorpion with your sword as it slashes you with its claws!")
            hero_health -= 2
            scorpion_health -= 2
        elif hero_health == "Defend" or hero_action == "defend":
            print("You raise your shield just as the scorpion slashes at you blocking its attack!")
        else:
            print("You didnt attack or defend!")
            print("The scorpion slashes you hurting you badly!")
            hero_health -= 4
        
        if scorpion_health < 1:
            break
        print()

        print("The scorpion pulls its claws back to cover itself!")
        hero_action = input("Would you like to attack or defend?: ")

        if hero_action == "Attack" or hero_action == "attack":
            print("You slash the scorpion with your sword as it attempts to parry only blocking half your strike!")
            scorpion_health -= 1
        elif hero_health == "Defend" or hero_action == "defend":
            print("You raise your shield to protect yourself against nothing!")
            print("The scorpion is also defending itself")
        else:
            print("You didnt attack or defend! but the scorpion is defending itself...you got lucky")
        
        if scorpion_health < 1:
            break
        print()

    if hero_health < 1:
        print("The scorpion slashed you one to many times")
        input("You die slowly cut to pieces by the scorpion....")
        quit()
    
    print()
    print("With the finale slash of your sword the scorpion rolls over and passes away")

    heal_1 = ""
    print(f"Your current health is {hero_health}")
    if hero_health == 20:
        print("You didnt get hurt at all from that battle")
        print("GOOD JOB!")
    else:
        while heal_1 not in ["yes","Yes","no","No"]:
            heal_1 = input("You currently have a health potion would you like to use it? yes/no: ")
        
            if heal_1 == "yes" or heal_1 == "Yes":
                print("You drink the health potion healing you completely")
                items.remove("Health_Potion")
            elif heal_1 == "no" or heal_1 == "No":
                print("You save your potion for another battle")
            else:
                print("Type yes to use potion or no to not use potion")
    
    print()

    print("With the scorpion slain you continue marching forward hoping thats the last monster you have to battle")
    print("After what feels like hours you come across a tall rectangular shaped temple with stairs leading to the top")
    print("You start climbing the stairs with every step making you feel like your getting closer to the suns in the sky")
    print("Once you reach the top infront of you is a chest and golem statue with a flame on its head ")
    input("You step towards the chest and using all your might lift the lid now able to get whatever is inside...")

    print()

    print("Inside the box is a set of dark black metal armor!")
    print("You put on your new armor and tho much stronger then your old leather armor it is strangely lighter")
    armor.clear()
    armor.extend(["Black_Metal_Helmet","Black_Metal_Boots","Black_Metal_Breatplate"])
    print(armor)
    input("With your new armor on you throw your old set of leather armor into the fire on top the golem statues head but suddenly hear a booming voice.... ")

    print()

    print(Fore.CYAN + "WHO DARES DISTURBE MY SLUMBER")
    print(Fore.WHITE + "The golem statue tho not moving is speaking to you!")
    print(Fore.CYAN + "AHH I SEE WE HAVE A NEW HERO")
    print("SOLVE MY RIDDLE AND I WILL GIVE YOU A REWARD YOU ARE SURE TO LOVE")
    input("BUT FAIL AND YOU SHALL SUFFER THE CONSEQUENCES...")

    print()
    hero_answ =""
    guess_count = 0

    print("I EAT, I LIVE, I BREATHE, I LIVE, I DRINK, I DIE")

    while hero_answ not in ["fire",'Fire',"flame","Flame"]:
        hero_answ = input("WHAT AM I???: ")
        guess_count += 1
        if guess_count > 2:
            break

    if guess_count <= 3:
        print()
        print("THAT IS CORRECT!")
        print("HERE IS YOUR REWARD I AM GOING BACK TO SLEEP")
        print(Fore.WHITE + "The golems mouth open and out comes a grenade!")
        print("Wait a grenade??? isnt that a weapon from yours world")
        items.append("Grenade")
        print("Before you can question why a weapon from your world is here you start to hear a rumble...")
    else:
        print()
        print(Fore.CYAN + "WRONG! NOW FACE MY WRATH")
        print(Fore.WHITE + "The golems mouth opens and shoots a poison slime onto you!")
        hero_health -= 2
        print("The poison slime burns your skin")
        if hero_health <1:
            input("You cant withstand the poison...you died")
            quit()
        print("But before you get the posion off yourself you start to hear a rumble...")
        
    print()

    print("The floor below you opens up and you start to fall for what feels like an eternity")
    print("You cant understand how you have been falling for so long when it didnt take you this long to climb the temple")
    print("But at that moment you land onto a soft white fluffy floor")
    input("You look around and can tell you no longer in the dessert but in a new unkown area...")
    
if choice_1 == "Right" or choice_1 == "right":
    print()
    print(Fore.WHITE + "You decide to take the right path")
    print("You can handle the cold and im sure wolf hares are friendly!")
    print("You start to walk forward as the dirt beneath your feet is slowly replaced by snow")
    print("Thick white clouds and tall trees hide the suns in the sky making you wish you had somthing to help fight against this freezing weather")
    print("Around you are small critters covered in thick white hair camouflaging with the pure white snow making it hard to identify them at all")
    print("You can start to hear a lound thumping in the distance making all the small animals hide in the snow")
    input("A giant grey figure jumps from behind a tree right in front of you catching you by suprise....")

    print()

    print("As you gain your composure standing in front of you is a giant grey wolf hare")
    print("The creature has thick greay hair with giant rabbit legs giving it the ability to pounce great distances")
    print("The rest of the body resembles that of a wolf except a round wide eyed rabbit face")
    print("But as it growls you can see giant rows of razar sharp teeth inside its mouth")
    input("The creature is not friendly at all and ready to to rip you to shredds...")

    print()

    print(Fore.RED + "PREPARE FOR BATTLE!!!")
    wolf_health = 3

    print()
    print(tutorial)

    print(Fore.WHITE + "")
