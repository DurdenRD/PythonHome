# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

n = int(input("введите трехзначное число: "))

if n < 0:
    n = -n

if n // 100 != 0 and n // 100 < 10 and n % 100 != 0:

    n1 = n // 100
    n2 = (n - n1*100) // 10
    n3 = n- n1*100 - n2*10
    n = n1 + n2 + n3
    print(n)
else:
    print("число не трехзначное")
