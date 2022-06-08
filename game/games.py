import operator
import typing as t


class Field:
    def __init__(self) -> None:
        self.__fields = [["", "", ""], ["", "", ""], ["", "", ""]]

    def set_symbol(self, symbol: str, coordinates: t.Tuple[int, int]) -> None:
        x, y = coordinates
        if x > 2 or y > 2 or self.__fields[x][y]:
            raise ValueError()
        self.__fields[x][y] = symbol
        self.render()

    def render(self) -> None:
        for row in self.__fields:
            print(" ", end="")
            print(" | ".join(row), sep=" | ")
            if operator.indexOf(self.__fields, row) < 2:
                print('-' * 9)


class Player:    
    x = int(input('Введите координату 1(строка): '))
    y = int(input('Введите координату 2(столбец): '))
    
    def __init__(self) -> None:
        self.sim = 'x'
        
        Field.set_symbol(self.sim ,x,y)
    
    def coor(x, y):
        return x+y
    