def main():
    students = {
        "Harry": "Gryffindor",
        "Ron": "Gryffindor",
        "Hermione": "Gryffindor",
        "Ginny": "Gryffindor",
        "Fred": "Gryffindor",
        "George": "Gryffindor",
        "Neville": "Gryffindor",
        "Luna": "Ravenclaw",
        "Cho": "Ravenclaw",
        "Cedric": "Hufflepuff",
        "Draco": "Slytherin",
        "Pansy": "Slytherin",
        "Crabbe": "Slytherin",
        "Goyle": "Slytherin"
    }

    for student in students:
        print(student, students[student], sep=": ", end="!\n")

if __name__ == "__main__":
    main()