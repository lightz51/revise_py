# Program to convert camel case to snake case
# Finished in different file instead. (camel.py)

def main():
    # Take camelcase input
    camel = input("Enter a camel case string: ")
    camel_start = find_uppercase(camel)
    camel = camel.lower()
    snake = conversion(camel, camel_start)

    print(f"Snake case: {snake}")

# def find_uppercase(cstring):
#     for i in range(len(cstring)):
#         if cstring[i].isupper():
#             return i

def find_uppercase(cstring):
    i = 0
    index = []
    while i < len(cstring):
        if cstring[i].isupper():
            index.append(i)
        i += 1
    return index

    # Convert to snake case, find index of upper case letter and insert "_" before it, lowercase it
def conversion(cstring, index):
    for i in index:
        cstring = cstring[:i] + "_" + cstring[i:]
    return cstring

if __name__ == "__main__":
    main()