array_a = [1, 1, 1, 1, 1, 1, 1]
array_b = [2, 3, 4, 5, 6, 7, 8]
array_c = [2, 3, 4, 5, 6, 7, 8]
array_d = [2, 3, 4, 5, 6, 7, 8]



zip_array = zip(array_a, array_b, array_c, array_d) # "Сшиваем" списки, получаем ((1, 3, 5), (2, 4, 6))
map_array = map(sum, zip_array) # Суммируем элементы в каждом подсписке
result = list(map_array) # Преобразовываем в list


print(result)
