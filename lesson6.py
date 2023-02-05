list = [1, 2, 3, "a", "b", "c", [7, 9]] # список(массив)
list[0] = 5 
print(list[-1][0]) # вывод элемента из списка

numbers = [5, 2, 7]
#numbers[3] = 100
numbers.append(100)        # добавление элемента в конец списка
numbers.insert(1, True)    #                    по индексу
numbers.extend([5, 6, 10]) #                    мн кол-во
numbers.sort()             # сортировка

numbers.pop()     # удаление по индексу или последний элемент
numbers.remove(2) # удаление по значению

print(numbers)
