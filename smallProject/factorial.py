def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
# factorial : 5! = 5 * 4 * 3 * 2 * 1
# first : 5 * (5-1)
# fact = 20 * (4-1)
# fact = 60 * (3-1)
# fact = 120 * (2-1)
# fact = 120


print(factorial(5))
