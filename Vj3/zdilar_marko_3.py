from zdilar_marko_1 import readMatrics

def twoOnesInARow(matrix):
    for row in matrix:
        numberOfOnes = 0
        for number in row:
            if(number == 1):
                numberOfOnes +=1
            elif(number != 0):
                return False
        if(numberOfOnes != 2):
            return False
    return True

def main():
    matrix = readMatrics("matrica2.txt")
    print(matrix)
    print(f"Matrix have each row with two ones and other zeros? {twoOnesInARow(matrix)}")
    

if __name__ == "__main__":
    main()
    