from zdilar_marko_1 import readMatrics

def sumMatrixRows(matrix):
    sumList = []
    for row in matrix:
        tempSum = 0
        for number in row:
            tempSum += number
        sumList.append(tempSum)
    
    return sumList

def main():
    matrix = readMatrics("matrica.txt")
    print(matrix)
    print(f"Suma redaka: {sumMatrixRows(matrix)}.")
    

if __name__ == "__main__":
    main()
