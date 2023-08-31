stockApel = 7
stockJeruk = 7
stockAnggur = 6

while True:
    nApel = int(input("Masukkan jumlah apel: "))
    print(f'Masukkan jumlah apel : {nApel}')
    if nApel >= 8:
        print(f'Jumlah yang dimasukkan terlalu banyak. stock Apel Tinggal {stockApel}')
        continue
    else:
        stockApel -= nApel
        break

while True:
    nJeruk = int(input("Masukkan jumlah jeruk: "))
    print(f'Masukkan jumlah jeruk : {nJeruk}')
    if nJeruk >= 8:
        print(f'Jumlah yang dimasukkan terlalu banyak stock Jeruk Tinggal {stockJeruk}')
        continue
    else:
        stockJeruk -= nJeruk
        break

while True:
    nAnggur = int(input("Masukkan jumlah anggur: "))
    print(f'Masukkan jumlah apel : {nAnggur}')
    if nAnggur >= 7:
        print(f'Jumlah yang dimasukkan terlalu banyak stock Anggur Tinggal {stockAnggur}')
        continue
    else:
        stockAnggur -= nAnggur
        break

# Harga buah
priceApel = 10000
priceJeruk = 15000
priceAnggur = 20000

# Total buah
totalPriceApel = nApel * priceApel
totalPriceJeruk = nJeruk * priceJeruk
totalPriceAnggur = nAnggur * priceAnggur

# Total harga
totalPriceOverall = totalPriceApel + totalPriceJeruk + totalPriceAnggur

# Output
print(
f'''
Detail Belanja \n
Apel: {nApel} x {priceApel} = {totalPriceApel}
Jeruk: {nJeruk} x {priceJeruk} = {totalPriceJeruk}
Anggur: {nAnggur} x {priceAnggur} = {totalPriceAnggur} \n
Total: {totalPriceOverall}
'''
)

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



