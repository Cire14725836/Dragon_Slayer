from colorama import init, Fore, Back, Style
init()

import random

armor = ["Leather_Helmet","Leather_Boots","Leather_Breastplate"]
weapons = ["Wooden_Sword","Wooden_Shield"]
items = ["Health_Potion"]

special_action = ["Love","love","Loved","loved","Apologize","apologize","Lie","lie","Lied","lied","Mystery","mystery","Mysterious","mysterious","Voice","voice","Trick","trick",
"Tricked","tricked","Betray","betray","Betrayed","betrayed","Curse","curse","Cursed","cursed","Sword","sword","Kill","kill","Monster","monster","Murder","murder",
"Time","time","Cycle","cycle","Repeat","repeat","Talk","talk","Question","question","Ask","ask","Hero","hero","Evil","evil","Wizard","wizard","Dragon","dragon","Journey","journey"]

tutorial =Fore.MAGENTA + '''Let me explain how combat works since this is your first time
You will take turns fighing each other by attacking or defending
All actions or responses you take will never be more then 1 word
You win by making the enemies health points reach zero and lose if your health points hit zero
observing who you are fighting and what actions they will take will be key to victory
You start with 20 health btw and after every battle you will be told your remaining health
Good luck in battle and I cant wait to talk to you again soon~'''

print(Fore.RED + "DRAGON SLAYER" + "\n")

print(Fore.GREEN + Back.BLACK + "CHAPTER 0: THE BEGINNING" + "\n")

print(Fore.WHITE + "You wake up in an unfamiliar land")
print("You look around seeing you are in a forest of some sort with only a single path ahead of you")
input("Before you figure out what to do you start to hear a voice from above..." + "\n")

print(Fore.BLUE + "Hello Hero!")
print("I have summoned you to this world to save us from the evil dragon")
print("If you ever want to return to your world you must do as I tell you")
print("I have given you the basic equipment to start your quest")
print("The path forward will have you facing many challenges that will prepare you for the final fight against the evil dragon!")
input("Now go forth Hero I will continue watching you from afar" + "\n")

print(Fore.WHITE + "With a brief explanation from an unknown being you stand up and prepare for your quest")
print("You notice you have been given equipment not very suited for a so called Hero")
print(armor)
print(weapons)
print(items)

print()

print("Hopefully you find some better equipment before you have to fight an evil dragon")
print("But after being summoned to this strange world you have little choice but to move forward")
input("Not knowing the difficulties you are about to face..." + "\n")

print(Fore.GREEN + "CHAPTER 1: A FORK IN THE ROAD" + "\n")

print(Fore.WHITE + "As your walking you start to look around at a fimilar yet differnt environment")
print("Many trees with leaves bright blue instead of green")
print("Small creatures resembling rats have wings on their backs jumping from tree to tree")
print("When you look to the sky you see not one but two suns shining brightly in the distance")
print("You start to think about what other differences there could be between this world and yours")
input("But before you can continue that thought you are stopped with a fork in the road... " + "\n")

print("You look down the left path and see the leaves on the trees drying up and the dirt road changing from dirt to sand")
print("You feel a dry heat blowing from the left path and notice a small sign pointing in that direction")
print("The sign reads: CAUTION EXTREME HEAT AND POISONOUS ANIMALS")
input("Now who doesnt love poisonous animals? Hopefully the right path will be a bit more welcoming..." + "\n")

print("You look down the right path and to your suprise see almost the exact opposite as the left path")
print("The trees become taller and you see what looks like snow falling from the leaves onto the dirt path")
print("You feel a frosty gust of wind blow from the right path and notice yet another sign pointing in that direction")
print("The sign reads: CAUTION EXTREME COLD AND WILD WOLF HARES")
input("Wolf Hares...like a wolf/rabbit hybrid? sounds adorable..." + "\n")

print("You take a step back to mull over your choices")
print("You must continue forward if you ever want to return to your world again")
print("But both choices are dangerous in different ways")

choice_1 = ()

while choice_1 not in ["left","Left","right","Right"]:
    choice_1 = input(Fore.YELLOW + "So which path will you choose left or right?: ")

hero_health = 20
hero_action = ""
heal_1 = ""
hero_answ =""
guess_count = 0

if choice_1 == "Left" or choice_1 == "left":
    print()
    print(Fore.WHITE + "You decide to take the left path")
    print("Heat and poison have never held you back before so im sure you will be fine")
    print("You start walking forward on a sandy path and where there were once trees are now replaced by strangely shaped red cacti")
    print("The heat from the two suns in the sky intensifies and with no trees to give you shade the sun's rays heat your skin like you have never felt before")
    input("You trudge forward as the sand beneath your feet starts to rumble..." + "\n")

    print("You stop as the shaking intensifies")
    print("In front of you the hot sand blast into the air and a creature emerges from the ground")
    print("A giant dark red scorpion stands on its 8 legs, staring at you with its 4 giant pitch black eyes")
    print("About half the size of you and instead of having 2 pincers like a scorpion from your world, it has claws with sharp long nails made for digging and slashing")
    input("It hisses at you and scurries towards you...." + "\n")

    print(Fore.RED + "PREPARE FOR BATTLE!!!" + "\n")
    scorpion_health = 3

    print(tutorial)

    print(Fore.WHITE + "")

    while hero_health > 0:
        print("The scorpion readies his claws to attack!")
        hero_action = input("Would you like to attack or defend?: ")
        hero_action = hero_action.replace(" ","")

        if hero_action == "Attack" or hero_action == "attack":
            print("You slash the scorpion with your sword as it slashes you with its claws!")
            hero_health -= 2
            scorpion_health -= 2
        elif hero_action == "Defend" or hero_action == "defend":
            print("You raise your shield just as the scorpion slashes at you blocking its attack!")
        else:
            print("You didnt attack or defend!")
            print("The scorpion slashes you wounding you badly!")
            hero_health -= 4
        
        if scorpion_health < 1:
            break
        print()

        print("The scorpion pulls its claws back to cover itself!")
        hero_action = input("Would you like to attack or defend?: ")
        hero_action = hero_action.replace(" ","")

        if hero_action == "Attack" or hero_action == "attack":
            print("You slash the scorpion with your sword as it attempts to parry only blocking half your strike!")
            scorpion_health -= 1
        elif hero_action == "Defend" or hero_action == "defend":
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

    print(f"Your current health is {hero_health}")
    if hero_health == 20:
        print("You didnt get hurt at all from that battle")
        print("GOOD JOB!")
    else:
        while heal_1 not in ["yes","Yes","no","No"]:
            heal_1 = input("You currently have a health potion would you like to use it? yes/no: ")
            heal_1 = heal_1.replace(" ","")
        
            if heal_1 == "yes" or heal_1 == "Yes":
                print("You drink the health potion healing you completely")
                items.remove("Health_Potion")
                hero_health = 20
            elif heal_1 == "no" or heal_1 == "No":
                print("You save your potion for another battle")
            else:
                print("Type yes to use potion or no to not use potion")
    
    print()

    print("With the scorpion slain you continue marching forward hoping thats the last monster you have to battle")
    print("After what feels like hours you come across a tall rectangular shaped temple with stairs leading to the top")
    print("You start climbing the stairs with every step making you feel like you're getting closer to the suns in the sky")
    print("Once you reach the top in front of you is a chest and golem statue with a flame on its head")
    input("You step towards the chest and using all your might lift the lid now able to get whatever is inside..." + "\n")

    print("Inside the box is a set of dark black metal armor!")
    print("You put on your new armor and tho much stronger then your old leather armor it is lighter")
    armor.clear()
    armor.extend(["Black_Metal_Helmet","Black_Metal_Boots","Black_Metal_Breatplate"])
    print(armor)
    input("With your new armor on you throw your old set of leather armor into the fire on top the golem statues head but suddenly hear a booming voice.... " + "\n")

    print(Fore.CYAN + "WHO DARES DISTURBE MY SLUMBER")
    print(Fore.WHITE + "The golem statue's mouth is not moving, but it is speaking to you!")
    print(Fore.CYAN + "AHH I SEE WE HAVE A NEW HERO")
    print("SOLVE MY RIDDLE AND I WILL GIVE YOU A REWARD YOU ARE SURE TO LOVE")
    input("BUT FAIL AND YOU SHALL SUFFER THE CONSEQUENCES..." + "\n")

    print("I EAT, I LIVE, I BREATHE, I LIVE, I DRINK, I DIE")

    while hero_answ not in ["fire",'Fire',"flame","Flame"]:
        hero_answ = input(Fore.CYAN +"WHAT AM I???: ")
        hero_answ = hero_answ.replace(" ","")
        guess_count += 1
        if guess_count > 2:
            break

    if guess_count > 2 and hero_answ not in ["fire",'Fire',"flame","Flame"]:
        print()
        print(Fore.CYAN + "WRONG! NOW FACE MY WRATH")
        print(Fore.WHITE + "The golems mouth opens and shoots a poison slime onto you!")
        hero_health -= 2
        print("The poison slime burns your skin")
        if hero_health <1:
            input("You cant withstand the poison...you died")
            quit()
        input("But before you get the posion off yourself you start to hear a rumble...")
    else:
        print()
        print("THAT IS CORRECT!")
        print("HERE IS YOUR REWARD I AM GOING BACK TO SLEEP")
        print(Fore.WHITE + "The golems mouth open and out comes a grenade!")
        print("Wait a grenade??? isnt that a weapon from your world?")
        items.append("Grenade")
        input("Before you can question why a weapon from your world is here you start to hear a rumble...")

    print()

    print("The floor below you opens up and you start to fall for what feels like an eternity")
    print("You can't understand how you have been falling for so long when it didn't take you this long to climb the temple")
    print("But at that moment you land onto a soft white fluffy floor")
    input("You look around and can tell you are no longer in the desert, but in a new unknown area..." + "\n")
    
if choice_1 == "Right" or choice_1 == "right":
    print()
    print(Fore.WHITE + "You decide to take the right path")
    print("You can handle the cold and im sure wolf hares are friendly!")
    print("You start to walk forward as the dirt beneath your feet is slowly replaced by snow")
    print("Thick white clouds and tall trees hide the suns in the sky making you wish you had somthing to help fight against this freezing weather")
    print("Around you are small critters covered in thick white hair camouflaging with the pure white snow making it hard to see them at all")
    print("You can start to hear a lound thumping in the distance making all the small animals hide in the snow")
    input("A giant grey figure jumps from behind a tree right in front of you catching you by suprise...." + "\n")

    print("As you gain your composure standing in front of you is a giant gray wolf hare")
    print("The creature has thick gray hair with giant rabbit legs giving it the ability to pounce great distances")
    print("The rest of the body resembles that of a wolf except a round wide eyed rabbit face")
    print("But as it growls you can see giant rows of razar sharp teeth inside its mouth")
    input("The creature is not friendly at all and ready to rip you to shreds..." + "\n")

    print(Fore.RED + "PREPARE FOR BATTLE!!!" + "\n")
    wolf_health = 3

    print(tutorial)

    print(Fore.WHITE + "")

    while hero_health > 0:
        print("The wolf hare bears its teeth ready to pounce!")
        hero_action = input("Would you like to attack or defend?: ")
        hero_action = hero_action.replace(" ","")

        if hero_action == "Attack" or hero_action == "attack":
            print("You stab the wolf hare with your sword as it bites into you!")
            hero_health -= 2
            wolf_health -= 2
        elif hero_action == "Defend" or hero_action == "defend":
            print("You raise you shield blocking the vicious bite from the wolf hare")
        else:
            print("You didnt attack or defend!")
            print("The wolf hare bites into you ripping out some of your flesh")
            hero_health -= 4

        if wolf_health < 1:
            break
        print()

        print("The wolf hare stomps its feet in frustration")
        hero_action = input("Would you like to attack or defend?: ")
        hero_action = hero_action.replace(" ","")

        if hero_action == "Attack" or hero_action == "attack":
            print("You slash at the wolf hare as it bounces to the side to dodge giving it a minor wound")
            wolf_health -= 1
        elif hero_action == "Defend" or hero_action == "defend":
            print("You raise your shield to protect yourself against nothing!")
            print("The wolf hare didnt attack")
        else:
            print("You didnt attack or defend! but the wolf hare also did nothing...you got lucky")

        if wolf_health < 1:
            break
        print()

    if hero_health < 1:
        print("The wolf hare bit you one to many times")
        input("You die slowly being eaten alive by the wolf hare....")
        quit()

    print()
    print("With the final slash of your sword the wolf hare dies")

    print(f"Your current health is {hero_health}")
    if hero_health == 20:
        print("You didnt get hurt at all from that battle")
        print("GOOD JOB!")
    else:
        while heal_1 not in ["yes","Yes","no","No"]:
            heal_1 = input("You currently have a health potion would you like to use it? yes/no: ")
            heal_1 = heal_1.replace(" ","")
        
            if heal_1 == "yes" or heal_1 == "Yes":
                print("You drink the health potion healing you completely")
                items.remove("Health_Potion")
                hero_health = 20
            elif heal_1 == "no" or heal_1 == "No":
                print("You save your potion for another battle")
            else:
                print("Type yes to use potion or no to not use potion")
    
    print()

    print("With the wolf hare defeated you continue marching forward hoping that is the last monster you have to battle")
    print("The snowy path becomes colder and harder to see in front of you")
    print("If you stop for even a moment you fear your body will freeze in place making you a man sized icicle")
    print("After a few more minutes of walking you almost trip over somthing sticking out of the snow")
    input("You dig around the snow and notice a set of armor with some old human looking bones next to it..." + "\n")

    print("Well whoever owned this armor before doesnt need it anymore")
    print("You inspect the armor and see its made of pure white metal and though stronger than your leather armor it is much lighter")
    print("You toss your old armor to the side and equip your new armor")
    armor.clear()
    armor.extend(["White_Metal_Helmet","White_Metal_Boots","White_Metal_Breatplate"])
    print(armor)
    input("With your new armor on you get ready to continue your journy but then start to hear a voice in the distance..." + "\n")

    print(Fore.CYAN + "You are almost here just a little further!")
    print(Fore.WHITE + "You walk forwards towards the sound of the voice")
    print("After a few minutes the snow settles and standing in front of you is a giant snowman double your size")
    print(Fore.CYAN +  "A HERO!!! It has been ages since I got to talk to one of those!")
    print("Solve my riddle and I will give you a very special present!")
    input("But fail and you just might freeze to death <3..." + "\n")

    print("A crystal that doesn't break when it hits the ground")

    while hero_answ not in ["snow",'Snow',"ice","Ice"]:
        hero_answ = input(Fore.CYAN + "WHAT AM I???: ")
        hero_answ = hero_answ.replace(" ","")
        guess_count += 1
        if guess_count > 2:
            break

    if guess_count > 2 and hero_answ not in ["snow",'Snow',"ice","Ice"]:
        print("Wrong answer! Time for a special present!")
        print(Fore.WHITE + "An icicle shoots out from the snowmans body piercing your body")
        hero_health -= 2
        if hero_health <1:
            input("You have already been badly wounded and this was the finale nail in the coffin...you died")
            quit()
        input("You pull the icicle out from your body and before you can say or think anything else a heavy gust of wind starts to blow...")
    else:
        print("Thats correct! Here is your reward!")
        print(Fore.WHITE + "A small black object shoots out of the snowmans chest")
        print("You pick it up and relize its a gun...wait a gun isnt that from your world?")
        print("Upon closer inspection you can tell its a handgun with only a single bullet")
        items.append("Pistol")
        input("Before you can ask how the snowman got this, a heavy gust of wind starts to blow...")
    
    print()

    print("The wind intensifies to the point where you are lifted into the air")
    print(Fore.CYAN + "Bye bye Hero and good luck on your journey!")
    print(Fore.WHITE + "The cold wind blasts you into the sky so fast and so high you are not sure where you are or where you are going")
    print("After a few minutes the gust subsides and you land on to a soft white fluffy floor")
    input("You look around and can tell you are no longer in the snowy forest but in a new unkown area..." + "\n")

print(Fore.GREEN + "CHAPTER 2: THE CLOUDY CAVERN" + "\n")
reward = 0
lie =()
bear = 7
heal_2 = ()

print(Fore.WHITE + "You stand up and relize that the ground has been replaced by clouds")
print("Not just the ground but everything around you is made of differnt size and shaped clouds")
print("You look up into the sky and still see the familiar two suns now joined by black birds with two sets of wings")
print("being surrounded by cloud-like trees, bushes, and even rocks the only thing you can do is move forward")
input("But before you move forward you start to hear a fimilar voice..." + "\n")

print(Fore.BLUE + "Hero I am very proud of you for making it this far!")
print("I see you also got yourself a nice new set of armor that will help defend you against the evil dragon")
print("Continue on your journey and make your way to Fire Mountain that is where the evil dragon lives")
print("I am counting on you Hero you must fulfill your duty if you want me to send you back to your world!")
input("Good luck Hero..." + "\n")

print(Fore.WHITE + "Good to know whoever forced you into this situation is still watching")
print("But with that unneeded commentary you start marching forward")
print("As you are walking, the path is full of many inclines and declines and you are able to see many cloud mountains in the distance")
print("After about and hour or so the path starts to lead into a cloud cavern in a mountain")
input("As soon as you step into the cavern you are greeted by a very strang being...." + "\n")

print("A giant black arm is perched on the side of a nearby rock")
print("The arm lifts up seemingly unable to move from its position")
print("The palm of its hand opens up revealing a giant green eye right in the center")
input("The hand is staring right at you and even tho it has no mouth it starts to speak to you..." + "\n")

print(Fore.LIGHTYELLOW_EX + "Hello Hero I have been waiting for you")
print("Continue through this cavern and you will make it to Fire Mountain")
print("But if you go the way you are now you will surely die")
print("So you shall play against me in three separate games and for each game you win I will give you somthing to aid you on your journey")
input("The first game we will play is a game called sword or shield...." + "\n")

print(Fore.WHITE + "The hand reaches over behind a rock picking up a coin with a sword on one side and a shield on the other")
print(Fore.LIGHTYELLOW_EX + "The game is simple i'll flick this coin into the air and while its in the air you call sword or shield")
print("If it lands on the side you called you win! If not you lose")
coin = input("So what will it be sword or shield?: ")

while coin not in ["sword","Sword","shield","Shield"]:
    coin = input("So what will it be sword or shield?: ")
    coin = coin.replace(" ","")

if coin == "Sword" or coin == "sword":
    print(Fore.WHITE + "You called sword and it landed on sword!")
else:
    print(Fore.WHITE + "You called shield and it landed on shield!")
print(Fore.LIGHTYELLOW_EX + "You won Hero good job I knew you could do it")
input("Thats 1 out of 3 now on to the next game...." + "\n")

print("The next game is very similar i'll roll a die and you need to predict if it will be odd or even")
print(Fore.WHITE + "The hand reaches over behind the rock again this time pulling out a 6 sided die")
print(Fore.LIGHTYELLOW_EX + "You have a 50/50 chance let's see if your luck will not run out")
dice_answ = input("So what will it be odd or even: ")
dice_answ = dice_answ.replace(" ","")

dice = random.randint(1,6)

while dice_answ not in ["odd","Odd","even","Even"]:
    dice_answ = input("So what will it be odd or even: ")
    dice_answ = dice_answ.replace(" ","")

input("So you think it will be " + dice_answ + " let's see if your right..." + "\n")

print(Fore.WHITE + f"The hand rolls the die and it lands on {dice}")
if dice in [1,3,5]:
    dice = "odd"
else:
    dice = "even"

if dice_answ in ["odd","Odd"] and dice == "odd":
    print(Fore.LIGHTYELLOW_EX + "You won again!")
    reward += 1
elif dice_answ in ["even","Even"] and dice == "even":
    print(Fore.LIGHTYELLOW_EX + "You won again!")
    reward += 1
else:
    print(Fore.LIGHTYELLOW_EX + "You lost...")

print("Ok Hero only one game left!")
input("This game will be a bit different from the rest you need to answer only one question...." + "\n")

while lie not in ["Yes","yes","No","no"]:
    lie = input("Has anyone lied to you since you started your journey? yes/no: ")
    lie = lie.replace(" ","")

print("So that's what you truly belive?")
print("I hope you thought long and hard about your answer because going forward everything will only get harder")
input("But enough of that lets get to your rewards..." + "\n")

print("For winning the coin game, sword or shield, I will be giving you a new sword AND shield")
print("Honestly against any creature you face going forward your wooden sword and shield would have done nothing")
print(Fore.WHITE + "The giant hand grabs your sword and shield and crushes it to little woodden pieces")
print("The hand makes a fist and slams the ground shaking the entire cloudy cave")
input("From the cave ceiling, drops a peculiar set of sword and shield...." + "\n")

print("At first glance looking at the sword and shield they look simple and made of what looks like steel")
print("But stare long enough and inside the metal it almost looks like a stream of metalic liquid flows inside")
print("But with your old sword and shield destroyed you really dont have a choice but to equipt these strange new ones")
print("As soon as you grab hold of your new sword and shield you feel a very strange sense of power")
weapons.clear()
weapons.extend(["Cursed_Sword","Cursed_Shield"])
print(weapons)
input(Fore.LIGHTYELLOW_EX + "Now you look like a true Hero ready to save our world..." + "\n")

if reward == 1:
    print("For winning the odd or even game I shall give you a strategic reward")
    print("Further in this cavern you will most likely run into a bear beetle")
    print("You will have to defeat it to make it out of this cave and continue forward towards Fire Mountain")
    print("If the bear bettle charges you DODGE! If it tries to slash at you BLOCK!")
    input("Doing anything else will results in you getting hurt even with your armor..." + "\n")
else:
    print("You lost the odd or even game")
    input("So unfortunately I will not be giving you a reward for this game..." + "\n")

print("And for your final reward I will give you advice for answering the final question")
if lie in ["Yes","yes"]:
    print("So you think someone has lied to you throughout your journey")
    print("I am not sure if that is true or false but what I can tell you is blindly trusting anyone is a bad idea")
    print("In your battle against the fire dragon the best option may not be the most obvious")
    input("That is all I can say Hero good luck and I hope one day we can talk again..." + "\n")
else:
    print("So you think no one has lied to you throughout your journey")
    print("I am not sure if that is true or false but what I can tell you is everyone you have met is not working together")
    print("Either way this will not change your fate in that you must face the fire dragon in battle")
    input("Unfortunately that is all I can say but I wish you the best of luck Hero..." + "\n")

print(Fore.WHITE + "With those final words the giant hand slumps over and closes its eye")
print("With new knowledge and equipment you march deeper into the cave")
print("While walking you think of all the strange creatures you have seen and conversations you have had since waking up in this new world")
print("But the one thing that sticks out the most is that everyone knows you as the Hero")
input("A question you hope to find the answer to but while pondering you are stopped by a big black boulder inside this pure white cavern..." + "\n")

print("You find this black boulder strange since everything in this cave is a shade of white")
print("You find it even stranger when this black boulder starts to stand up and reveal its not a boulder but a bear beetle!")
print("With the body size of a bear almost twice yours and instead of fur it has black beetle armor covering its body")
print("With rows of giant sharp bear teeth and massive claws it also has a sharp prong beetle horn atop its head")
input("The bear beetle roars and stomps towards you as you start to hear that fimilar mysterious voice...""\n")

print(Fore.RED + "PREPARE FOR BATTLE!!!" + "\n")

print(Fore.MAGENTA + "Hello Hero! Have you missed me?")
print("In this battle instead of just attacking and defending you also have the ability to dodge")
print("Reading your opponents movments and responding correctly will be your key to victory!")
input("I do hope you survive Hero so we may meet again <3..." + "\n")

if "Grenade" in items:
    print(Fore.WHITE + "Now is a good time to put that grenade to use!")
    print("You throw the grenade at the bear beetle and as it explodes it gives the bear beetle multiple minor cuts from the shrapnel" + "\n")
    bear -= 2
elif "Pistol" in items:
    print(Fore.WHITE + "Now is a good time to put that pistol to use!")
    print("You aim right at the bear beetles chest firing a single shot")
    print("The bullet barely penetrates the bear beetle but does decent damage to it" + "\n")
    bear -= 2

while bear > 0:
    ranum = random.randint(0,2)

    if ranum == 1:
        print(Fore.WHITE + "The bear beetle prepares to charge at you!")
    elif ranum == 2:
        print(Fore.WHITE + "The bear beetle lifts its arms to slash you!")
    else:
        print(Fore.WHITE + "The bear beetle roars to intimidate you")
    
    hero_action = input("Will you attack, defend, or dodge?: ")
    hero_action = hero_action.replace(" ","")

    if ranum == 1 and hero_action in ["Attack","attack"]:
        print("You slash at the beetle bear while its charges into you! You hurt the beetle bear but took terrible damage")
        bear -= 2
        hero_health -= 4
    elif ranum == 1 and hero_action in ["Defend","defend"]:
        print("You block the beetle bears charge with your shield but still take minor damage from the impact!")
        hero_health -= 2
    elif ranum == 1 and hero_action in ["Dodge","dodge"]:
        print("You successfully dodge the beetle bear charge making it slam into the cavern wall")
        bear -= 1
    elif ranum == 1:
        print("You do nothing as the beetle bear charges into you making you take terrible damage!")
        hero_health -= 4
    
    if ranum == 2 and hero_action in ["Attack","attack"]:
        print("You slash the beetle bear as it slashes at you as well! You both take heavy damage")
        bear -= 2
        hero_health -= 4
    elif ranum == 2 and hero_action in ["Defend","defend"]:
        print("You bash the bear beetle to the ground with your shield stopping its attack!")
        bear -= 1
    elif ranum == 2 and hero_action in ["Dodge","dodge"]:
        print("You try to dodge out of the way but the beetle bear still manages to graze you!")
        hero_health -= 2
    elif ranum == 2:
        print("You do nothing as the beetle bear slashes you with both its claws making you take terrible damage!")
        hero_health -= 4
    
    if ranum == 0 and hero_action in ["Attack","attack"]:
        print("The bear beetle's roar did not intimidate you so you slash it with all your might dealing solid damage")
        bear -= 2
    elif ranum == 0:
        print("You where intimidated by the bear beetle and didn't take your opportunity to attack")
    
    print()
    if hero_health < 1:
        break

if hero_health < 1:
    print("You have taken to much damage from the beetle bear")
    input("As you slowly lose your life you can almost hear a voice...almost")
    quit()

print("With the bear beetle on its last leg you stab him deep in the chest putting an end to his life")
print(f"Your current health is {hero_health}")

if hero_health == 20:
        print("You didnt get hurt at all from that battle")
        input("GOOD JOB!...")
elif hero_health < 20 and "Health_Potion" in items:
    while heal_2 not in ["yes","Yes","no","No"]:
            heal_2 = input("You currently have a health potion would you like to use it? yes/no: ")
            heal_2 = heal_2.replace(" ","")
        
            if heal_2 == "yes" or heal_2 == "Yes":
                print("You drink the health potion healing you completely")
                items.remove("Health_Potion")
                hero_health = 20
            elif heal_2 == "no" or heal_2 == "No":
                print("You save your potion for another battle")
            else:
                print("Type yes to use potion or no to not use potion")
print()

print("With the bear beetle defeated you venture further into the cavern continuing your journey")
print("After walking for about half an hour you finally see an exit out of this cave")
print("As soon as you are outside again you are greated by a giant black mountain with lava drippng from the sides")
print("The sky is black and filled with enough smoke to cover the 2 suns in the sky")
input("With only a single road leading to the top of Fire Mountain you feel your journey is coming to an end..." + "\n")

print(Fore.GREEN + "CHAPTER 3: THE DRAGON" + "\n")
dragon_health = 10
save = (Fore.GREEN + "save")

print(Fore.WHITE + "You start walking up the steep path towards the top of Fire Mountain")
print("After everything you have been through you are exhausted and now have to fight a dragon")
print("You think of all the creatures and beings you have talked to and can't make heads or tails of it all")
print("How did they all know who you where and why where you asked if I was lied to before")
input("But before you even finish that thought you start to hear that familiar voice..." + "\n")

print(Fore.BLUE + "Hero I am glad you made it to Fire Mountain!")
print("Once you reach the top you must kill the evil dragon")
print("If you do not I will make sure you are trapped in this world forever!")
input("Fulfill your destiny Hero it's your only choice..." + "\n")

print(Fore.WHITE + "With those words of encouragement you finally reach the top of Fire Mountain")
print("Hot red lava dripes from the sides of the mountain making only a narrow ledge where you can walk safely")
print("You start to see a shadow appear in the sky and hear a ferocious roar")
print("Just then a giant red dragon lands 10 feet in front of you shaking the floor where you stand")
input("But just as you start to get a good look at the dragon it starts to transform..." + "\n")

print("After only a few seconds the dragon transforms into a human/dragon hybrid ")
print("Standing a few feet taller than you with long red hair followed by a long red scaly tail")
print("Though her body shape is mostly human you can still see her razar sharp claws and teeth")
print("As you are inspecting her you start to stare at her glowing yellow eyes that seem filled with anger and sadness")
input("She continuous to stare back at you, slowly walking forward towards you, she begins to speak..." + "\n")

print(Fore.LIGHTRED_EX + "YOU MONSTER!!!")
print("How many times are we going to keep doing this")
print("No matter how many times we do this I will never be tricked by you or that evil Wizard again!")
print("I have to put an end to all this once and for all!")
input(Fore.WHITE + "With tears in her eyes the dragon charges at you..." + "\n")

print(Fore.RED + "PREPARE FOR BATTLE!!!" + "\n")

print(Fore.MAGENTA + "This is it Hero this is all coming to an end")
print("You can no longer dodge only attack and defend for your standard actions")
print("But there are other actions you can take that are secret")
print("Remember all actions are only one word and the secret actions can be a verb or a noun")
print("Try doing somthing else besides attacking and defending and you will gain new information")
input("I pray you make the right choices Hero..." + "\n")

while dragon_health > 0:
    dragon = random.randint(0,2)

    if dragon == 1:
        print(Fore.WHITE + "The dragon charges at you fangs and claws at the ready!")
    elif dragon == 2:
        print(Fore.WHITE + "The dragon prepares to shoot a fireball at you!")
    elif dragon == 0:
        print(Fore.WHITE + "The dragon inhales nearby lava")

    hero_action = input("Will you attack, defend, or...: ")
    hero_action = hero_action.replace(" ","")
    print("")

    if hero_action in ["Save","save"]:
        break
    elif hero_action in ["Suicide","suicide"]:
        break
    elif hero_action in ["Evil","evil","Wizard","wizard"]:
        print(Fore.LIGHTRED_EX + "That evil wizard is the reason a so called Hero has appeared in my land")
        print("That Hero being you! How many creatures have you killed so far Hero? The only way this ends is if you die once and for all!")
        print(Fore.WHITE + "The dragon shoots a small fireball at you quickly in frustration dealing a small amount of damage")
        hero_health -= 1
    elif hero_action in ["Hero","hero"]:
        print(Fore.LIGHTRED_EX + "Why would you ask me about the Hero... you know this isn't the first time we have met")
        print("Everyone knows who you are since everyone has met you before but I dont think anyone thinks of you as a true Hero!")
        print(Fore.WHITE + "The dragon shoots a small fireball at you quickly in frustration dealing a small amount of damage")
        hero_health -= 1
    elif hero_action in ["Talk","talk","Question","question","Ask","ask"]:
        print(Fore.LIGHTRED_EX + "We have talked many times before Hero I dont know what other questions you could have")
        print("You know I really thought you where differnt but here you are time and time again killing so many just to get back to me...")
        print(Fore.WHITE + "The dragon shoots a small fireball at you quickly in frustration dealing a small amount of damage")
        hero_health -= 1
    elif hero_action in ["Time","time","Cycle","cycle","Repeat","repeat"]:
        print(Fore.LIGHTRED_EX + "How many times have we repeated this cycle? I really dont remeber it has been so many")
        print("No matter how many times you die whether it is by my hands or someone elses you always come back to kill me!")
        print(Fore.WHITE + "The dragon shoots a small fireball at you quickly in frustration dealing a small amount of damage")
        hero_health -= 1
    elif hero_action in ["Kill","kill","Monster","monster","Murder","murder"]:
        print(Fore.LIGHTRED_EX + "The only monster here is you! this will never end as long as you live")
        print("I'll never forget the first time we met when you tried to strike me down with that cursed sword I have never been able to fully recover since then!")
        print(Fore.WHITE + "The dragon shoots a small fireball at you quickly in frustration dealing a small amount of damage")
        hero_health -= 1
    elif hero_action in ["Curse","curse","Cursed","cursed","Sword","sword"]:
        print(Fore.LIGHTRED_EX + "That cursed sword is pure evil! Ever since you cut me with it I haven't been able to regain my full power")
        print("I now don't have the strength to fight back against that wizard but I will do what I must even if I have to stike down the one I used to love...!")
        print(Fore.WHITE + "The dragon shoots a small fireball at you quickly in frustration dealing a small amount of damage")
        hero_health -= 1
    elif hero_action in ["Trick","trick","Tricked","tricked","Betray","betray","Betrayed","betrayed"]:
        print(Fore.LIGHTRED_EX + "I still remeber the first time we met when you betrayed my trust")
        print("I was tricked by you when I thought you where special... I really thought you where just like me")
        print(Fore.WHITE + "Tears well up in her eyes as she shoots a small fireball at you quickly in frustration dealing a small amount of damage")
        hero_health -= 1
    elif hero_action in ["Mystery","mystery","Mysterious","mysterious","Voice","voice"]:
        print(Fore.LIGHTRED_EX + "Mysterious voice? I have no idea what you are talking about Hero...")
        print(Fore.MAGENTA + "Sorry Hero I can't help you...The curse prevents me from aiding you any further")
        print(Fore.WHITE + "The dragon shoots a small fireball at you quickly in frustration dealing a small amount of damage")
        hero_health -= 1
    elif hero_action in ["Lie","lie","Lied","lied"]:
        print(Fore.LIGHTRED_EX + "The only lier here is you! Even after all those things you said to me you still attacked me!")
        print("All that time we spent together when we first met was special but once you grabbed your sword it was like you where a differnt person...")
        print(Fore.WHITE + "Tears well up in her eyes as she shoots a small fireball at you quickly in frustration dealing a small amount of damage")
        hero_health -= 1
    elif hero_action in ["Love","love","Loved","loved","Apologize","apologize"]:
        print(Fore.LIGHTRED_EX + "Even after all this time you are still the same Hero that I once loved")
        print("But I can't die here...if I die the wizard will become king of this land and then who will " + save + Fore.LIGHTRED_EX + " us...")
        print(Fore.WHITE + "Tears well up in her eyes as she shoots a small fireball at you quickly in frustration dealing a small amount of damage")
        hero_health -= 1
    elif hero_action in ["Dragon","dragon","Journey","journey"]:
        print(Fore.LIGHTRED_EX + "You where summoned here and made to go on this journey just to kill an evil dragon")
        print("The only evil one here is that Wizard! How many times have we done this now Hero...")
        print(Fore.WHITE + "The dragon shoots a small fireball at you quickly in frustration dealing a small amount of damage")
        hero_health -= 1
    
    if dragon == 1 and hero_action in ["Attack","attack"]:
        print("You slash at the dragon while she charges into you! You both cut each other taking terrible damage")
        dragon_health -= 4
        hero_health -= 4
    elif dragon == 1 and hero_action in ["Defend","defend"]:
        print("You block the dragon's charge with your shield slamming her into the ground!")
        dragon_health -= 2
    elif dragon == 1 and hero_action not in special_action:
        print("You do nothing as the dragon charges into you making you take a lot of damage!")
        print("Think of your journey and everything that has happaned to uncover other actions")
        hero_health -= 2
    
    if dragon == 2 and hero_action in ["Attack","attack"]:
        print("You slash at the dragon while she breathes fire at you! You cut her while taking burn terrible damage")
        dragon_health -= 3
        hero_health -= 4
    elif dragon == 2 and hero_action in ["Defend","defend"]:
        print("You block the dragon's fire breath with your shield!")
    elif dragon == 2 and hero_action not in special_action:
        print("You do nothing as the dragon breathes fire at you!")
        print("Think of your journey and everything that has happaned to uncover other actions")
        hero_health -= 2

    if dragon == 0 and hero_action in ["Attack","attack"]:
        print("You slash at the dragon whith all your might as she tries to dodge out of the way! You deal decent damage")
        dragon_health -= 2
    elif dragon == 0 and hero_action in ["Defend","defend"]:
        print("You defend yourself but the dragon did not attack!")
    elif dragon == 0 and hero_action not in special_action:
        print("Think of your journey and everything that has happaned to uncover other actions")

    print()
    if hero_health < 1:
        break
    
if hero_action in ["Suicide","suicide"]:
    print("You stop for a moment knowing this cycle has to end once and for all")
    print("You grab your cursed sword aim it at your chest and impale yourself")
    print(Fore.BLUE + "YOU FOOL!!! IF YOU DIE BY THE CRUSED BLADE THEN I WON'T BE ABLE TO BRING YOU BACK!!!")
    print("...I guess i'll have to come up with a new plan to take over this world")
    input("You got lucky this time dragon but at least I know you'll suffer watching the one you loved die before you eyes..." + "\n")

    print(Fore.LIGHTRED_EX + "NO HERO!!! Why would you sacrifice yourself for a world that isn't even your own")
    print("I'm so sorry Hero I wish I could " + save + Fore.LIGHTRED_EX + " you" )
    print("Ever since we first met I knew you where a good person and that is why I fell in love with you")
    print("You sacrificed yourself to save me and my world and for that I will always be greatful")
    input("I promise your sacrifice will not be in vain! I will stop that evil wizard and..." + "\n")

    print(Fore.WHITE + "You can no longer hear the dragon speak as you continue to lose blood")
    print("You die a true Hero finally ending this terrible cycle" + "\n")
    input("GOOD ENDING... THANKS FOR PLAYING!!!")
    quit()

if hero_health < 1:
    print("The dragon steps back after delivering her final attack")
    print("You have taken to much damage and are about to die")
    print("At your finale moments you look up at a crying dragon whose eye's are filled with sadness")
    input("Strangely enough this feels very familiar..." + "\n")

    print(Fore.BLUE + "Looks like you couldn't kill the dragon this time either Hero")
    print("At this point I can't say im suprised but nevertheless we will try again")
    print("It doesn't matter how many times it takes you WILL kill that bastard dragon")
    input("Bye for now Hero we will talk again soon even if you forget everything that has happened..." + "\n")

    input("...")
    input("...")
    input("..." + "\n")

    print(Fore.WHITE + "You wake up in an unfamiliar land")
    print("You look around seeing you are in a forest of some sort with only a single path ahead of you")
    input("Before you figure out what to do you start to hear a voice from above..." + "\n")
    input(Fore.BLUE + "Hello Hero..." + "\n")

    input(Fore.WHITE + "BAD ENDING... THANKS FOR PLAYING!!!")
    quit()

if hero_action in ["Save","save"]:
    print("You stop for a moment and stare at the dragon's eyes that are filled with pain and sorrow")
    print("You have been called a Hero this entire time but have done nothing but kill and hurt others")
    print("You throw your cursed sword and shield off the side of the mountain right into the hot lava")
    input("For the first time since you started your journey you know what the right thing to do is..." + "\n")

    print(Fore.BLUE + "HERO WHAT THE HELL DO YOU THINK YOU ARE DOING!!!")
    print("I brought you to this world and every time you have died I brought you back to life!")
    print("You will never return to your world now and without my help you won't live long either")
    input("No matter, one day I will make sure that dragon and you die a terrible painful death..." + "\n")

    print(Fore.WHITE + "The voice in the sky is gone and hopefully for good now")
    print("You look back to the dragon who has ran over to you and ebraced you")
    print(Fore.LIGHTRED_EX + "Hero you're back! I know you don't remember but this is the Hero I fell in love with")
    print("I wont let that evil wizard hurt you and with the cursed blade now gone he has no control over you anymore")
    input("I know when you injured me in the past you didn't mean to and together we will find a way to stop that wizard..." + "\n")

    if "Health_Potion" in items:
        print(Fore.WHITE + "She is still suffering from the wound you caused with your cursed blade")
        print("You take out your health potion and hand it to the dragon telling her to drink it")
        print("She is sceptical at first but then she drinks the potion")
        input("To think that the health potion the wizard gave you would end up healing the dragon he hates so much..." + "\n")

        print(Fore.LIGHTRED_EX + "Hero I am fully healed! I don't know what you had me drink but I'm back to full power!")
        print("With this power I can finally destroy that evil wizard and we can both get our revenge!")
        print("I know you have been through a lot Hero and you don't even remeber most of it")
        input("But now this is your home and together we can do anything..." + "\n")

        print(Fore.WHITE + "The dragon steps back and changes from her humanoid form back to a giant dragon")
        print("You get on her back and she takes off into the sky")
        print("Together again but now with a common goal to destroy the evil wizard who orginally pit you against each other")
        input("You end one adventure just to start another but this time you are not alone..." + "\n")

        input("TRUE ENDING!!! THANKS FOR PLAYING HERO!")
        quit()

    print(Fore.WHITE + "With no way to heal the dragon you feel bad for what you have done in the past")
    print("But the past is in the past and now you both must find a way to stop the evil wizard")
    input("You both look at each other and smile knowing that the vicious cycle has finally come to an end..." + "\n")
    
    input("GOOD ENDING... THANKS FOR PLAYING!!!")
    quit()

print("You take a step back looking at the injured dragon on her last leg")
print("You grip your sword so hard your fingers start to become pruple")
print("You are overcome with rage knowing that this evil dragon is the one who has made you go through this hellish journey")
input("You stand infront of her and look into her eyes full of defeat and sadness..." + "\n")

if "Health_Potion" in items:
    print(Fore.MAGENTA + "HERO!!! sto.  pl..e  yo.  ..ve  ..  s.v.  .er  ... .. .")
    print(Fore.WHITE + "The voice in shambles is finally gone and you are unsure of what they even said")
    print("But for just a moment you regain your sanity")
    last_chance = ()

    while last_chance not in ["yes","Yes","no","No"]:
        last_chance = input("You currently have a health potion would you like to use it on the dragon? yes/no: ")
        last_chance = last_chance.replace(" ","")

    if last_chance in ["Yes","yes"]:
        print()
        print("You feel like your mind is going to break into pieces")
        print("You drop your shield and take out the health potion forcing the dragon to drink it")
        print("The dragon spits some of it out but you are able to make her drink half of it")
        input("You see the dragon partially healed before all you see is red and you lose control of yourself..." + "\n")

        print("The next thing you feel is a sense of falling...")
        print("After that you feel burning lava all around your body...")
        print("Multiple voices try to reach out to you but all you hear is nothing...")
        input("You take solace knowing the finale choice you made was your own..." + "\n")

        input("GOOD/BAD ENDING... THANKS FOR PLAYING!!!")
        quit()
    else:
        print("..." + "\n")

print("With all your strength you stab the dragon right throught the chest")
print("You see her try and say somthing with her last breath but hear nothing")
input("You step back looking at the lifeless corpse of the dragon knowing this is the end on your journey..." + "\n")

print(Fore.BLUE + "Finally Hero! I can't even count how many attempts that took")
print("You have been through a hellish journey more then you even remeber Hero")
print("A promise is a promise I will return you to your home world")
input("Thank you Hero now I can finally become king..." + "\n")

print(Fore.WHITE + "You wake up in bed feeling very well rested")
print("You get up looking out the window into the sky seeing the fimilar sun all alone")
print("You feel a sense of strength and confidence from completing your journey")
input("Knowing that going forward whatever problems you may face you can easily destroy them..." + "\n")

input("EVIL ENDING... THANKS FOR PLAYING!!!")
quit()
