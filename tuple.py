# Задание 1. Создание и вывод кортежа

tuple1 = (1,True,"Str",10, False)
print(tuple1)

# Задание 2. Доступ к элементам

print(tuple1[0],tuple1[2],tuple1[4])

# Задание 3. Индексация и отрицательные индексы

tuple2 = (1,False,"Str",-7,True)
print(tuple2[-1],tuple2[-2])

# Задание 4. Подсчёт количества элементов

tuple3 = (1,2,3,1,2,5,4,3,1,5,4,3,1,1,4,4)
print(tuple3,f"Число 1 повторяется {tuple3.count(1)} раз")

# Задание 5. Поиск индекса элемента

print(tuple1,f"Элемент False находится по индексу {tuple1.index(False)}")

# Задание 6. Срезы кортежа

tenTuple = (1,2,3,4,5,6,7,8,9,10)
print(tenTuple[0],tenTuple[1],tenTuple[2],"и последние" ,tenTuple[-3],tenTuple[-2],tenTuple[-1])
print("Числа с шагом в 2: ", tenTuple[::2])

# Задание 7. Объединение кортежей

print(tuple1+tuple2)

# Задание 8. Повторение кортежа

print(tenTuple*3)

# Задание 9. Преобразование списка в кортеж и обратно

list1 = [34,4.4,"BMW",True,"sau"]
list1 = tuple(list1)
print(list1)
list1 = list(list1)
print(list1)

# Задание 10. Итерация по кортежу

tuple4 = (1,2,3,4,5,6,7)
for i in tuple4:
    print(i)
# Создай кортеж из 5–7 элементов.
# С помощью цикла for выведи каждый элемент на новой строке.