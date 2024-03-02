def main():
    print_square(4)
    # print_row(4)
#     n = int(input("Height of brick column: "))
#     print_column(n)

# def print_column(height):
#     for _ in range(height):
#         print("#") 

# def print_row(width):
#     print("?" * width)

def print_square(size):
    # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):
            # print brick
            print("#", end="")
        print()

if __name__ == "__main__":
    main()