import math

def isPitagorial(a, b, c):
    pitagorialA  = (c * c) + (b * b)
    if(pitagorialA == (a * a)):
        return True
    return False

def main():
    while True:
        list = []
        list.append(float(input("Enter side a: ")))
        list.append(float(input("Enter side b: ")))
        list.append(float(input("Enter side c: ")))
        
        list.sort(reverse=True)
        
        if list[0] <= 0 or list[1] <= 0 or list[2] <= 0:
            print("Pogresan unos.")
            break

        if isPitagorial(list[0], list[1], list[2]):
            print("Brojevi su pitagorine trojke")
        else:
            print("Brojevi nisu pitagorine trojke")

if __name__ == "__main__":
    main()
