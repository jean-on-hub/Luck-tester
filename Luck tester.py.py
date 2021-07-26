from random import randint
#variables assignment
num_rounds = 0
num_wins = 0
validation =5
#game choice
while validation == 5:
    print("Welcome to the luck tester")
    game = input("Enter c to choose the coin game or d to choose the dice game ")
    while (game != "c" and game != "d"):
            input("it must either be c or d ")
    if game == "c":
        print("you chose the coin game")
        validation = 0
    elif game == "d":
        print("you chose the dice game")
        validation = 1
    else:
        print("it must either be heads or tails")

while validation == 0:
    #making the coin game
    print("Welcome to the coin flip game")
    #user choice
    choice = input("Enter h to choose heads or t to choose tails ")
    if choice == "h":
        print("you chose heads")
    elif choice == "t":
        print("you chose tails")
    else:
        print("it must either be heads or tails")
        continue
        
    #coin flip
    result=randint(1,2)
    #
    if result == 1:
        print("The coin fell on its head")
    else:
        print("The coin fell on its tail")
    if choice == "h" and result == 1:
        print("you guessed right!")
        num_rounds +=1
        num_wins +=1
    elif choice == "t" and result == 2:
        print("you guessed right!")
        num_rounds +=1
        num_wins +=1
    else:
        print("you guessed wrongly, sorry")
        num_rounds +=1
        
    print("You have played "+ str(num_rounds)+ " games and won "+ str(num_wins))
    #play again request
    play_again = input("Do you want to play again? Enter y for yes and n for no ")
    print(play_again)
    while (play_again != "y" and play_again != "n"):
        input("it must either be yes or no ")
    if play_again == "y":
        continue
    elif play_again == "n":
        validation = 5
while validation == 1:
    print("Welcome to the dice game")
    #user choice
    choice = input("Enter a number from 1 to 6 to begin ")
    wrong_choice= False
    for n in range(1,7):
        if choice == str(n):
            wrong_choice = True
            break
    while wrong_choice == False:
        choice = input("It must be a number from 1 to 6")
    if choice == "1":
        print("you chose one")
    elif choice == "2":
        print("you chose two")
    elif choice == "3":
        print("you chose three")
    elif choice == "4":
        print("you chose four")
    elif choice == "5":
        print("you chose five")
    elif choice == "6":
        print("you chose six")
          
    #dice throw
    result=randint(1,6)
    #
    if str(result) == choice:
        print("you guessed correctly")
        num_rounds +=1
        num_wins +=1
    else:
        print("you guessed wrongly, sorry")
        num_rounds +=1
            
    print("You have played "+ str(num_rounds)+ " games and won "+ str(num_wins))
    #play again request
    play_again = input("Do you want to play again? Enter y for yes and n for no ")
    print(play_again)
    while (play_again != "y" and play_again != "n"):
        input("it must either be yes or no ")
    if play_again == "y":
        continue
    elif play_again == "n":
        validation = 5