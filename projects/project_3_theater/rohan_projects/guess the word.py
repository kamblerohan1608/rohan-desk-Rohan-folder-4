
# guess word

import random


def word():
        
    ls =["motorcycle","ambulance","rikshaw","helicopter","facebook","instagram","whatsapp","telegram","twitter","earthquick","tornado","landslide","tsunami","volcano","peacock","sparrow","ostrich","penguin","woodpeaker","notebook","college","mathmatics","algebra","geography","jiraffe","elephant","kangaroo","gorilla","hourse","rabbit","fridge","microwave","keyboard","monitor","internet","windows","application","blackhole","neptune","jupitor","astroid","satellite","milkyway","hockey","badminton","filding","hattrick","batsman"]

    global sec_word
    sec_word = random.choice(ls)
    #print(sec_word)
    
    global word_range
    word_range = len(sec_word)
    #print(word_range)
    word_range -= 1
    i = 1
    global blank_position
    blank_position = []
    while i <= 3:
        empty_char = random.randint(0,word_range)
        if empty_char not in blank_position :
            blank_position.append(empty_char)
        if len(blank_position) == 3 :
            i += 3
    #print(blank_position)

    for j in range(0, word_range + 1):
        if j in blank_position:
            print("_",end = " ")
        else:
            print(sec_word[j],end = " ")
    print()




def hint_1():

    animal = ["giraffe","elephant","kangaroo","gorilla","hourse","rabbit"]
    house = ["fridge","microwave"]
    computer = ["keyboard","monitor","internet","windows","application"]
    space = ["blackhole","neptune","jupitor","astroid","satellite","milkyway"]
    sports = ["hockey","badminton","filding","hattrick","batsman"]
    study = ["notebook","college","mathmatics","algebra","geography"]
    bird = ["peacock","sparrow","ostrich","penguin","woodpeaker"]
    disaster = ["earthquick","tornado","landslide","tsunami","volcano"]
    social_media = ["facebook","instagram","whatsapp","telegram","twitter"]
    transportation = ["motorcycle","ambulance","rikshaw","helicopter"]
    
    if sec_word in animal:
        print()
        print("Hint : May be something which lives in wild...")
        print()
    elif sec_word in house:
        print()
        print("Hint : It is seen in houses...")
        print()
    elif sec_word in computer:
        print()
        print("Hint : Seams like it is related with computer stuff...")
        print()
    elif sec_word in space:
        print()
        print("Hint : Something related to the wonders of space...")
        print()
    elif sec_word in sports:
        print()
        print("Hint : It can be related with sports... ")
        print()
    elif sec_word in study:
        print()
        print("Hint : Has some relevence with study ...")
        print()
    elif sec_word in bird:
        print()
        print("Hint : Sort of a bird ...")
        print()
    elif sec_word in disaster:
        print()
        print("Hint : Causes distruction ...")
        print()
    elif sec_word in social_media:
        print()
        print("Hint : Are you socially active ...")
        print()
    elif sec_word in transportation:
        print()
        print("Hint : It transports people ...")
        print()

def hint_2():

    blank_position.pop()
    for j in range(0, word_range + 1):
        if j in blank_position:
            print("_",end = " ")
        else:
            print(sec_word[j],end = " ")
    print()




print()
print("************************** WELCOME TO THE GAME ********************************\n")
print("**************************** Guess The word ***********************************\n\n")
print("Rules of the game : \n")
print("You have to guess the incomplete word displayed.")
print("You will be provided with 3 chances.")
print("In each chance you can either guess or use hint.")
print("There are two hints available in your 3 chances.\n    1. Using first hint will -1 from your score")
print("    2. Using secound hint will -1 from your score as well as you will loose one life.")
print("According to the chances and hints used you will get the score")
print("\nLet's Start \n")
print()
word()
print()
print("Enter the guess or type hint to use hint...")
win = 0
hint_count = 0
turn = 3
while turn >= 1 :
    if hint_count == 0 or hint_count == 1:
        print()
        ch = input("Enter guess/hint :  ")
        print()

        if ch == "hint" or ch == "Hints" or ch == "HINTS":
            if hint_count == 0:
                print("The first hint is ....")
                hint_1()
                print()
                hint_count += 1
                turn += 1
            elif turn == 1 and hint_count == 1:
                print()
                print("Its your last chance.....\n\nCannot use secound hint as it costs one life, try guessing it rather.")
                print()
                turn += 1
            else:
                print("You loose one life.")
                print()
                print("You used hint one more letter is visible now ....")
                print()
                hint_2()
                
                hint_count += 1
                

        elif ch == sec_word :
            print()
            print("************** Hurrey... You Guessed it correct ***************")
            print()
            print("\n The word was  :  ",sec_word)
            print()
            win += 1
            break 

        else :
            print()
            print("\n ......Guess Incorrect......")
            print()


    else:
        print()
        print()
        ch = input("Enter guess :  ")
        print()
        if ch == sec_word :
            print()
            print("************** Hurrey... You Guessed it correct ***************")
            print()
            print("\n The word was  :  ",sec_word)
            print()
            win += 1
            break 

        
        elif ch == "hint" or ch == "Hint" or ch == "HINT":
            print('''
            No hints available...
            ''')
            turn += 1

        else :
            print()
            print("\n ......Guess Incorrect......")
            print()

    turn -= 1



if hint_count == 0 and win != 0:
    score = turn*3
    total = score + 1 
    print(f'''
    Your score is {score} and +1 for not using hints i.e {total}
    ''')
elif hint_count == 1 and win != 0:
    score = turn * 3
    total = score -1
    print(f'''
    Your score is {score} and -1 for using one hint i.e {total}
    ''')
elif hint_count == 2 and win != 0:
    score = turn * 3
    total = score -2
    print(f'''
    Your score is {score} and -2 for using both hints i.e {total}
    ''')

else :
    print()
    print()
    print("The word was : ",sec_word)
    print()
    print()
    print("****************** You loose the game *********************")
    print()
    print()
    print("************************************************************")
    print()








