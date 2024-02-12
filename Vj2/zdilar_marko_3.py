def brojSusjednih():
    samoglasnici = ['A', 'E', 'I', 'O', 'U']
    userString = input("Unesite string: ")
    prethodnoSlovo = ''
    brojSusjednihSamoglasnika = 0
    for character in userString:
        character = character.upper()
        if(character in samoglasnici):
            if(character == prethodnoSlovo):
                brojSusjednihSamoglasnika += 1
        prethodnoSlovo = character
        
    return brojSusjednihSamoglasnika

def main():
    print("Broj susjednih samoglasnika je " + str(brojSusjednih()))


if __name__ == "__main__":
    main()