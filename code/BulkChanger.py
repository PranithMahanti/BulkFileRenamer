from os import listdir, rename

path = "bulk/"

files = listdir(path)
c = 0
to_be_replaced = input("String to be replaced: ")
replacement = input("Replacement: ")

for file in files:
    f = f"{path}/{file}"
    rename(f, f.replace(to_be_replaced, replacement))
