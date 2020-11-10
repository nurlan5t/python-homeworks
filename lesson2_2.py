print("Здарова!!! Че опять деньги потратил?")

expenses = []

while True:
    print("1) Вывести все рассходы ")
    print("2) Сумма всех расходов ")
    print("3) Добавить новый рассход ")
    option = int(input("Выберите вариант: "))


    if option == 1:
        for rasshod in expenses:
            print(f"{rasshod[0]} | {rasshod[1]} | {rasshod[2]}")

    if option == 2:
        result = 0
        for rasshod in expenses:
            result += rasshod[0]
            money = money - result
        print(f"Сумма ваших рассходов: {result}")
        print(f"Остаток в кошельке {money}")
        expenses.insert(3, money)

    if option == 3:
        amount = int(input("Введите сумму: "))
        name = input("На что потратил: ")
        date = input("Когда потратил: ")
        money = int(input("Введите сумму в кошельке: "))
        expenses.append([amount, name, date, money])

