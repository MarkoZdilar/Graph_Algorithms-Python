def nadjiPresjek(intervalA, intervalB):
    najmanjaGornja = 0
    najvecaDonja = 0
    if(intervalA[1] < intervalB[1]):
        najmanjaGornja = intervalA[1]
    else:
        najmanjaGornja = intervalB[1]
    
    if(intervalA[0] < intervalB[0]):
        najvecaDonja = intervalB[0]
        if(najvecaDonja > intervalA[1]):
            print("Presjek je prazan skup!")
            return
    else:
        najvecaDonja = intervalA[0]
        if(najvecaDonja > intervalB[1]):
            print("Presjek je prazan skup!")
            return

    print("Presjek je [" + str(najvecaDonja) + ", " + str(najmanjaGornja) + "]")
    
    

def sortirajUlaze(donja, gornja):
    donja = float(donja)
    gornja = float(gornja)
    interval = []
    if(donja < gornja):
        interval.append(donja)
        interval.append(gornja)
    else:
        interval.append(gornja)
        interval.append(donja)
    
    return interval

def main():
    aDonja = input("Unesite prvu granicu prvog intervala: ")
    aGornja = input("Unesite drugu granicu prvog intervala: ")
    intervalA = sortirajUlaze(aDonja, aGornja)
    aDonja = input("Unesite prvu granicu drugog intervala: ")
    aGornja = input("Unesite drugu granicu drugog intervala: ")
    intervalB = sortirajUlaze(aDonja, aGornja)
    print("Prvi interval: " + str(intervalA))
    print("Drugi interval: " + str(intervalB))

    nadjiPresjek(intervalA, intervalB)


if __name__ == "__main__":
    main()