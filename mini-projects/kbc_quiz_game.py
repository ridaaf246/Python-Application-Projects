print("welcome to kon bane ga crorepati")

print("Question no.01\n1. International Literacy Day is observed on: ")
print("A. sep 8         B. nov 28\nC. may 2         D. sep 22")
answer = input("Choose answer: ").lower()

money1 = [10000, 20000, 30000, 40000, 50000]

if answer == "b":
    print("Congratulations! Correct answer")
    print("You won", money1[0])
else:
    print("Sorry! You choose wrong answer")



print("WELCOME TO \"KON BANEGA CAROEPATI!\"")

question = [
"1. International Literacy Day is observed on:",
"2. The language of Lakshadweep, a Union Territory of India, is",
"3. In which group of places the Kumbha Mela is held every twelve years?",
"4. Bahubali festival is related to",
"5. Which day is observed as the World Standards Day?"
]

options = [
"A. Sep 8     B. Nov 28     C. May 2     D. Sep 22",
"A. Tamil     B. Hindi     C. Malayalam     D. Telugu",
"A. Ujjain, Puri, Prayag, Haridwar     B. Prayag, Haridwar, Ujjain, Nasik     C. Rameshwaram, Puri, Badrinath, Dwarika     D. Chittakoot, Ujjain, Prayag, Haridwar",
"A. Islam     B. Hinduism     C. Buddhism     D. Jainism",
"A. June 26     B. Oct 14     C. Nov 15     D. Dec 2"
]

answers = ["A", "C", "B", "D", "B"]

money = 0


print(question[0])
print(options[0])

user = input("Enter your answer: ").capitalize()

if answers[0] == user:
    money = money + 20000
    print("Congratulations, You gave the right answer")
    print("You have won:", money)
else:
    print("You choose the wrong option")
    money = money - 20000
    if money < 0:
        money = 0
    print("Your current prize is:", money)



print(question[1])
print(options[1])

user = input("Enter your answer: ").capitalize()

if answers[1] == user:
    money = money + 20000
    print("Congratulations, You gave the right answer")
    print("You have won:", money)
else:
    print("You choose the wrong option")
    money = money - 20000
    if money < 0:
        money = 0
    print("Your current prize is:", money)



print(question[2])
print(options[2])

user = input("Enter your answer: ").capitalize()

if answers[2] == user:
    money = money + 20000
    print("Congratulations, You gave the right answer")
    print("You have won:", money)
else:
    print("You choose the wrong option")
    money = money - 20000
    if money < 0:
        money = 0
    print("Your current prize is:", money)



print(question[3])
print(options[3])

user = input("Enter your answer: ").capitalize()

if answers[3] == user:
    money = money + 20000
    print("Congratulations, You gave the right answer")
    print("You have won:", money)
else:
    print("You choose the wrong option")
    money = money - 20000
    if money < 0:
        money = 0
    print("Your current prize is:", money)



print(question[4])
print(options[4])

user = input("Enter your final answer: ").capitalize()

if answers[4] == user:
    money = money + 20000
    print("🎉 FINAL QUESTION ANSWERED CORRECTLY!")
    print("Amazing! You completed the last question.")
    print("Your final winning amount is:", money)
else:
    print("Oh no! You gave the final question wrong.")
    money = money - 20000
    if money < 0:
        money = 0
    print("Your final winning amount is:", money)




print(" FINAL RESULT ")

print("Total amount won:", money)


if money >= 60000:
    print("WOW! 🎉")
    print("You really played amazingly!")
    print("You won a great prize. Congratulations on your excellent performance!")

elif money >= 20000 and money <= 40000:
    print("Good job! 😊")
    print("You did better than doing nothing.")
    print("You still managed to win a nice prize. Keep improving!")

else:
    print("Better luck next time! 😊")
    print("Don't lose hope. I hope you will win a bigger prize in your next game!")


print("Thank you for playing Kon Banega Crorepati!")