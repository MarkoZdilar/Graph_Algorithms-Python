def isPrimeNumber(num):
    numOfDividers = 0
    for i in range (1, num + 1):
        if num % i == 0:
            numOfDividers+=1
    
    if numOfDividers > 2:
        return False
    else:
        return True

def howManyPrimes(firstNum, secondNum):
    primes = 0
    for i in range (firstNum, secondNum): 
        if isPrimeNumber(i):
            primes += 1
    return primes

def main():
    firstNum = int(input('Enter first number:'))
    secondNum = int(input('Enter second number:'))
    print('Number of primes between ', firstNum, ' and ', secondNum, ' is ', howManyPrimes(firstNum, secondNum))

if __name__ == "__main__":
    main()
    
