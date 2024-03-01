def main():
    # x = float(input("Enter the value of x: "))
    # y = float(input("Enter the value of y: "))

    # z = round(x + y)
    # print(f"{z:,}")
    score = int(input("Please enter your score: "))

    if score > 100:
        print("Invalid score")
    elif 90 <= score <= 100:
        print("Grade A")
    elif 80 <= score < 90:
        print("Grade B")
    elif 70 <= score < 80:
        print("Grade C")
    elif 60 <=score < 70:
        print("Grade D")
    else:
        print("Grade F")

if __name__ == "__main__":
    main()