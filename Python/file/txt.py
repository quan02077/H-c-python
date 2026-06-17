employees = ["Peter Griffin", "Glenn Quagmire", "Joe", "Cleverland"]

file_path = "output.txt"

try:
    with open(file_path, "w") as file:
        for employee in employees:
            file.writelines(employee + "\n")
        print(f"txt file '{file_path}' was created!")
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileExistsError:
    print("That file already exists!")
except FileNotFoundError:
    print("That file was not found")