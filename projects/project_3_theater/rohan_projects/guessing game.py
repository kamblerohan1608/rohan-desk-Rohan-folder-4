import random

#print(dir(random))

#help(random)

a=random.randint(1,50)
#print (a)

print()
print("************************** WELCOME TO THE GUESS GAME *****************************")
print()
print("****************************** Rules of the game *********************************")
print()
print("1. You will have to guess a random number between 1 to 50. ")
print("2. There will be 5 chances provided to you. ")
print("3. Related hints will be given to you in each chance.")
print("4. Try to guess the number in as less chances as you can.")
print("5. Lesser number of chances used higher you will get score out of 10. ")
print()
print("Try it out...")
print()
print()
print('System has selected a number between 1 to 50 try to guess it....')
print()
print()

i=5
while i>=1:

    ch=int(input("Enter your guess : "))

    if ch == a:
        print()
        print("********************* Congratulations You Have Guessed Correctly **************************")
        print()
        break
    elif a in range(ch-5,ch+6):
        print()
        print(" Hint 1  :  You are in +5,-5 range of the number")
        if a in range(ch-5,ch):
            print()
            print("Hint 2  :  go a bit lower..........")
            print()
        else:
            print()
            print("Hint 2  :  go a bit higher..........")
            print()
    elif a in range (ch-10,ch+11):
        print()
        print("Hint 1  :  You are in +10,-10 range of the number")
        if a in range(ch-10,ch):
            print()
            print("Hint 2  :  go a bit lower..........")
            print()
        else:
            print()
            print("Hint 2  :  go a bit higher..........")
            print()
    elif ch > a+10:
        print()
        print("Hint :  Try going lower..........")
        print()
    elif ch < a-10:
        print()
        print("Hint :  Try going Higher..........")
        print()
    i-=1

score = i*2 
print("*******************************************************************************************")
print()
print()
print("  The number was : " + str(a))
print()
print()
print("  Your score is " + str(score)  )
print()
print()
