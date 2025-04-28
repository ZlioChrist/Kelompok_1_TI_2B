# =========================
# Mengimpor Library
# =========================

from collections import deque  # Mengimpor deque dari modul collections, untuk antrian fleksibel (bisa tambah/hapus dari dua sisi)
from queue import Queue        # Mengimpor Queue dari modul queue, untuk antrian FIFO standar
import time                    # Mengimpor modul time, untuk mensimulasikan delay waktu

# =========================
# Fungsi Quick Sort
# =========================
def quick_sort(data):
    """
    Fungsi untuk mengurutkan data menggunakan algoritma Quick Sort.
    """
    if len(data) <= 1:  # Jika data kosong atau hanya 1 elemen, langsung kembalikan
        return data
    else:
        pivot = data[0]  # Pilih elemen pertama sebagai pivot
        kiri = [x for x in data[1:] if x <= pivot]  # Semua elemen lebih kecil/sama dari pivot
        kanan = [x for x in data[1:] if x > pivot]  # Semua elemen lebih besar dari pivot
        # Gabungkan hasil rekursif kiri + pivot + kanan
        return quick_sort(kiri) + [pivot] + quick_sort(kanan)

# =========================
# Kelas Antrian dengan Stack
# =========================
class AntrianPasienStack:
    def __init__(self):
        self.stack = []  # Inisialisasi stack kosong

    def daftar_pasien(self, nama):
        self.stack.append(nama)  # Tambahkan pasien ke atas stack
        print(f"✅ {nama} telah ditambahkan ke antrian (Stack).")

    def panggil_pasien(self):
        if self.isEmpty():  # Cek apakah stack kosong
            print("⚠️ Tidak ada pasien dalam antrian.")
            return
        print("🔔 Memanggil pasien... Mohon tunggu...")
        time.sleep(2)  # Delay 2 detik
        pasien = self.stack.pop()  # Hapus dan ambil pasien dari atas stack
        print(f"🔔 Pasien {pasien} dipanggil (Stack).")

    def pasien_berikutnya(self):
        if self.isEmpty():
            print("⚠️ Tidak ada pasien dalam antrian.")
            return
        print(f"🔎 Pasien berikutnya: {self.stack[-1]} (Stack)")  # Lihat pasien paling atas

    def isEmpty(self):
        return len(self.stack) == 0  # Return True jika stack kosong

    def lihat_antrian(self):
        if self.isEmpty():
            print("⚠️ Tidak ada pasien dalam antrian.")
        else:
            print("📋 Daftar antrian (Stack):", " -> ".join(self.stack))

    def sort_antrian(self):
        if self.isEmpty():
            print("⚠️ Tidak ada pasien untuk diurutkan.")
        else:
            self.stack = quick_sort(self.stack)  # Urutkan stack
            print("✅ Antrian telah diurutkan menggunakan Quick Sort (Stack).")

# =========================
# Kelas Antrian dengan Queue
# =========================
class AntrianPasienQueue:
    def __init__(self):
        self.queue = Queue()  # Inisialisasi queue kosong (FIFO)

    def daftar_pasien(self, nama):
        self.queue.put(nama)  # Tambahkan pasien ke belakang queue
        print(f"✅ {nama} telah ditambahkan ke antrian (Queue).")

    def panggil_pasien(self):
        if self.isEmpty():
            print("⚠️ Tidak ada pasien dalam antrian.")
            return
        print("🔔 Memanggil pasien... Mohon tunggu...")
        time.sleep(2)  # Delay 2 detik
        pasien = self.queue.get()  # Ambil pasien dari depan queue
        print(f"🔔 Pasien {pasien} dipanggil (Queue).")

    def pasien_berikutnya(self):
        print(f"⚠️ Queue bawaan tidak mendukung melihat pasien berikutnya secara langsung.")  # Tidak ada fungsi 'peek'

    def isEmpty(self):
        return self.queue.empty()  # Cek apakah queue kosong

    def lihat_antrian(self):
        print(f"⚠️ Queue bawaan tidak mendukung melihat seluruh isi antrian secara langsung.")  # Tidak bisa akses langsung elemen

    def sort_antrian(self):
        print(f"⚠️ Queue bawaan tidak mendukung pengurutan secara langsung.")  # Tidak bisa diurutkan langsung

# =========================
# Kelas Antrian dengan Deque
# =========================
class AntrianPasienDeque:
    def __init__(self):
        self.deque = deque()  # Inisialisasi deque kosong

    def daftar_pasien(self, nama):
        self.deque.append(nama)  # Tambahkan pasien ke kanan deque
        print(f"✅ {nama} telah ditambahkan ke antrian (Deque).")

    def panggil_pasien(self):
        if self.isEmpty():
            print("⚠️ Tidak ada pasien dalam antrian.")
            return
        print("🔔 Memanggil pasien... Mohon tunggu...")
        time.sleep(2)  # Delay 2 detik
        pasien = self.deque.popleft()  # Ambil pasien dari kiri deque
        print(f"🔔 Pasien {pasien} dipanggil (Deque).")

    def pasien_berikutnya(self):
        if self.isEmpty():
            print("⚠️ Tidak ada pasien dalam antrian.")
            return
        print(f"🔎 Pasien berikutnya: {self.deque[0]} (Deque)")  # Lihat pasien di depan

    def isEmpty(self):
        return len(self.deque) == 0  # Return True jika deque kosong

    def lihat_antrian(self):
        if self.isEmpty():
            print("⚠️ Tidak ada pasien dalam antrian.")
        else:
            print("📋 Daftar antrian (Deque):", " -> ".join(self.deque))

    def sort_antrian(self):
        if self.isEmpty():
            print("⚠️ Tidak ada pasien untuk diurutkan.")
        else:
            sorted_list = quick_sort(list(self.deque))  # Ubah deque ke list dan urutkan
            self.deque = deque(sorted_list)  # Ubah kembali ke deque
            print("✅ Antrian telah diurutkan menggunakan Quick Sort (Deque).")

# =========================
# Fungsi memilih struktur data
# =========================
def pilih_struktur_data():
    """
    Fungsi untuk memilih jenis struktur data antrian.
    """
    print("\nPilih struktur data untuk antrian:")
    print("1. Stack (LIFO - Last In First Out)")
    print("2. Queue (FIFO - First In First Out)")
    print("3. Deque (Double Ended Queue - FIFO)")

    pilihan = input("Pilihan (1/2/3): ")

    if pilihan == "1":
        return AntrianPasienStack()
    elif pilihan == "2":
        return AntrianPasienQueue()
    elif pilihan == "3":
        return AntrianPasienDeque()
    else:
        print("❌ Pilihan tidak valid. Default ke Stack.")
        return AntrianPasienStack()

# =========================
# Fungsi utama
# =========================
def main():
    rs = pilih_struktur_data()  # Memilih struktur data

    while True:  # Loop utama
        print("\n===== 🟢 SISTEM ANTRIAN PASIEN =====")
        print("1. ➕ Tambah Pasien")
        print("2. 📞 Panggil Pasien (dengan Delay)")
        print("3. 🔎 Lihat Pasien Berikutnya")
        print("4. 📋 Lihat Daftar Antrian")
        print("5. 🔀 Urutkan Daftar Antrian (Quick Sort)")
        print("6. ❌ Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            nama = input("Masukkan nama pasien: ")
            rs.daftar_pasien(nama)
        elif pilihan == "2":
            rs.panggil_pasien()
        elif pilihan == "3":
            rs.pasien_berikutnya()
        elif pilihan == "4":
            rs.lihat_antrian()
        elif pilihan == "5":
            rs.sort_antrian()
        elif pilihan == "6":
            print("👋 Terima kasih! Program selesai.")
            break  # Keluar dari program
        else:
            print("❌ Pilihan tidak valid. Silakan coba lagi.")

# =========================
# Menjalankan program
# =========================
if __name__ == "__main__":
    main()
