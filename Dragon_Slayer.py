from colorama import init, Fore, Back, Style
init()

armor = ["Leather_Helmet","Leather_Boots","Leather_Breastplate"]
weapons = ["Wooden_Sword","Wooden_Shield"]
items = ["Health_Potion"]

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