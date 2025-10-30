print("guess the number between 0 to 100")

choice=5


import random
num=random.randint(0,100)
while choice>0:
    print()
    print(" you have only {} guess".format(choice))
    print()
    guess=int(input("Enter the number:"))
    if num==guess:
        print()
        print(" ********** you won **************")
        break
    elif num>guess:
        print()
        print("Too low Guess higher")
        print("-------------------------")
    elif num<guess:
        print("Too high Guess lesser")
        print("-------------------------")
    choice-=1

if choice==0:
    print("you lose")
    
    print()
    
    print("The answer is {}".formate(num))
    
    print()
    
    print("Better luck Next time...")

