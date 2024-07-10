import pandas as pd

data = [
    ["Mahasiswa 1", 90, 80],
    ["Mahasiswa 2", 50, 60],
    ["Mahasiswa 3", 65, 70]
]

df = pd.DataFrame(data, columns=["Nama", "Algoritma dan Struktur Data 2", "Matematika Numerik"])

rata_rata_kuliah = df.iloc[:, 1:].mean()

print("Rata-rata nilai untuk setiap mata kuliah:")
print(rata_rata_kuliah)

rata_rata_mahasiswa = df.iloc[:, 1:].mean(axis=1)

print("\nRata-rata nilai untuk setiap mahasiswa:")
for i, nilai in enumerate(rata_rata_mahasiswa, start=1):
    print(f"Mahasiswa {i}: {nilai:.2f}")