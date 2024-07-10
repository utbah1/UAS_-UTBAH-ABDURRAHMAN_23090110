mahasiswa = []

while True:
    nama = input("Masukkan nama: ")

    nim = input("Masukkan NIM: ")

    data_mahasiswa = {"nama": nama, "nim": nim}
    mahasiswa.append(data_mahasiswa)

    jawaban = input("Ingin menambahkan lagi? (Ya/Tidak): ")

    if jawaban.lower() == "tidak":
        break

print("Data Mahasiswa:")
for i, data in enumerate(mahasiswa, 1):
    print(f"Mahasiswa {i}:")
    print(f"Nama: {data['nama']}")
    print(f"NIM: {data['nim']}")
    print()