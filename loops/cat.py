def main():
    # count = 5
    # while count > 0:
    #     print("meow")
    #     count -= 1

    # for i in [0,1,2]: # can use list, tuple, string, range
    # for _ in range(3):
    #     print("meow")
    # OR
#     print("meow\n" * 3, end="")
    # OR
    # n = 0
    # while n <= 0:
    #     n = int(input("How many times do you want the cat to meow? "))
    #     for _ in range(n):
    #         print("meow")
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("How many times do you want the cat to meow? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

if __name__ == "__main__":
    main()
