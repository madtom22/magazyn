from tkinter import E

items = [
{'name':'śrubka','quantity':100,'unit':'szt','unit_price':4},
{'name':'gwóźdz','quantity':500,'unit':'szt','unit_price':1.2},
{'name':'nakrętka','quantity':250,'unit':'szt','unit_price':2},
{'name':'kształtka','quantity':50,'unit':'szt','unit_price':3.5}
]
    


if __name__ == "__main__":

    x = str(input('Podaj co chcesz zrobić? '))
    
    while x != 'exit':
        
        if x == 'show':
            print(items)
        x = str(input('Podaj co chcesz zrobić? '))
    
    print('Koniec...Narka!')