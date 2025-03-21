def add_numbers(a, b):

    return a + b


def main():

    
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))
        result = add_numbers(num1, num2)
        print(f"Wynik dodawania: {result}")



if __name__ == "__main__":
    main()