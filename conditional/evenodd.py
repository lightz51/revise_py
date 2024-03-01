def main():
    num = int(input("Enter a number: "))
    if is_even(num):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

def is_even(n):
    return n % 2 == 0
#   return True if n % 2 == 0 else False

if __name__ == "__main__":
    main()