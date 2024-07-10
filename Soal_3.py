class AntrianRestoran:
    def __init__(self):
        self.antrian = []

    def enqueue(self, pesanan):#Menambahkan
        self.antrian.append(pesanan)
        print(f"Pesanan '{pesanan}' berhasil ditambahkan ke dalam antrian.")

    def dequeue(self): #menghapus
        if not self.antrian:
            print("Antrian kosong.")
            return None
        pesanan = self.antrian.pop(0)
        print(f"Pesanan '{pesanan}' berhasil dihapus dari antrian.")
        return pesanan
    def display_antrian(self): #menampilkan
        if not self.antrian:
            print("Antrian kosong.")
        else:
            print("Antrian pesanan saat ini:")
            for i, pesanan in enumerate(self.antrian, 1):
                print(f"{i}. {pesanan}")

def main():
    antrian = AntrianRestoran()

    while True:
        print("\nAntrian Resto Gueh:")
        print("1. Tambah Pesanan")
        print("2. Hapus Pesanan")
        print("3. Tampilkan Antrian")
        print("4. Keluar")

        choice = input("Pilih menu: ")
        print("\n")

        if choice == "1":
            pesanan = input("Masukkan pesanan: ")
            antrian.enqueue(pesanan)
        elif choice == "2":
            antrian.dequeue()
        elif choice == "3":
            antrian.display_antrian()
        elif choice == "4":
            print("Terima kasih")
            break

if __name__ == "__main__":
    main()