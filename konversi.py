#Program konversi dolar ke rupiah
kursRupiah = 0.000068
#Mendapatkan uang user dengan tipe float supaya dapat menerima bilangan bulat atau desimal
dolar = float(input("masukkan dolar :"))
dolartorupiah = dolar / kursRupiah
#Menggunakan fungsi round untuk membulatkan desimal dengan argumen 2 yang berarti dua angka di belakang koma
rupdecimal = round(dolartorupiah, 2)

print("US$.",dolar, "==> Rupiah", rupdecimal)