#tugas 1 
#soal
""" Seorang dosen ingin merekap nilai mahasiswa. Nilai akhir dihitung dari tugas (bobot 30%),
UTS (bobot 30%), dan UAS (bobot 40%), semuanya dalam skala 0 sampai 100. Nilai huruf ditentukan
sebagai berikut. """


""" Nilaiakhir |  Nilaihuruf """
"""  ≥85       |    A       """
""" 70s.d.<85  |    B       """
""" 55s.d.<70  |    C       """
""" 40s.d.<55  |    D       """
""" <40        |    E       """

""" Mahasiswa dinyatakan lulus jika memperoleh nilai huruf minimal C. Data lima mahasiswa
disimpan dalam daftar berikut pada program Anda. """

""" Nama   |  Tugas  |  UTS  |   UAS     """
""" Andi   |  80     |  70   |  90      """
""" Bunga  |  90     |  85   |  88      """
""" Citra  |  60     |  45   |  50      """
""" Dimas  |  75     |  80   |  65      """
""" Eka    |  30     |  40   |  35      """

""" (a)Tulislah program yang menampilkan tabel rekap berisi nama, nilai akhir, nilai huruf, dan
keterangan lulus atau tidak lulus untuk setiap mahasiswa. Setelah tabel, tampilkan rata
rata nilai akhir kelas dan banyaknya mahasiswa yang lulus. """

""" (b)Program Anda harus memiliki sedikitnya empat fungsi selain main(), dengan sedikitnya
satu fungsi void dan satu fungsi non-void. Buatlah tabel rancangan fungsi dengan kolom:
namafungsi, parameter, mengembalikan nilai atau tidak, dan tugas yang dikerjakan. """

""" (c)Tentukan secara manual nilai akhir dan nilai huruf untuk Andi dan Dimas, lalu bandingkan
dengan ke luaran program Anda. """

""" (d)Dosen meminta tambahan fitur: menampilkan nama mahasiswa dengan nilai akhir tertinggi. 
Jelaskan fungsi apa saja yang perlu Anda tambah atau ubah, dan fungsimana yang
tidak perlu disentuh sama sekali. Kaitkan jawaban Anda dengan cara Anda mengelompokkan kode pada bagian(b) """



bobot_tugas = 30 / 100
bobot_UTS = 30 / 100
bobot_UAS = 40 / 100

data_mahasiswa = [
    ["Andi", 80, 70, 90],
    ["Bunga", 90, 85, 88],
    ["Citra", 60, 45, 50],
    ["Dimas", 75, 80, 65],
    ["Eka", 30, 40, 35],
]

# Pengaturan lebar kolom tabel supaya tanda | selalu lurus
# Nama = 8 karakter, Nilai akhir = 11, Huruf = 5, Keterangan = 11
FORMAT_BARIS = "{:<8} | {:>11} | {:^5} | {:<11}"
GARIS_TABEL = "-" * 9 + "+" + "-" * 13 + "+" + "-" * 7 + "+" + "-" * 12


def hitung_nilai_akhir(tugas, uts, uas):
    """Menghitung nilai akhir berbobot dari nilai tugas, UTS, dan UAS."""
    return (tugas * bobot_tugas) + (uts * bobot_UTS) + (uas * bobot_UAS)


def hitung_nilai_huruf(nilai_akhir):
    """Mengubah nilai akhir menjadi nilai huruf A sampai E."""
    if nilai_akhir >= 85:
        return "A"
    if nilai_akhir >= 70:
        return "B"
    if nilai_akhir >= 55:
        return "C"
    if nilai_akhir >= 40:
        return "D"
    return "E"


def keterangan_lulus_atau_tidak_lulus(nilai_huruf):
    """Menentukan lulus (True) jika nilai huruf minimal C."""
    return nilai_huruf in ("A", "B", "C")


def cek_tabel(data):
    """Mencetak tabel rekap nama, nilai akhir, huruf, dan keterangan."""
    print(FORMAT_BARIS.format("Nama", "Nilai Akhir", "Huruf", "Keterangan"))
    print(GARIS_TABEL)
    for mahasiswa in data:
        nilai_akhir = hitung_nilai_akhir(mahasiswa[1], mahasiswa[2], mahasiswa[3])
        huruf = hitung_nilai_huruf(nilai_akhir)
        if keterangan_lulus_atau_tidak_lulus(huruf):
            keterangan = "Lulus"
        else:
            keterangan = "Tidak Lulus"
        print(FORMAT_BARIS.format(mahasiswa[0], f"{nilai_akhir:.2f}", huruf, keterangan))


def hitung_rata_rata(data):
    """Menghitung rata-rata nilai akhir seluruh mahasiswa."""
    total = 0
    for mahasiswa in data:
        total = total + hitung_nilai_akhir(mahasiswa[1], mahasiswa[2], mahasiswa[3])
    return total / len(data)


def hitung_jumlah_lulus(data):
    """Menghitung banyaknya mahasiswa yang lulus."""
    jumlah = 0
    for mahasiswa in data:
        nilai_akhir = hitung_nilai_akhir(mahasiswa[1], mahasiswa[2], mahasiswa[3])
        huruf = hitung_nilai_huruf(nilai_akhir)
        if keterangan_lulus_atau_tidak_lulus(huruf):
            jumlah = jumlah + 1
    return jumlah


#fitur tambahan bagian (d)
def cari_nilai_tertinggi(data):
    """Mencari nama dan nilai akhir mahasiswa dengan nilai akhir tertinggi."""
    nama_tertinggi = data[0][0]
    nilai_tertinggi = hitung_nilai_akhir(data[0][1], data[0][2], data[0][3])
    for mahasiswa in data:
        nilai_akhir = hitung_nilai_akhir(mahasiswa[1], mahasiswa[2], mahasiswa[3])
        if nilai_akhir > nilai_tertinggi:
            nama_tertinggi = mahasiswa[0]
            nilai_tertinggi = nilai_akhir
    return nama_tertinggi, nilai_tertinggi


def cetak_nilai_tertinggi(nama, nilai_akhir):
    """Mencetak nama dan nilai akhir mahasiswa dengan nilai tertinggi."""
    print("mahasiswa nilai tertinggi   :", nama, "dengan nilai", round(nilai_akhir, 2))
# ------------------------------------------------


def main():
    """Alur utama: cetak tabel, ringkasan kelas, dan mahasiswa tertinggi."""
    cek_tabel(data_mahasiswa)
    print(GARIS_TABEL)
    rata_rata = hitung_rata_rata(data_mahasiswa)
    jumlah_lulus = hitung_jumlah_lulus(data_mahasiswa)
    print("rata-rata nilai akhir kelas :", round(rata_rata, 2))
    print("jumlah mahasiswa yang lulus :", jumlah_lulus, "dari", len(data_mahasiswa))
    # fitur tambahan bagian (d)
    nama, nilai = cari_nilai_tertinggi(data_mahasiswa)
    cetak_nilai_tertinggi(nama, nilai)


if __name__ == "__main__":
    main()




#penjelasan bagian C perbandingan nilai andi dan dimas
""" bagian (C) perbandingan nilai andi dan dimas """
""" Rumus nilai akhir:
     Nilai akhir = 30% x Tugas + 30% x UTS + 40% x UAS
                 = 0,3 x Tugas + 0,3 x UTS + 0,4 x UAS """

""" ANDI (Tugas 80, UTS 70, UAS 90)
Langkah 1, hitung tiap komponen:
     Tugas : 0,3 x 80 = 24
     UTS   : 0,3 x 70 = 21
     UAS   : 0,4 x 90 = 36
Langkah 2, jumlahkan: Nilai akhir = 24 + 21 + 36 = 81
Langkah 3, tentukan huruf:
     81 >= 85 ? tidak
     81 >= 70 ? ya   -> nilai huruf B
Langkah 4, tentukan keterangan: B minimal C, maka LULUS.
Hasil manual Andi: NA = 81, huruf B, Lulus. """

""" DIMAS (Tugas 75, UTS 80, UAS 65)
Langkah 1, hitung tiap komponen:
     Tugas : 0,3 x 75 = 22,5
     UTS   : 0,3 x 80 = 24
     UAS   : 0,4 x 65 = 26
Langkah 2, jumlahkan: NA = 22,5 + 24 + 26 = 72,5
Langkah 3, tentukan huruf:
     72,5 >= 85 ? tidak
     72,5 >= 70 ? ya -> nilai huruf B
Langkah 4, tentukan keterangan: B minimal C, maka LULUS.
Hasil manual Dimas: NA = 72,5, huruf B, Lulus. """

""" Perbandingan dengan keluaran program
     Nama   | Manual          |Keluaran program       | Cocok?
     Andi   | 81   , B, Lulus | 81.00, B, Lulus       | Ya
     Dimas  | 72,5 , B, Lulus | 72.50, B, Lulus       | Ya """


#Penjelasan bagian D fitur tambahan, menampilkan nilai tertinggi, fungsi yang di tambah dan yang tidak perlu
#disentuh sama sekali
""" bagian D fitur tambahan, menampilkan nilai tertinggi, fungsi yang di tambah dan yang tidak perlu
#disentuh sama sekali """

""" Fungsi yang ditambah:
=> cari_nilai_tertinggi(data) (non-void): mencari mahasiswa dengan nilai akhir terbesar, lalu mengembalikan nama dan nilainya.
=> cetak_nilai_tertinggi(nama, nilai_akhir) (void): hanya mencetak hasilnya. """

""" Fungsi yang diubah: hanya main(), dengan menambah pemanggilan kedua fungsi di atas. """

""" Fungsi yang tidak perlu disentuh: hitung_nilai_akhir, hitung_nilai_huruf, keterangan_lulus_atau_tidak_lulus, 
cek_tabel, hitung_rata_rata, dan hitung_jumlah_lulus.
Rumus, batas huruf, syarat lulus, dan tampilan tabel tidak berubah, jadi tidak ada alasan menyentuhnya. """


""" Kaitan dengan pengelompokan kode di bagian (b):
=> Satu fungsi mengerjakan satu tugas. Mencari nilai tertinggi adalah tugas baru, 
jadi dibuatkan fungsi baru dan fungsi lama tidak berisiko rusak.
=> Menghitung dipisah dari menampilkan. Format tampilan bisa diubah tanpa menyentuh logika pencarian.
=> Rumus nilai akhir tidak ditulis ulang. Fitur baru memanggil hitung_nilai_akhir yang sudah ada, 
sehingga nilai tertinggi pasti sama dengan angka di tabel. """