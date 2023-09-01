# Program Lama

# while True:
#     nApel = int(input("Masukkan Jumlah Apel : "))
#     print(f'Masukkan Jumlah Apel : {nApel}')
#     if nApel >= stockApel:
#         print(f'Jumlah yang dimasukkan terlalu banyak. stock Apel Tinggal {stockApel}')
#         continue
#     else:
#         stockApel -= nApel
#         break
    
# while True:
#     nJeruk = int(input("Masukkan Jumlah Jeruk : "))
#     print(f'Masukkan Jumlah Jeruk : {nJeruk}')
#     if nJeruk >= stockJeruk:
#         print(f'Jumlah yang dimasukkan terlalu banyak. stock Jeruk Tinggal {stockJeruk}')
#         continue
#     else:
#         stockJeruk -= nJeruk
#         break

# while True:
#     nAnggur = int(input("Masukkan Jumlah Anggur : "))
#     print(f'Masukkan Jumlah Anggur : {nAnggur}')
#     if nAnggur >= stockAnggur:
#         print(f'Jumlah yang dimasukkan terlalu banyak. stock Anggur Tinggal {stockAnggur}')
#         continue
#     else:
#         stockAnggur -= nAnggur
#         break


# Program Baru
def input_fruit(name, stock, price):  
    """
    _Summary_

    Args:
        name (str): definisikan nama buah yang sesuai dengan variabel yang ada
        stock (int): definisikan jumlah stok buah yang ada pada variabel stock
        price (int): definisikan harga buah yang ada pada variabel price

    Returns:
        totalHargaPerBuah (int): mengembalikan total harga masing masing buah
    """    
    while True:
        n = int(input(f"Masukkan Jumlah {name.capitalize()} : "))
        if n >= stock:
            print(f'Jumlah yang dimasukkan terlalu banyak. stock {name.capitalize()} Tinggal {stock}')
            continue
        else:
            price = n * price
            stock -= n
            break
    return price, n

# Stock dan Harga
stockApel = 10
stockJeruk = 10
stockAnggur = 10

priceApel = 10000
priceJeruk = 15000
priceAnggur = 20000

# Total harga masing masing buah dan keseluruhan buah
totalPriceApel, nApel = input_fruit('apel', stockApel, priceApel)
totalPriceJeruk, nJeruk = input_fruit('jeruk', stockJeruk, priceJeruk)
totalPriceAnggur, nAnggur = input_fruit('anggur', stockAnggur, priceAnggur)
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



