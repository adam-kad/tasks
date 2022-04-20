CUBES = [
    "blue",
    "blue",
    "blue",
    "yellow",
    "yellow",
    "blue",
    "blue",
    ["blue", "yellow", "blue", ["blue", "yellow", "blue", ["blue", "yellow", "blue"]]],
    ["blue", "blue", "yellow", "blue"],
    [[[[[[[[[['yellow', 'blue', 'yellow']]]]]]]]]]
]


def find_cube(cubes, depth=0):
    for index, cube in enumerate(cubes, 0):

        if depth < 10:

            if isinstance(cube, list):
                find_cube(cube, depth + 1)
            else:
                if cube == "blue":
                    continue
                elif cubes[index + 1] == "blue":
                    print(f"Остановись, ты нашел нужный кубик:")
                    print(f"Индекс: {index} \nГлубина: {depth}")
                    print("----" * 12)
                    continue
                elif cubes[index + 1] == "yellow":
                    continue
        

        elif depth >= 10:

            if isinstance(cube, list):
                find_cube(cube, depth + 1)
            else:
                if cube == "yellow":
                    continue
                elif cubes[index + 1] == "yellow":
                    print(f"Остановись, ты нашел нужный синий кубик:")
                    print(f"Индекс: {index} \nГлубина: {depth}")
                    print("----" * 12)
                    continue
                elif cubes[index + 1] == "blue" and cubes[index + 2] == 'yellow':
                    continue


find_cube(CUBES)
