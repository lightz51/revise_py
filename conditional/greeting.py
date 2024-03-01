def main():
    greeting = input("Greeting: ").lower()
    if greeting.find("hello") == -1:
        if greeting.startswith("h"):
            print("20$")
        else:
            print("100$")
    else:
        print("0$")

if __name__ == "__main__":
    main()