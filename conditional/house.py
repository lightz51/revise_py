name = input("What's your name: ").lower()

match name:
    case "harry" | "hermione" | "ron":
        print("Gryffindor")
    case "draco" | "snape":
        print("Slytherin")
    case "neville" | "cedric":
        print("Hufflepuff")
    case "luna", "cho":
        print("Ravenclaw")
    case "hagrid":
        print("You're a wizard, Harry")
    case _:
        print("Unknown house")