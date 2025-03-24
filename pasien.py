
class AntrianPasien:
    def __init__(self):
        self.stack = []  # List sebagai Stack untuk menyimpan pasien

    # Menambahkan pasien ke antrian (Push)
    def daftar_pasien(self, nama):
        self.stack.append(nama)
        print(f"✅ {nama} telah ditambahkan ke antrian.")

    # Memanggil pasien (Pop)
    def panggil_pasien(self):
        if self.isEmpty():
            print("⚠️ Tidak ada pasien dalam antrian.")
            return
        pasien = self.stack.pop()
        print(f"🔔 Pasien {pasien} dipanggil untuk pemeriksaan.")

    # Melihat pasien berikutnya (Peek)
    def pasien_berikutnya(self):
        if self.isEmpty():
            print("⚠️ Tidak ada pasien dalam antrian.")
            return
        print(f"🔎 Pasien berikutnya: {self.stack[-1]}")

    # Mengecek apakah antrian kosong (isEmpty)
    def isEmpty(self):
        return len(self.stack) == 0

    # Melihat daftar pasien dalam antrian
    def lihat_antrian(self):
        if self.isEmpty():
            print("⚠️ Tidak ada pasien dalam antrian.")
        else:
            print("📋 Daftar antrian pasien:", " -> ".join(self.stack))

# Program utama dengan menu interaktif
def main():
    
    rs = AntrianPasien()
    
    while True:
        print("\n===== SISTEM ANTRIAN PASIEN =====")
        print("1. Tambah Pasien")
        print("2. Panggil Pasien")
        print("3. Lihat Pasien Berikutnya")
        print("4. Lihat Daftar Antrian")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

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
            print("👋 Terima kasih! Program selesai.")
            break
        else:
            print("❌ Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()