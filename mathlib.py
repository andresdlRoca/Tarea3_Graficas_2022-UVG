def matrixMult(A, B):
    result = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0,0,0,0]]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def convertMatrix(row, col, data):
    mat = []
    for i in range(row):
        rowList = []
        for j in range(col):
            rowList.append(data[row * i + j])
        mat.append(rowList)

    return mat

def identity(num):
    matrix = []
    for row in range(0, num):
        matrix.append([])
        for col in range(0, num):
            # Here end is used to stay in same line
            if (row == col):
                matrix[row].append(1)
            else:
                matrix[row].append(0)
    return matrix

def dot(vec1, vec2):
     return sum([x*y for x,y in zip(vec1, vec2)])

def matMultVect(M, v):
    return [dot(r,v) for r in M]