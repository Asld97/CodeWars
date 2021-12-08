# Exercise 13 Product of consecutive Fib numbers
"""
You are asked to find 2 numbers in the Fibonacci sequence f(n) and f(n+1)
which product is greater or equals to the number given.

You must return it as a array/tuple/what ever like this:
(fn(n), fn(n+1), eq) while eq is a boolean that indicates if the product is equals with the number given.

If it is not equal, the Fibonaccies numbers in Array are the one which product is bigger
"""


# Fibonacci numbers generator
def fib_generator():
    a = 0
    b = 1

    while True:
        yield a
        temp = a
        a = b
        b = temp + b


# Comparison function
def productFib(product):
    temp_tab = []

    for i in fib_generator():
        temp_tab.append(i)
        if len(temp_tab) == 3:
            product_1 = temp_tab[0] * temp_tab[1]
            product_2 = temp_tab[1] * temp_tab[2]

            if product_1 == product:
                return [temp_tab[0], temp_tab[1], True]
            if product_1 < product < product_2:
                return [temp_tab[1], temp_tab[2], False]

            temp_tab.pop(0)


numb = 800
print(productFib(numb))
