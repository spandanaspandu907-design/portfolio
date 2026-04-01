import os
import shutil

folder = "."

# Create folders
if not os.path.exists("Images"):
    os.mkdir("Images")

if not os.path.exists("Documents"):
    os.mkdir("Documents")

files = os.listdir(folder)

for file in files:

    # Skip folders
    if file == "Images" or file == "Documents" or file == "test.py":
        continue

    # Move Images
    if file.endswith(".jpg") or file.endswith(".png"):
        shutil.move(file, "Images/" + file)
        print(file, "moved to Images")

    # Move Documents
    elif file.endswith(".pdf") or file.endswith(".txt"):
        shutil.move(file, "Documents/" + file)
        print(file, "moved to Documents")