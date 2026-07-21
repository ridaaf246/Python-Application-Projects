employees = []

while True:
    print("Employee Payroll and Attendance System")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Mark Attendance")
    print("4. Calculate Salary")
    print("5. Search Employee")
    print("6. Delete Employee")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        id = input("Enter Employee ID: ")

        found = False

        for e in employees:
            if e["id"] == id:
                found = True
                break

        if found:
            print("Employee ID already exists.")
        else:
            name = input("Enter Employee Name: ")
            dept = input("Enter Department: ")
            salary = int(input("Enter Basic Salary: "))

            data = {
                "id": id,
                "name": name,
                "dept": dept,
                "salary": salary,
                "attendance": 0
            }

            employees.append(data)

            print("Employee added successfully.")

    elif choice == "2":
        if len(employees) == 0:
            print("No employee records found.")
        else:
            for e in employees:
                print("Employee ID:", e["id"])
                print("Name:", e["name"])
                print("Department:", e["dept"])
                print("Salary:", e["salary"])
                print("Attendance:", e["attendance"])
                print()

    elif choice == "3":
        id = input("Enter Employee ID: ")

        found = False

        for e in employees:
            if e["id"] == id:
                days = int(input("Enter present days: "))
                e["attendance"] += days

                print("Attendance updated.")
                found = True
                break

        if found == False:
            print("Employee not found.")

    elif choice == "4":
        id = input("Enter Employee ID: ")

        found = False

        for e in employees:
            if e["id"] == id:
                pay = (e["salary"] / 30) * e["attendance"]

                print("Employee Name:", e["name"])
                print("Present Days:", e["attendance"])
                print("Basic Salary:", e["salary"])
                print("Payable Salary:", pay)

                found = True
                break

        if found == False:
            print("Employee not found.")

    elif choice == "5":
        id = input("Enter Employee ID: ")

        found = False

        for e in employees:
            if e["id"] == id:
                print("Employee Found")
                print("Name:", e["name"])
                print("Department:", e["dept"])
                print("Salary:", e["salary"])
                print("Attendance:", e["attendance"])

                found = True
                break

        if found == False:
            print("Employee not found.")

    elif choice == "6":
        id = input("Enter Employee ID to delete: ")

        found = False

        for e in employees:
            if e["id"] == id:
                employees.remove(e)

                print("Employee deleted.")
                found = True
                break

        if found == False:
            print("Employee not found.")

    elif choice == "7":
        print("Thank you for using Employee Payroll System.")
        break

    else:
        print("Invalid choice.")