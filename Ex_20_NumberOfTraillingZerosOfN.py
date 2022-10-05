"""
Algorytm:
1. Każda wielokrotność 5, to jedno dodatkowe zero w wyniku: 5 -> 0 10 -> 0 ....
2. 5. wielokrotność liczby 5 dodaje 2 zera : 25 -> 00, 50 -> 00

Wnioski:
Jedna 25 -> 000 000 (sześć zer)

"""


def zeros(n):
    digits_num = len(str(n))
    sum_of_zeros = 0
    for item in range(1, digits_num + 10):
        sum_of_zeros += n // pow(5, item)
    return sum_of_zeros


n = 1000449
print(zeros(n))
