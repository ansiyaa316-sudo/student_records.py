import json
student_records = {
    "S001": {"name": "Alice Johnson", "age": 20, "grade": "A"},
    "S002": {"name": "Bob Smith", "age": 19, "grade": "B"},
    "S003": {"name": "Carol Lee", "age": 21, "grade": "A-"}
}

print("Keys:", list(student_records.keys()))

student_records["S001"]["grade"] = "A+"
del student_records["S002"]

print("Looping through records:")
for sid, details in student_records.items():
    print(f"ID: {sid}, Name: {details['name']}")

with open("students.json", "w") as file:
    json.dump(student_records, file, indent=4)

with open("students.json", "r") as file:
    loaded_records = json.load(file)

print("=== Final Records ===")
for sid, details in loaded_records.items():
    print(f"ID: {sid} | {details['name']} | Age: {details['age']} | Grade: {details['grade']}")