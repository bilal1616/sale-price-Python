from math import *

while True:
    
    def main():
        alis = float(input("Alış Fiyatı: "))
        kdv = float(input("KDV: "))
        
        print("Kdvli Alış Tutarı: ")
        print(alis * kdv)
        print("TL")
        print("Toplam Satış Fiyatı: ")
        print((alis * kdv)*2)
        print("TL")
        
    main()
    
else:
    pass