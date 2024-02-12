lst = [7, 18, 3, 'a', True, (2,3)]

def largerIter(list):
    largest = None
    for element in list:
        if largest is None:
            largest = element

        if str(element).isnumeric():
            if element > largest:
                largest = element
    
    return largest

def largerRecursive(list):
    if len(list) == 1:
        return list[0]
    else:
        largest = largerRecursive(list[1:])
        return largest if str(list[0]).isnumeric() and str(largest).isnumeric() and largest > list[0] else list[0]

print("Iterative: Largest number from the list " + str(lst) + " is " + str(largerIter(lst)) + ".")
print("Recursive: Largest number from the list " + str(lst) + " is " + str(largerRecursive(lst)) + ".")
