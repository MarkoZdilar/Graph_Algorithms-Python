from zdilar_marko_1 import readMatrics

def makeDict(matrix):
    
    print(matrix)
    dictionary = {}
    for row in matrix:
        dictionary[row[0]] = []
        dictionary[row[0]].append(row[1])

    return dictionary

def main():
    matrix = readMatrics("file.txt")
    print(f"New dictionary: {makeDict(matrix)}")
    

if __name__ == "__main__":
    main()
    