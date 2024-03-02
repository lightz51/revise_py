def main():
    n = int(input("Height and width of the brick block: "))
    print_square(n)

def print_square(size):
    for i in range(size):
        print("#" * size)

if __name__ == "__main__":
    main()