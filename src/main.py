import fruitmarket as fm

# List Buah
listBuah = ['Apel', 'Jeruk', 'Anggur']
# List Harga
listHarga = [10000, 15000, 20000]
# List Stock
listStock = [10, 10, 10]

# List Keranjang
keranjangBuah = []
keranjangHarga = []
keranjangStock = []
keranjangTotal = []

# define PROMPT message
PROMPT = '''Selamat Datang Di Pasar Buah \n
List Menu:
1. Menampilkan Daftar Buah
2. Menambah Buah
3. Menghapus Buah
4. Membeli Buah
5. Exit The Program
Masukkan Angka Menu yang ingin dijalankan: '''

def main():
    while True:
        inputan = int(input(PROMPT))
        if inputan == 1:
            fm.show(listBuah, listHarga, listStock)
            continue

        elif inputan == 2:
            fm.add(listBuah, listHarga, listStock)
            continue

        elif inputan == 3:
            fm.remove(listBuah, listHarga, listStock)
            continue

        elif inputan == 4:
            fm.buy(listBuah, listHarga, listStock, keranjangBuah, keranjangHarga, keranjangStock, keranjangTotal)
            continue

        elif inputan == 5:
            exit()

if __name__ == '__main__':
        main()