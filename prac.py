def main():
    name = input("What is your name? ").strip().title()
    first_name, last_name = name.split(" ")
    print("Hello,", first_name)

if __name__ == "__main__":
    main()
