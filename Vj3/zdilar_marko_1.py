import os

def readMatrics(matrixName):
    script_dir = os.path.dirname(__file__)  # path do .py
    file_path = os.path.join(script_dir, matrixName)
    matrix = []

    with open(file_path) as file:
        #row = [int(num) for num in line.split()]
        for line in file:
            nums = line.split() # .split() - defaultno radi split po razmacima
            row = []
            for num in nums:
                row.append(int(num))
            
            matrix.append(row)
            print(row)

    return matrix

def isSquareMatrix(matrix):
    num_rows = len(matrix)
    for row in matrix:
        if(len(row) != num_rows):
            return False
    
    return True


def sumAboveSecondaryDiagonal(matrix):
    matrixLen = len(matrix)
    sum = 0

    for i in range(matrixLen):
        for j in range(matrixLen - i - 1): # prvo 0 3, pa 0 2, 0,1... 1 2, 1 1, 1 0...
            sum += matrix[i][j]

    return sum


def sumAboveMainDiagonal(matrix): #Gornji lijevi do donji desni kut
    matrixLen = len(matrix)
    sum = 0

    for i in range(matrixLen):
        for j in range(i + 1, matrixLen):
            sum += matrix[i][j] # prvo 0 1, pa 0 2, 0,3... 1 1, 1 2, ...
    return sum


def main():
    matrix = readMatrics("matrica.txt")
    if(not isSquareMatrix(matrix)):
        print("(0, 0)")
        return
    
    print(f"({sumAboveMainDiagonal(matrix)}, {sumAboveSecondaryDiagonal(matrix)})")

if __name__ == "__main__":
    main()