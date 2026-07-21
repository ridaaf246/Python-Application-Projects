patients = []
doctors = []

while True:
    print("Hospital Management System")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Add Doctor")
    print("7. View Doctors")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        id = input("Enter Patient ID: ")

        found = False

        for p in patients:
            if p["id"] == id:
                found = True
                break

        if found:
            print("Patient ID already exists.")
        else:
            name = input("Enter Patient Name: ")
            age = input("Enter Age: ")
            disease = input("Enter Disease: ")
            phone = input("Enter Phone Number: ")

            data = {
                "id": id,
                "name": name,
                "age": age,
                "disease": disease,
                "phone": phone
            }

            patients.append(data)

            print("Patient added successfully.")

    elif choice == "2":
        if len(patients) == 0:
            print("No patient records found.")
        else:
            for p in patients:
                print("Patient ID:", p["id"])
                print("Name:", p["name"])
                print("Age:", p["age"])
                print("Disease:", p["disease"])
                print("Phone:", p["phone"])
                print()

    elif choice == "3":
        id = input("Enter Patient ID: ")

        found = False

        for p in patients:
            if p["id"] == id:
                print("Patient Found")
                print("Name:", p["name"])
                print("Age:", p["age"])
                print("Disease:", p["disease"])
                print("Phone:", p["phone"])

                found = True
                break

        if found == False:
            print("Patient not found.")

    elif choice == "4":
        id = input("Enter Patient ID to update: ")

        found = False

        for p in patients:
            if p["id"] == id:
                p["name"] = input("Enter New Name: ")
                p["age"] = input("Enter New Age: ")
                p["disease"] = input("Enter New Disease: ")
                p["phone"] = input("Enter New Phone: ")

                print("Patient record updated.")

                found = True
                break

        if found == False:
            print("Patient not found.")

    elif choice == "5":
        id = input("Enter Patient ID to delete: ")

        found = False

        for p in patients:
            if p["id"] == id:
                patients.remove(p)

                print("Patient record deleted.")

                found = True
                break

        if found == False:
            print("Patient not found.")

    elif choice == "6":
        id = input("Enter Doctor ID: ")
        name = input("Enter Doctor Name: ")
        dept = input("Enter Department: ")
        phone = input("Enter Phone Number: ")

        data = {
            "id": id,
            "name": name,
            "dept": dept,
            "phone": phone
        }

        doctors.append(data)

        print("Doctor added successfully.")

    elif choice == "7":
        if len(doctors) == 0:
            print("No doctors available.")
        else:
            for d in doctors:
                print("Doctor ID:", d["id"])
                print("Name:", d["name"])
                print("Department:", d["dept"])
                print("Phone:", d["phone"])
                print()

    elif choice == "8":
        print("Thank you for using Hospital Management System.")
        break

    else:
        print("Invalid choice.")