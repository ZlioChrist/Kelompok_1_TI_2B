# Mengimpor Library

import time
import re  # Import modul untuk ekspresi reguler


# Fungsi Quick Sort
# =========================

def quick_sort(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        kiri = [x for x in data[1:] if x <= pivot]
        kanan = [x for x in data[1:] if x > pivot]
        return quick_sort(kiri) + [pivot] + quick_sort(kanan)

# =========================
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

# =========================
# Fungsi untuk membaca dan membersihkan data dari file
# =========================

def baca_data_dari_file():
    try:
        with open("file.txt", "r") as f:
            content = f.read()
            # Menghapus semua karakter selain angka dan spasi
            content = re.sub(r"[^\d\s]", "", content)
            # Mengonversi string yang sudah dibersihkan menjadi list angka
            data = list(map(int, content.split()))
        print(f"✅ Berhasil membaca {len(data)} angka dari file.")
        return data
    except FileNotFoundError:
        print("⚠️ File tidak ditemukan. Pastikan file.txt ada di direktori yang sama dengan program.")
        return []
    except ValueError as e:
        print(f"⚠️ Terjadi kesalahan saat membaca data: {e}")
        return []
    
    # =========================
# Fungsi untuk membandingkan performa Quick Sort vs Bubble Sort
# =========================

def bandingkan_sort_dari_file(data):
    # Membandingkan Quick Sort
    start_time = time.time()
    quick_sorted_data = quick_sort(data.copy())  # Menggunakan copy agar data asli tidak berubah
    quick_sort_time = time.time() - start_time
    print(f"📊 Waktu eksekusi Quick Sort: {quick_sort_time:.6f} detik")

    # Membandingkan Bubble Sort
    start_time = time.time()
    bubble_sorted_data = bubble_sort(data.copy())  # Menggunakan copy agar data asli tidak berubah
    bubble_sort_time = time.time() - start_time
    print(f"📊 Waktu eksekusi Bubble Sort: {bubble_sort_time:.6f} detik")

    # Menampilkan selisih waktu
    selisih = bubble_sort_time - quick_sort_time
    print(f"⏱️ Selisih waktu (Bubble - Quick): {selisih:.6f} detik")

    # Penjelasan alasan selisih waktu
    if selisih > 0:
        # Jika Bubble Sort lebih lama, berarti Quick Sort lebih efisien
        print("📉 Alasan: Quick Sort lebih efisien daripada Bubble Sort untuk data besar, "
              "karena memiliki kompleksitas waktu O(n log n) sementara Bubble Sort O(n^2).")
    elif selisih < 0:
        # Jika Bubble Sort lebih cepat, bisa terjadi pada data kecil atau hampir terurut
        print("📈 Alasan: Dalam beberapa kasus, Bubble Sort bisa lebih cepat untuk data kecil atau hampir terurut, "
              "meskipun secara umum Quick Sort lebih efisien untuk data besar.")
    else:
        # Jika waktu keduanya hampir sama, artinya data tersebut sangat kecil atau sudah terurut
        print("📊 Alasan: Kedua algoritma memerlukan waktu yang hampir sama, bisa terjadi pada data kecil atau terurut.")

# =========================
# Fungsi utama
# =========================

def main():
    # Membaca data dari file.txt
    data_angka = baca_data_dari_file()  # Memanggil fungsi untuk membaca data

    # Jika data valid, lanjutkan ke perbandingan
    if data_angka:
        bandingkan_sort_dari_file(data_angka)  # Melakukan perbandingan algoritma
        
        # =========================
# Menjalankan program
# =========================

if __name__ == "__main__":
    main()