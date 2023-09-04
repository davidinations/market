import main as m

def show(listBuah, listHarga, listStock):
    print(f'''\nDaftar Buah \n
Index \t | Buah \t | Harga \t | Stock ''')
    for i in range(len(listBuah)):
        print(f'{i} \t | {listBuah[i]} \t | {listHarga[i]} \t | {listStock[i]}')
    print('\n')

def add(listBuah, listHarga, listStock):
    namaBuah = input('Masukkan Nama Buah: ')
    stockBuah = int(input('Masukkan Stock Buah: '))
    hargaBuah = int(input('Masukkan Harga Buah: '))
    listBuah.append(namaBuah)
    listHarga.append(hargaBuah)
    listStock.append(stockBuah)
    print(f'''Daftar Buah \n
Index \t | Buah \t | Harga \t | Stock ''')
    for i in range(len(listBuah)):
        print(f'{i} \t | {listBuah[i]} \t | {listHarga[i]} \t | {listStock[i]}')
    print('\n')

def remove(listBuah, listHarga, listStock):
    namaBuah = input('Masukkan Nama Buah: ')
    listBuah.remove(namaBuah)
    print(f'''Daftar Buah \n
Index \t | Buah \t | Harga \t | Stock ''')
    for i in range(len(listBuah)):
        print(f'{i} \t | {listBuah[i]} \t | {listHarga[i]} \t | {listStock[i]}')
    print('\n')
    
def payment(totalPriceOverall):
    while True:
        payment = int(input("Masukkan Jumlah Uang : "))
        print(f'Masukkan Jumlah Uang : {payment}')
        if payment < totalPriceOverall:
            print(f'Uang Anda Kurang Sebesar {totalPriceOverall-payment}\n')
            continue
        else:
            print(f'Terima Kasih')
            if payment != totalPriceOverall:
                print(f'\nUang Kembalian Anda : {payment-totalPriceOverall}')
            break

def buy(listBuah, listHarga, listStock, keranjangBuah, keranjangHarga, keranjangStock, keranjangTotal):
    print(f'''Daftar Buah \n
Index \t | Buah \t | Harga \t | Stock ''')
    for i in range(len(listBuah)):
        print(f'{i} \t | {listBuah[i]} \t | {listHarga[i]} \t | {listStock[i]}')
    print('\nMasukkan Index Buah yang ingin dibeli: ')
    indexBuah = int(input())
    print(f'Anda membeli {listBuah[indexBuah]} sebanyak: ')
    jumlahBuah = int(input())
    if jumlahBuah > listStock[indexBuah]:
        print('Stock Tidak Mencukupi')
        print(f'''Keranjang Buah \n
Index \t | Buah \t | Harga \t | Stock \t | Total ''')
        for i in range(len(keranjangBuah)):
            print(f'{i} \t | {keranjangBuah[i]} \t | {keranjangHarga[i]} \t | {keranjangStock[i]} \t | {keranjangTotal[i]}')
        print('\n')
        print(f'Apakah Anda ingin membeli buah lain? (y/n)')
        inputan = input()
        if inputan == 'y':
            buy(listBuah, listHarga, listStock, keranjangBuah, keranjangHarga, keranjangStock, keranjangTotal)
        else:
            if len(keranjangBuah) == 0:
                m.main()
            else:
                print(f'''Keranjang Buah \n
Index \t | Buah \t | Harga \t | Stock \t | Total ''')
                for i in range(len(keranjangBuah)):
                    print(f'{i} \t | {keranjangBuah[i]} \t | {keranjangHarga[i]} \t | {keranjangStock[i]} \t\t | {keranjangTotal[i]}')
                print('\n')
                print(f'Total Harga : {sum(keranjangTotal)}')
                totalPriceOverall = sum(keranjangTotal)
                payment(totalPriceOverall)
    else:
        keranjangBuah.append(listBuah[indexBuah])
        keranjangHarga.append(listHarga[indexBuah])
        keranjangStock.append(jumlahBuah)
        keranjangTotal.append(listHarga[indexBuah]*jumlahBuah)
        listStock[indexBuah] -= jumlahBuah
        print(f'''Keranjang Buah \n
Index \t | Buah \t | Harga \t | Stock \t | Total ''')
        for i in range(len(keranjangBuah)):
            print(f'{i} \t | {keranjangBuah[i]} \t | {keranjangHarga[i]} \t | {keranjangStock[i]} \t\t | {keranjangTotal[i]}')
        print('\n')
        print(f'Apakah Anda ingin membeli buah lain? (y/n)')
        inputan = input()
        if inputan == 'y':
            buy(listBuah, listHarga, listStock, keranjangBuah, keranjangHarga, keranjangStock, keranjangTotal)
        else:
            if len(keranjangBuah) == 0:
                m.main()
            else:
                print(f'''Keranjang Buah \n
Index \t | Buah \t | Harga \t | Stock \t | Total ''')
                for i in range(len(keranjangBuah)):
                    print(f'{i} \t | {keranjangBuah[i]} \t | {keranjangHarga[i]} \t | {keranjangStock[i]} \t\t | {keranjangTotal[i]}')
                print('\n')
                print(f'Total Harga : {sum(keranjangTotal)}')
                totalPriceOverall = sum(keranjangTotal)
                payment(totalPriceOverall)

            
        
