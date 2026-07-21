import os
import json


def make_folders(path):
    folders = {
        "Images": [".png", ".jpg", ".jpeg", ".gif"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Documents": [".pdf", ".docx", ".txt", ".pptx"],
        "Music": [".mp3", ".wav"],
        "Programs": [".py", ".cpp", ".java"],
        "Others": []
    }

    for name in folders:
        new_folder = os.path.join(path, name)

        if not os.path.exists(new_folder):
            os.mkdir(new_folder)

    return folders


def check_file(file, folders):
    ext = os.path.splitext(file)[1].lower()

    for name in folders:
        if ext in folders[name]:
            return name

    return "Others"


def organize(path):
    folders = make_folders(path)
    history = []

    try:
        files = os.listdir(path)

        for file in files:
            old_path = os.path.join(path, file)

            if os.path.isfile(old_path):

                folder = check_file(file, folders)

                new_path = os.path.join(path, folder, file)

                os.rename(old_path, new_path)

                history.append({
                    "file": file,
                    "folder": folder
                })

                print(file, "moved to", folder)

        file = open("organizer_history.json", "w")
        json.dump(history, file, indent=4)
        file.close()

        print("Files organized successfully")

    except:
        print("Something went wrong")


def show_history():
    try:
        file = open("organizer_history.json", "r")
        data = json.load(file)
        file.close()

        for item in data:
            print(item["file"], "moved to", item["folder"])

    except:
        print("No history found")


while True:
    print("Smart File Organizer Pro")
    print("1. Organize Files")
    print("2. Show History")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        path = input("Enter folder path: ")

        if os.path.exists(path):
            organize(path)

        else:
            print("Folder does not exist")

    elif choice == "2":
        show_history()

    elif choice == "3":
        print("Program closed")
        break

    else:
        print("Invalid choice")