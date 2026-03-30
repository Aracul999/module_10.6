width = int(input('Введите ширину: '))
height = int(input('Введите высоту: '))

symbol_width = '-'
symbol_height = '|'
symbol_space = ' '

for row in range(1, height + 1):
    for col in range(1, width + 1):

        if row == 1 or row == height:
            print(symbol_width, end='')
        elif col == 1 or col == width:
            print(symbol_height, end='')
        else:
            print(symbol_space, end='')

    print()
