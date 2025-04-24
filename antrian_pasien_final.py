# Mengimpor deque dari modul collections
from collections import deque

# Mengimpor Queue dari modul queue
from queue import Queue


# =========================
# Kelas Antrian menggunakan Stack (LIFO)
# =========================
class AntrianPasienStack:
    def __init__(self):
        self.stack = []  # Inisialisasi list kosong sebagai stack

    def daftar_pasien(self, nama):
        self.stack.append(nama)  # Menambahkan nama ke akhir list (push)
        print(f"✅ {nama} telah ditambahkan ke antrian (Stack).")  # Konfirmasi

    def panggil_pasien(self):
        if self.isEmpty():  # Jika stack kosong
            print("⚠️ Tidak ada pasien dalam antrian.")
            return
        pasien = self.stack.pop()  # Menghapus dan mengambil elemen terakhir
        print(f"🔔 Pasien {pasien} dipanggil (Stack).")  # Menampilkan siapa yang dipanggil

    def pasien_berikutnya(self):
        if self.isEmpty():  # Jika kosong
            print("⚠️ Tidak ada pasien dalam antrian.")
            return
        print(f"🔎 Pasien berikutnya: {self.stack[-1]} (Stack)")  # Melihat elemen terakhir tanpa menghapus (peek)

    def isEmpty(self):
        return len(self.stack) == 0  # True jika panjang stack 0 (kosong)

    def lihat_antrian(self):
        if self.isEmpty():  # Cek apakah kosong
            print("⚠️ Tidak ada pasien dalam antrian.")
        else:
            print("📋 Daftar antrian (Stack):", " -> ".join(self.stack))  # Gabungkan nama-nama dalam stack dengan panah


# =========================
# Kelas Antrian menggunakan Queue (FIFO)
# =========================
class AntrianPasienQueue:
    def __init__(self):
        self.queue = Queue()  # Membuat objek Queue dari modul queue

    def daftar_pasien(self, nama):
        self.queue.put(nama)  # Menambahkan nama ke antrian
        print(f"✅ {nama} telah ditambahkan ke antrian (Queue).")  # Konfirmasi

    def panggil_pasien(self):
        if self.isEmpty():  # Jika antrian kosong
            print("⚠️ Tidak ada pasien dalam antrian.")
            return
        pasien = self.queue.get()  # Mengambil pasien dari depan antrian
        print(f"🔔 Pasien {pasien} dipanggil (Queue).")  # Tampilkan pasien yang dipanggil

    def pasien_berikutnya(self):
        print(f"⚠️ Queue bawaan tidak mendukung melihat pasien berikutnya secara langsung (tanpa akses internal).")

    def isEmpty(self):
        return self.queue.empty()  # Mengembalikan True jika antrian kosong

    def lihat_antrian(self):
        print(f"⚠️ Queue bawaan tidak mendukung melihat seluruh isi antrian secara langsung.")  # Tidak bisa akses isi langsung


# =========================
# Kelas Antrian menggunakan Deque (Double-ended Queue)
# =========================
class AntrianPasienDeque:
    def __init__(self):
        self.deque = deque()  # Membuat deque kosong

    def daftar_pasien(self, nama):
        self.deque.append(nama)  # Menambahkan nama ke kanan (akhir antrian)
        print(f"✅ {nama} telah ditambahkan ke antrian (Deque).")  # Konfirmasi

    def panggil_pasien(self):
        if self.isEmpty():  # Jika deque kosong
            print("⚠️ Tidak ada pasien dalam antrian.")
            return
        pasien = self.deque.popleft()  # Mengambil dan menghapus pasien dari kiri (depan)
        print(f"🔔 Pasien {pasien} dipanggil (Deque).")  # Tampilkan pasien yang dipanggil

    def pasien_berikutnya(self):
        if self.isEmpty():  # Cek apakah deque kosong
            print("⚠️ Tidak ada pasien dalam antrian.")
            return
        print(f"🔎 Pasien berikutnya: {self.deque[0]} (Deque)")  # Tampilkan pasien paling depan (peek)

    def isEmpty(self):
        return len(self.deque) == 0  # True jika deque kosong

    def lihat_antrian(self):
        if self.isEmpty():  # Cek apakah kosong
            print("⚠️ Tidak ada pasien dalam antrian.")
        else:
            print("📋 Daftar antrian (Deque):", " -> ".join(self.deque))  # Gabungkan isi deque menjadi string


# =========================
# Fungsi untuk memilih jenis struktur data
# =========================
def pilih_struktur_data():
    print("\nPilih struktur data untuk antrian:")
    print("1. Stack (LIFO - Last In First Out)")  # Opsi 1: Stack
    print("2. Queue (FIFO - First In First Out)")  # Opsi 2: Queue
    print("3. Deque (Double Ended Queue - FIFO)")  # Opsi 3: Deque
    pilihan = input("Pilihan (1/2/3): ")  # Ambil input pilihan

    if pilihan == "1":
        return AntrianPasienStack()  # Kembalikan objek Stack
    elif pilihan == "2":
        return AntrianPasienQueue()  # Kembalikan objek Queue
    elif pilihan == "3":
        return AntrianPasienDeque()  # Kembalikan objek Deque
    else:
        print("❌ Pilihan tidak valid. Default ke Stack.")  # Jika salah input, pakai Stack
        return AntrianPasienStack()


# =========================
# Fungsi utama (main program)
# =========================
def main():
    rs = pilih_struktur_data()  # Memilih dan membuat objek antrian

    while True:  # Loop tak terbatas sampai user keluar
        print("\n===== 🟢 SISTEM ANTRIAN PASIEN =====")
        print("1. ➕ Tambah Pasien")  # Menu 1
        print("2. 📞 Panggil Pasien")  # Menu 2
        print("3. 🔎 Lihat Pasien Berikutnya")  # Menu 3
        print("4. 📋 Lihat Daftar Antrian")  # Menu 4
        print("5. ❌ Keluar")  # Menu 5

        pilihan = input("Pilih menu (1-5): ")  # Ambil pilihan user

        if pilihan == "1":
            nama = input("Masukkan nama pasien: ")  # Input nama pasien
            rs.daftar_pasien(nama)  # Tambah ke antrian
        elif pilihan == "2":
            rs.panggil_pasien()  # Panggil pasien
        elif pilihan == "3":
            rs.pasien_berikutnya()  # Lihat pasien berikutnya
        elif pilihan == "4":
            rs.lihat_antrian()  # Lihat semua antrian
        elif pilihan == "5":
            print("👋 Terima kasih! Program selesai.")  # Keluar
            break  # Akhiri loop
        else:
            print("❌ Pilihan tidak valid. Silakan coba lagi.")  # Validasi input


# =========================
# Menjalankan program jika file ini dijalankan langsung
# =========================
if __name__ == "__main__":
    main()  # Menjalankan fungsi utama
