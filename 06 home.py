# ; Задача 6: Вы пользуетесь общественным транспортом? 
# ; Вероятно, вы расплачивались за проезд и получали билет с номером. 
# ; Счастливым билетом называют такой билет с шестизначным номером, 
# ; где сумма первых трех цифр равна сумме последних трех. Т.е. 
# ; билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# ; Вам требуется написать программу, которая проверяет счастливость билета.

# ; *Пример:*

# ; 385916 -> yes
# ; 123456 -> no


n = int(input("введите шестизначное положительное число: "))

    

if n < 1000000 and n > 99999:

    n1 = n // 100000
    n2 = (n - n1*100000) // 10000
    n3 = (n - n1*100000 - n2*10000) // 1000
    
    n6 = n % 10
    n5 = ((n - n6)//10)%10 
    n4 = ((n - n6 - n5*10)//100)%10 

    left = n1 + n2 + n3
    right = n4 + n5 + n6

    if left == right:
        print("Yes")
    else: 
        print("No")

else:
    print("число не корректное")