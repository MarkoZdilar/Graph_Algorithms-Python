def brojevni_trokut():
    rows = int(input('Enter number of rows: '))
    
    if( rows < 20 ):
        for i in range (1, rows + 1):
            list = []
            columns = (i + ( i - 1 ))

            for j in range (i, columns + 1):
                list.append(j % 10)
                
            for j in range (columns - 1, i - 1, -1):
                list.append(j % 10)
            
            print(list) 

def main():
    brojevni_trokut()

if __name__ == "__main__":
    main()




