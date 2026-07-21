def game():
    user = input("Rock, Paper, Scissor\nChoose one: ").lower()
    import random
    list = ["rock", "paper", "scissor"]
    computer= random.choice(list)
    if user =="rock" and computer == "rock":
      print("Draw")
    elif user == "rock" and computer == "paper":
      print("computer win")
    elif user == "rock" and computer == "scissor":
     print("You win")
    elif user == "paper" and computer == "rock":
     print("You win")
    elif user == "paper" and computer == "paper":
      print("Draw")
    elif user == "paper" and computer == "scissor":
      print("Computer win")
    elif user == "scissor" and computer == "rock":
     print("Computer win")
    elif user == "scissor" and computer == "paper":
     print("You win")
    else:
      print("Draw")

game ()

while True:
    a = input ("Wanna play again?\nPress 1 to Play\nPress 0 to Quit\n")
    if a == "1":
       game()
    elif a == "0":
        print("Thankyou for playing the game")
        break
    else:
        raise ValueError
