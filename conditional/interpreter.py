def main():
    n1, x, n2 = input("Expression: ").split(" ")
    n1, n2 = map(float, (n1,n2))
    n1 = round(n1, 1)
    n2 = round(n2, 1)

    match x:
        case "+":
            print(n1 + n2)
        case "-":
            print(n1 - n2)
        case "*":
            print(n1 * n2)
        case "/":
            print(n1 / n2)
        case "%":
            print(n1 % n2)
        case _:
            print("Unsupported Operator")

if __name__ == "__main__":
    main()