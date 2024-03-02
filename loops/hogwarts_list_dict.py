def main():
    students = [
        {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
        {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
        {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
        {"name": "Luna", "house": "Ravenclaw", "patronus": "Hare"},
        {"name": "Ginny", "house": "Gryffindor", "patronus": "Horse"},
        {"name": "Draco", "house": "Slytherin", "patronus": None}
    ]

    for student in students:
        print(student["name"], student["house"], student["patronus"], sep=" - ")

    # for i in range(len(students)):
    #     print(students[i]["name"], students[i]["house"], students[i]["patronus"])

if __name__ == "__main__":
    main()