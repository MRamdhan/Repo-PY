rak = [10,10,10,10,10,10,10,10,10,10]
harga_per_tahu = 1000

uang = int(input("Input uang: "))
jumlah_beli = int(input("Jumlah tahu yang akan dibeli: "))

total_harga = jumlah_beli * harga_per_tahu

total_stok = sum(rak)

if jumlah_beli > total_stok:
    print("Stok tahu tidak cukup!")
elif uang < total_harga:
    print("Uang tidak cukup!")
else:
    sisa = jumlah_beli
    for i in range(len(rak)):
        if rak[i] >= sisa:
            rak[i] -= sisa
            break
        else:
            sisa -= rak[i]
            rak[i] = 0

    print(f"Total harga yang dibeli : {total_harga}")
    print(f"Uang Kembali : {uang} - {total_harga}")
    print(f"Sisa Tahu : {sum(rak)}")
    print(f"Posisi Akhir Rak : {rak}")
