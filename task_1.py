for row in range(0 , 6):
    print(row, end='\t')

    for col in range(2, 10+1 , 2):
        print(col + row , sep=' ' , end='\t')

    print()
