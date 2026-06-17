import json

employee = {
    "Name": "Peter Griffin",
    "Age": 45,
    "Job": "Fisherman"
}
file_path = "test.json"

try:
    with open(file_path, "w") as f:
        json.dump(employee, f)
        print(f"json file '{file_path}' was created!")
    with open(file_path, "r") as f:
        content = json.load(f)
        print(content)
except FileExistsError:
    pass