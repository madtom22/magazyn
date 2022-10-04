from statistics import quantiles


items = [
{'name':'śrubka','quantity':100,'unit':'szt','unit_price':4},
{'name':'gwóźdz','quantity':500,'unit':'szt','unit_price':1.2},
{'name':'nakrętka','quantity':250,'unit':'szt','unit_price':2},
{'name':'kształtka','quantity':50,'unit':'szt','unit_price':3.5}
]

def get_items():
    print('Name\t\tQuantity\t\tUnit\t\tUnit Price (PLN)')
    print('____\t\t________\t\t____\t\t__________')
    #for name, quantity, unit, unit_price in list(items()):
     #   print(name, quantity, unit, unit_price)

    for i in range(len(items)):
        y = items[i]
        print(y['name'],'\t\t',y['quantity'],'\t\t',y['unit'],'\t\t',y['unit_price'])

if __name__ == "__main__":

    x = str(input('Podaj co chcesz zrobić? '))
    
    while x != 'exit':
        
        if x == 'show':
            print(get_items())
            
        x = str(input('Podaj co chcesz zrobić? '))
    
    print('Koniec...Narka!')