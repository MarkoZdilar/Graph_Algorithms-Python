d = {1:[2,3,5], 2:[1, 4], 3:[1,2]}

def revDict(d):
    d2 = {}
    for key,values in d.items():
        for value in values:
            if value not in d2.keys():
                d2[value] = []
            if value in d2.keys() and value not in d2.values():
                d2[value].append(key)

    return dict(sorted(d2.items()))

print(revDict(d))

# New dictionary: {1:[2,3],2:[1,3], 3:[1], 4:[2], 5:[1]}