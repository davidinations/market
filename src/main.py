# Input User 
nApel = int(input("Masukkan jumlah apel: "))
nJeruk = int(input("Masukkan jumlah jeruk: "))
nAnggur = int(input("Masukkan jumlah anggur: "))

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
Detail Belanja

Apel: {nApel} x {priceApel} = {totalPriceApel}
Jeruk: {nJeruk} x {priceJeruk} = {totalPriceJeruk}
Anggur: {nAnggur} x {priceAnggur} = {totalPriceAnggur}
Total: {totalPriceOverall}
'''
)
