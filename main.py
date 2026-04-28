FILENAME = "data.txt"

try:
    with open(FILENAME, "x") as file:
        file.write("Hello, World!\n")
except FileExistsError:
    print(f"The file '{FILENAME}' already exists. Please choose a different name.")