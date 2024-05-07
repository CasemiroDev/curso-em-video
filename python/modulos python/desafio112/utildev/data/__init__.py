def readmoney(a):
    valid = False
    while valid != True:
        entry = str(input(a)).replace(",",".").strip()
        if entry.isalpha or entry == '':
            print("Erro valor inválido.")
        else:
            valid = True
            return float(entry)