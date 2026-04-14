import os

# os.system("notepad")

print(os.getcwd())

# os.mkdir("new_folder")

# os.rename("new_folder", "renamed_folder")

# os.rmdir("renamed_folder")
for i in range (5):
    if(os.path.exists(f"folder_{i}")):
        print("Folder already exists")
    else:
        os.mkdir(f"folder_{i}")
    

    