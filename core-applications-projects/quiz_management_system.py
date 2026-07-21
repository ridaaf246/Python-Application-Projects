questions = []

while True:
    print("Quiz Management System")
    print("1. Add Question")
    print("2. View Questions")
    print("3. Take Quiz")
    print("4. Delete Question")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        question = input("Enter Question: ")
        a = input("Option A: ")
        b = input("Option B: ")
        c = input("Option C: ")
        d = input("Option D: ")
        answer = input("Correct Answer (A/B/C/D): ").upper()

        data = {
            "question": question,
            "A": a,
            "B": b,
            "C": c,
            "D": d,
            "answer": answer
        }

        questions.append(data)

        print("Question added successfully.")

    elif choice == "2":
        if len(questions) == 0:
            print("No questions available.")

        else:
            for i in range(len(questions)):
                print("Question", i + 1)
                print(questions[i]["question"])
                print("A.", questions[i]["A"])
                print("B.", questions[i]["B"])
                print("C.", questions[i]["C"])
                print("D.", questions[i]["D"])
                print("Answer:", questions[i]["answer"])
                print()

    elif choice == "3":
        if len(questions) == 0:
            print("No questions available.")

        else:
            score = 0

            for i in range(len(questions)):
                print("Question", i + 1)
                print(questions[i]["question"])
                print("A.", questions[i]["A"])
                print("B.", questions[i]["B"])
                print("C.", questions[i]["C"])
                print("D.", questions[i]["D"])

                ans = input("Your Answer: ").upper()

                if ans == questions[i]["answer"]:
                    print("Correct")
                    score = score + 1

                else:
                    print("Wrong")
                    print("Correct Answer:", questions[i]["answer"])

            print("Your Score:", score, "/", len(questions))

    elif choice == "4":
        if len(questions) == 0:
            print("No questions available.")

        else:
            for i in range(len(questions)):
                print(i + 1, questions[i]["question"])

            num = int(input("Enter question number to delete: "))

            if num >= 1 and num <= len(questions):
                questions.pop(num - 1)
                print("Question deleted.")

            else:
                print("Invalid question number.")

    elif choice == "5":
        print("Thank you for using Quiz Management System.")
        break

    else:
        print("Invalid choice.")