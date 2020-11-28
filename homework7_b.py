import CurrencyExchange

currency = CurrencyExchange.Currency()

while 1:
    num = int(input('Enter the amount: '))
    currency1 = int(input('Choose the currency: 1)USD 2)EUR 3)RUB '))
    if currency1 == 1:
        currency1 = 'USD'
    if currency1 == 2:
        currency1 = 'EUR'
    if currency1 == 3:
        currency1 = 'RUB'

    currency2 = int(input(f'{num}{currency1} to 1)USD 2)EUR 3)RUB ? '))
    if currency2 == 1:
        currency2 = 'USD'
    if currency2 == 2:
        currency2 = 'EUR'
    if currency2 == 3:
        currency2 = 'RUB'

    print(currency.convertCurrency(num, currency1, currency2))