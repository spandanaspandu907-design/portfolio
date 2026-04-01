import os
import hashlib

def get_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]

def analyze(files, path):
    types = {
        "Images": [".jpg", ".png", ".jpeg"],
        "Documents": [".pdf", ".txt", ".docx"],
        "Videos": [".mp4", ".mkv"],
        "Others": []
    }

    result = {k: 0 for k in types}

    for f in files:
        ext = os.path.splitext(f)[1].lower()
        found = False
        for k, v in types.items():
            if ext in v:
                result[k] += 1
                found = True
                break
        if not found:
            result["Others"] += 1

    print("\nFile Analysis:")
    for k, v in result.items():
        print(f"{k}: {v} files")


def find_duplicates(files, path):
    hashes = {}
    duplicates = []

    for f in files:
        fp = os.path.join(path, f)
        with open(fp, "rb") as file:
            h = hashlib.md5(file.read()).hexdigest()

        if h in hashes:
            duplicates.append(f)
        else:
            hashes[h] = f

    print("\nDuplicate Files:")
    print(duplicates if duplicates else "No duplicates found")


def largest_files(files, path):
    sizes = [(f, os.path.getsize(os.path.join(path, f))) for f in files]
    sizes.sort(key=lambda x: x[1], reverse=True)

    print("\nTop 3 Largest Files:")
    for f, s in sizes[:3]:
        print(f"{f} - {s//1024} KB")


# -------- MAIN --------
path = input("Enter folder path:")

if not os.path.exists(path):
    print("Invalid path!")
else:
    files = get_files(path)

    analyze(files, path)
    find_duplicates(files, path)
    largest_files(files, path)