n = int(input("Введите количество кустов: "))
while n < 3:
    dictionary = input("Ошибка! Количество кустов не должно быть меньше 3-х! \nВведите количество кустов: ")

numbers = list()
for i in range(n):
    numbers.append(int(input(f"Введите количество ягод на кусту {i + 1}: ")))

numbers_count = list()
for i in range(len(numbers) - 1):
    numbers_count.append(numbers[i - 1] + numbers[i] + numbers[i + 1])
numbers_count.append(numbers[-2] + numbers[-1] + numbers[0])

print(f"Максимальное число ягод, которое может собрать модуль: {max(numbers_count)}")
