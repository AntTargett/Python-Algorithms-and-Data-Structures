ListA = [[1, 2, 3],
         [4, 5, 6]]
ListB = [[7, 8],
         [9, 10],
         [11, 12]]


def MultiplicationOfMatrices(MatrixA, MatrixB):
    FinalList = [[0]*len(MatrixA) for i in range(len(MatrixB[0]))]
    print(FinalList)
    for k in range(len(MatrixA)):
        for i in range(len(MatrixB[0])):
            for l in range(len(MatrixB)):
                FinalList[k][i] += MatrixA[k][l]*MatrixB[l][i]
    print(FinalList)


MultiplicationOfMatrices(ListA, ListB)
