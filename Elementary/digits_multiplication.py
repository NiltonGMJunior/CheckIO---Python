def checkio(number):

    prod = 1

    num_str = str(number)

    for i in num_str:
        if i != '0':
            prod *= int(i)

    return prod
