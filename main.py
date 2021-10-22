from FSM.Lexer import Lexer

if __name__ == '__main__':
    fileName=input('Give the name of the file: ')
    fileName=fileName.split('/')[-1:][0]
    print(f'opening file \'{fileName}\' for parsing... ')
    fileName=fileName
    with open(fileName,'r') as f:
        for line in f:
            Lexer.computeLine(line)


