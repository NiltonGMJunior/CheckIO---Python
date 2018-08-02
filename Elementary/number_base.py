def checkio(str_number, radix):

    result = 0

    base = list(range(0, 10))

    for i in range(0, len(base)):
        base[i] = str(base[i])

    ordA = ord('A')
    ordZ = ord('Z')

    for i in range(ordA, ordZ + 1):
        base.append(chr(i))

    base = base[0:radix]

    for i in range(0, len(str_number)):
        try:
            temp = base.index(str_number[len(str_number) - i - 1])
        except ValueError:
            return -1
        result += temp*radix**i

    return result
