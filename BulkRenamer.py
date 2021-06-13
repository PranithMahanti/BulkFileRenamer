from os import listdir, rename

path = "bulk/"

files = listdir(path)
c = 0
new_name = input("New Name: ")

for file in files:
    c += 1
    rename(f"{path}/{file}", f"{path}/{new_name} {c}")
