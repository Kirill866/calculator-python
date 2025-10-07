# Простой калькулятор на Python

def calculator():
    print("=== Простой калькулятор ===")
    print("Доступные операции: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            op = input("Введите операцию (+, -, *, /): ")
            num2 = float(input("Введите второе число: "))

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Ошибка: деление на ноль!")
                    continue
                result = num1 / num2
            else:
                print("Неизвестная операция. Попробуйте снова.")
                continue

            print(f"Результат: {result}\n")
            
        except ValueError:
            print("Ошибка: введите числа корректно!")
        
        again = input("Хотите продолжить? (да/нет): ").lower()
        if again != 'да':
            print("Выход из программы.")
            break


if __name__ == "__main__":
    calculator()
