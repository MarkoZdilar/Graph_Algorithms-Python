def mergeLists(lst1, lst2):
    #Set - jedinstvene elemente liste
    #Još jedno rješenje - Bitwise OR jer sa listama vraća uniju
    return list(set(lst1 + lst2))

def main():
    listA = [5, True, 1, 2, 3, 4]
    listB = ["A", 2, 7, 14]
    print(mergeLists(listA, listB))

if __name__ == "__main__":
    main()