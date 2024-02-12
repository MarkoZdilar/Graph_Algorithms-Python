from zdilar_marko_3a import  isPrimeNumber

def primeNeighbours(num):
    primes = []
    neighbours = []
    for i in range(2, num):
        if(isPrimeNumber(i)):
            primes.append(i)

    for i in range(1, len(primes)):
        if ( primes[i] - primes[ i - 1 ] ) == 2:
            neighbours.append((primes[i - 1]))
            neighbours.append((primes[i]))
    
    return neighbours



def main():
    num = int(input('Enter your number: '))
    print(primeNeighbours(num))

if __name__ == "__main__":
    main()