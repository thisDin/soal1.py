#tugas 2
#soal 
""" Sebuah toko daring menentukan ongkos kirim berdasarkan berat paket (bilangan bulat, dalam
kg) dan jarak pengiriman (dalam km)."""

""" => Biaya berat: Rp10.000 untuk paket hingga 2 kg. Untuk setiap kg selebihnya ditambah
Rp4.000. """
""" => Biaya jarak: tidak ada biaya tambahan jika jarak tidak lebih dari 20 km, dan Rp5.000 jika
jarak lebih dari 20 km """
""" => Ongkos kirim adalah jumlah biaya berat dan biaya jarak. Pelanggan yang berstatus anggota
mendapat potongan 10% dari ongkos kirim. """

""" Toko memiliki daftar pesanan hari ini sebagai berikut."""

"""  Pelanggan     Berat(kg)     Jarak(km)     Anggota  """
"""  Rina            1             10           Bukan   """
"""  Sari            5             25           Bukan   """
"""  Tono            5             25            Ya     """
"""  Umar            2             30            Ya     """
"""  Vina            8             15           Bukan   """

""" (a) Tulislah program yang mencetak struk untuk setiap pesanan, berisi nama pelanggan, biaya
berat, biaya jarak, potongan (jika ada), dan ongkos kirim akhir. Setelah semua struk, cetak
total pendapatan ongkos kirim hari ini."""
""" (b) Rancang pembagian program ke dalam fungsi-fungsi. Seperti pada Soal 1, sertakan tabel
rancangan fungsi (nama fungsi, parameter, mengembalikan nilai atau tidak, tugas yang
dikerjakan). Terdapat sedikitnya satu fungsi void dan satu fungsi non-void. """
""" (c) Tentukan secara manual ongkos kirim akhir untuk pesanan Sari, Tono, dan Umar, lalu
buktikan bahwa program Anda memberikan hasil yang sama. """
""" (d) Toko mengubah kebijakan: batas jarak menjadi 15 km dan biaya tambahan jarak menjadi
Rp7.000. Tunjukkan bagian kode yang harus Anda ubah. Jika Anda harus mengubah
lebih dari satu tempat untuk satu perubahan aturan, jelaskan bagaimana pengelompokan
kode dapat diperbaiki """




batas_berat_kg = 2            # paket sampai 2 kg kena tarif dasar
biaya_berat_dasar = 10_000    # tarif dasar
biaya_per_kg = 4_000          # tambahan tiap kg di atas 2 kg
batas_jarak_km = 20           # jarak sampai 20 km tidak kena biaya tambahan
biaya_jarak_tambahan = 5_000  # biaya tambahan jika jarak lebih dari 20 km
diskon_anggota = 10           # potongan anggota 10%

# Format tiap pesanan: [nama, berat_kg, jarak_km, anggota]
daftar_pesanan = [
    ["Rina", 1, 10, False],
    ["Sari", 5, 25, False],
    ["Tono", 5, 25, True],
    ["Umar", 2, 30, True],
    ["Vina", 8, 15, False],
]


def hitung_biaya_berat_paket(berat):
    """Biaya berat: tarif dasar + (kelebihan kg x tarif per kg)."""
    if berat <= batas_berat_kg:
        return biaya_berat_dasar
    kelebihan = berat - batas_berat_kg
    return biaya_berat_dasar + kelebihan * biaya_per_kg


def hitung_biaya_jarak(jarak):
    """Biaya jarak: tambahan hanya jika jarak LEBIH DARI batas.

    Soal bilang "lebih dari 20 km", jadi pakai '>' (tepat 20 km masih gratis).
    """
    if jarak > batas_jarak_km:
        return biaya_jarak_tambahan
    return 0


def hitung_potongan(ongkos, anggota):
    """Potongan 10% dari ongkos kirim, hanya untuk anggota."""
    if anggota:
        return ongkos * diskon_anggota // 100
    return 0


def hitung_rincian(berat, jarak, anggota):
    """Menghitung semua komponen ongkir sekaligus.
    Mengembalikan: (biaya_berat, biaya_jarak, potongan, ongkos_akhir)
    """
    biaya_berat = hitung_biaya_berat_paket(berat)
    biaya_jarak = hitung_biaya_jarak(jarak)
    potongan = hitung_potongan(biaya_berat + biaya_jarak, anggota)
    ongkos_akhir = biaya_berat + biaya_jarak - potongan
    return biaya_berat, biaya_jarak, potongan, ongkos_akhir


def hitung_total_pendapatan(data):
    """Menjumlahkan ongkos akhir semua pesanan (memakai hitung_rincian)."""
    total = 0
    for nama, berat, jarak, anggota in data:
        total = total + hitung_rincian(berat, jarak, anggota)[3]
    return total


def format_rupiah(jumlah):
    """Mengubah 27000 menjadi 'Rp27.000'.

    BUG DIPERBAIKI: kode lama
        f"{jumlah:}". teks.replace(",", ".")
    menyebabkan error karena 'teks' bukan atribut string, dan format ':'
    tanpa koma tidak membuat pemisah ribuan. Yang benar:
        f"{jumlah:,}".replace(",", ".")
    ':,' membuat pemisah ribuan berupa koma (27,000), lalu koma diganti
    titik sesuai penulisan rupiah Indonesia (27.000).
    """
    return "Rp" + f"{jumlah:,}".replace(",", ".")


def cetak_struk(nama, biaya_berat, biaya_jarak, potongan, ongkos_akhir):
    """Mencetak satu struk pengiriman (void: hanya print, tanpa return)."""
    print(f"Pelanggan   : {nama}")
    print(f"Biaya berat : {format_rupiah(biaya_berat)}")
    print(f"Biaya jarak : {format_rupiah(biaya_jarak)}")
    if potongan > 0:  # baris potongan hanya dicetak jika ada potongan
        print(f"Potongan    : -{format_rupiah(potongan)}")
    # PERBAIKAN: typo "Ongkos akhi" -> "Ongkos akhir"
    print(f"Ongkos akhir: {format_rupiah(ongkos_akhir)}")
    print("-" * 30)


def main():
    """Alur utama: cetak struk setiap pesanan, lalu total pendapatan.

    PERBAIKAN: rumus tidak lagi ditulis ulang di sini. main() cukup
    memanggil hitung_rincian() lalu mencetak hasilnya. Total pendapatan
    dihitung oleh hitung_total_pendapatan() sehingga fungsi itu terpakai.
    """
    for nama, berat, jarak, anggota in daftar_pesanan:
        biaya_berat, biaya_jarak, potongan, ongkos_akhir = hitung_rincian(
            berat, jarak, anggota
        )
        cetak_struk(nama, biaya_berat, biaya_jarak, potongan, ongkos_akhir)

    total = hitung_total_pendapatan(daftar_pesanan)
    print(f"Total pendapatan ongkos kirim: {format_rupiah(total)}")


if __name__ == "__main__":
    main()



#penjelasan bagian C bukti manual
""" (c) bukti manual (aturan awal: batas 20 km, tambahan Rp5.000)
Sari  (5 kg, 25 km, bukan anggota)
  Biaya berat = 10.000 + (5-2) x 4.000 = 10.000 + 12.000 = 22.000
  Biaya jarak = 25 > 20  -> 5.000
  Ongkos      = 22.000 + 5.000 
              = 27.000
  Potongan    = 0
  Ongkos akhir = Rp27.000

Tono  (5 kg, 25 km, anggota)
  Biaya berat = 22.000 ; Biaya jarak = 5.000 ; Ongkos = 27.000
  Potongan    = 10% x 27.000 
              = 2.700
  Ongkos akhir= 27.000 - 2.700 
              = Rp24.300

Umar  (2 kg, 30 km, anggota)
  Biaya berat = 10.000 (2 kg masih tarif dasar)
  Biaya jarak = 30 > 20 -> 5.000
  Ongkos      = 15.000
  Potongan    = 10% x 15.000 
              = 1.500
  Ongkos akhir= 15.000 - 1.500 
              = Rp13.500

Program menghasilkan angka yang sama persis: 
rina: Rp10.000, sari: Rp27.000, tono: Rp24.300 ,umar: Rp13.500, vina: Rp34.000 = Rp108.800. """

#penjelasan bagian D 
""" (d) kebijakan baru (batas 15 km, tambahan Rp7.000)
Yang diubah hanya dua baris di bagian konstanta:

    batas_jarak_km = 15
    biaya_jarak_tambahan = 7_000

tidak ada fungsi yang perlu disentuh, karena semua fungsi membaca konstanta
dan rumus ongkir hanya ada di satu tempat (hitung_rincian). Itulah
pengelompokan kode yang baik: satu perubahan aturan = satu tempat perubahan.

Catatan: pada kode awal, rumus ongkir tertulis di dua tempat (main dan
hitung_ongkos_akhir). Itu yang harus diperbaiki dengan menjadikan
hitung_rincian sebagai satu-satunya sumber rumus.

Hasil dengan aturan baru (Vina 15 km tetap gratis karena 15 tidak > 15):
Sari = 29.000 ; Tono = 26.100 ; Umar = 15.300 ; Rina = 10.000 ; Vina = 34.000 
Total = Rp114.400 """

