from zdilar_marko_3a import isPrimeNumber

def waysToShowEvenNumber():
    num = int(input('Enter even number:'))
    
    if num % 2 == 1:
        print("Wrong input! Number is odd.")
    else:
        primes = []

        for i in range (2, num):
            if isPrimeNumber(i):
                primes.append(i)

        for i in range (0, len(primes)):
            for j in range (i, len(primes)):
                if (primes[i] + primes[j] == num):
                    print(primes[i], ' + ', primes[j] ,' = ', num)


def main():
    waysToShowEvenNumber()

if __name__ == "__main__":
    main()