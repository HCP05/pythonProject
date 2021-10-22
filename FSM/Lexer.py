import enum
from enum import Enum

from tabulate import tabulate


def lexDict(f):
    def wrap(*args: list[str], **kwargs):
        elements = args[0]
        tokens=[]
        for el in elements:

        return f(*args, **kwargs)

    return wrap


@lexDict
def getLexNames(x):
    myDictionary = {
        Lexer.MyTypes.REJECT: 'REJECT',
        Lexer.MyTypes.IDENTIFIER: 'IDENTIFIER',
        Lexer.MyTypes.KEYWORD: 'KEYWORD',
        Lexer.MyTypes.OPERATOR: 'OPERATOR',
        Lexer.MyTypes.SEPARATOR: 'SEPARATOR',
        Lexer.MyTypes.CONSTANT: 'CONSTANT'
    }
    return myDictionary[x]


class Lexer:
    @classmethod
    def __fromEnumsToNames(cls):
        x = [[data.name for data in row] for row in cls.stateTable]
        return x[0], x[1:]

    class MyTypes(Enum):
        STARTPOINT = 0
        REJECT = 1
        IDENTIFIER = 2
        KEYWORD = 3
        OPERATOR = 4
        SEPARATOR = 5
        CONSTANT = 6

    stateTable = None

    @staticmethod
    def computeLine(x: str = ''):
        if Lexer.stateTable is None:
            Lexer.stateTable = Lexer.__createTable()
            # method 1
            # print('StateTable is created:\n\n{}'.format(
            #     '\n'.join([' '.join(['{}'.format(item.name + ' ' * (13 - len(item.name))) for item in row])
            #                for row in Lexer.stateTable])))

            # method 2
            headers, list = Lexer.__fromEnumsToNames()
            print(tabulate(list, headers=headers[1:], tablefmt="fancy_grid"))
            print()
        if x != '\n':
            x = [char for char in x]
            getLexNames(x)

    @classmethod
    def __createTable(cls):
        myTypes = Lexer.MyTypes
        return [
            [myTypes.STARTPOINT, myTypes.REJECT, myTypes.IDENTIFIER, myTypes.KEYWORD, myTypes.OPERATOR,
             myTypes.SEPARATOR, myTypes.CONSTANT],
            [myTypes.REJECT, myTypes.REJECT, myTypes.REJECT, myTypes.REJECT, myTypes.REJECT, myTypes.REJECT,
             myTypes.REJECT],
            [myTypes.IDENTIFIER, myTypes.REJECT, myTypes.IDENTIFIER, myTypes.KEYWORD, myTypes.REJECT, myTypes.REJECT,
             myTypes.REJECT],
            [myTypes.KEYWORD, myTypes.REJECT, myTypes.IDENTIFIER, myTypes.REJECT, myTypes.REJECT, myTypes.REJECT,
             myTypes.REJECT],
            [myTypes.OPERATOR, myTypes.REJECT, myTypes.REJECT, myTypes.REJECT, myTypes.OPERATOR, myTypes.REJECT,
             myTypes.REJECT],
            [myTypes.SEPARATOR, myTypes.REJECT, myTypes.REJECT, myTypes.REJECT, myTypes.REJECT, myTypes.SEPARATOR,
             myTypes.REJECT],
            [myTypes.CONSTANT, myTypes.REJECT, myTypes.REJECT, myTypes.REJECT, myTypes.REJECT, myTypes.REJECT,
             myTypes.CONSTANT],
        ]
