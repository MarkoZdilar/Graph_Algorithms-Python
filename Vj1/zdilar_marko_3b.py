from zdilar_marko_3a import isPrimeNumber

def nPrime(num):
    primeCounter = 0 
    i = 1
    while primeCounter != num:
        i += 1
        if(isPrimeNumber(i)):
            primeCounter += 1
            print('Prime number = ', i)

    return i

def main():
    num = int(float(input('Enter your number:')))
    print(num, 'th prime number is', nPrime(num))

if __name__ == "__main__":
    main()