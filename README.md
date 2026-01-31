# Student Records Management

This Python script demonstrates how to manage student records using dictionaries and JSON. It covers creating records, updating and deleting data, looping through entries, saving to a JSON file, and reading data back from the file.

The script is beginner-friendly and showcases core Python concepts like dictionaries, loops, file handling, and JSON serialization.

## Features

Store student records using a Python dictionary

Access dictionary keys and values

Update and delete specific records

Loop through all student records

Save records to a JSON file

Read records back from the JSON file

Display clean, formatted output

## Files

students.json – Generated automatically to store student records

Python script – Contains all logic for managing records

## How the Script Works
### 1. Import JSON Module
import json


Used for converting Python dictionaries to JSON and back.

### 2. Store Student Data

Student records are stored in a dictionary, where each key is a student ID.

student_records = {
    "S001": {"name": "Alice Johnson", "age": 20, "grade": "A"},
    "S002": {"name": "Bob Smith", "age": 19, "grade": "B"},
    "S003": {"name": "Carol Lee", "age": 21, "grade": "A-"}
}

### 3. Access Dictionary Keys

Prints all student IDs:

print("Keys:", list(student_records.keys()))

### 4. Update and Delete Records

Updates Alice’s grade

Deletes Bob’s record

student_records["S001"]["grade"] = "A+"
del student_records["S002"]

### 5. Loop Through Records

Displays remaining student IDs and names:

for sid, details in student_records.items():
    print(f"ID: {sid}, Name: {details['name']}")

### 6. Save Records to JSON

Writes the dictionary to students.json:

with open("students.json", "w") as file:
    json.dump(student_records, file, indent=4)

### 7. Read Records from JSON

Loads data back into Python:

with open("students.json", "r") as file:
    loaded_records = json.load(file)

### 8. Display Final Output

Prints all stored data in a clean format:

for sid, details in loaded_records.items():
    print(f"ID: {sid} | {details['name']} | Age: {details['age']} | Grade: {details['grade']}")

## Requirements

Python 3.x
(No external libraries required)




Learn JSON file handling in Python

Improve looping and formatted output skills
