import json, os

user_data = "users.json"

def load_data():
    if not os.path.exists(user_data):
        return []
    try:
        with open(user_data, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Lỗi file!")
        return []

def save_data(users):
    with open(user_data, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

