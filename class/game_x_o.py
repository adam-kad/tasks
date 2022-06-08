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