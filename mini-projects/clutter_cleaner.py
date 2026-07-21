import os

folder = "Clutter"

files = os.listdir(folder)

png = 1
jpg = 1
txt = 1

for file in files:

    old = folder + "/" + file

    if file.endswith(".png"):
        new = folder + "/" + str(png) + ".png"
        os.rename(old, new)
        png += 1

    elif file.endswith(".jpg"):
        new = folder + "/" + str(jpg) + ".jpg"
        os.rename(old, new)
        jpg += 1

    elif file.endswith(".txt"):
        new = folder + "/" + str(txt) + ".txt"
        os.rename(old, new)
        txt += 1

print("Clutter cleared!")