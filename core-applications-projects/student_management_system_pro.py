students = []

while True:
    print("Student Management System Pro")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        id = input("Enter Student ID: ")

        found = False

        for s in students:
            if s["id"] == id:
                found = True
                break

        if found:
            print("Student ID already exists.")

        else:
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            course = input("Enter Course: ")
            marks = input("Enter Marks: ")

            data = {
                "id": id,
                "name": name,
                "age": age,
                "course": course,
                "marks": marks
            }

            students.append(data)

            print("Student added successfully.")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")

        else:
            for s in students:
                print("ID:", s["id"])
                print("Name:", s["name"])
                print("Age:", s["age"])
                print("Course:", s["course"])
                print("Marks:", s["marks"])
                print()

    elif choice == "3":
        id = input("Enter Student ID: ")

        found = False

        for s in students:
            if s["id"] == id:
                print("Student Found")
                print("ID:", s["id"])
                print("Name:", s["name"])
                print("Age:", s["age"])
                print("Course:", s["course"])
                print("Marks:", s["marks"])

                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice == "4":
        id = input("Enter Student ID to update: ")

        found = False

        for s in students:
            if s["id"] == id:
                s["name"] = input("Enter New Name: ")
                s["age"] = input("Enter New Age: ")
                s["course"] = input("Enter New Course: ")
                s["marks"] = input("Enter New Marks: ")

                print("Student record updated.")

                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice == "5":
        id = input("Enter Student ID to delete: ")

        found = False

        for s in students:
            if s["id"] == id:
                students.remove(s)

                print("Student record deleted.")

                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice == "6":
        print("Thank you for using Student Management System Pro.")
        break

    else:
        print("Invalid choice.")