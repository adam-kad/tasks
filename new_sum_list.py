array_a = [1, 1, 1, 1, 1, 1, 1]
array_b = [2, 3, 4, 5, 6, 7, 8]
array_c = [2, 3, 4, 5, 6, 7, 8]
array_d = [2, 3, 4, 5, 6, 7, 8]


result = [a + b + c + d for a, b, c, d in zip(array_a, array_b, array_c, array_d)]


#zip_array = zip(array_a, array_b, array_c, array_d) # "Сшиваем" списки, получаем
#map_array = map(sum, zip_array) # Суммируем элементы в каждом подсписке
#result = list(map_array) # Преобразовываем в list


print(result)
