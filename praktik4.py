import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Parameter distribusi
mean = 170  # rata-rata tinggi badan
std_dev = 10  # standar deviasi
sample_size = 1000  # jumlah sampel

# Bangkitkan data tinggi badan
heights = np.random.normal(mean, std_dev, sample_size)

# Buat DataFrame
df = pd.DataFrame(heights, columns=['Tinggi Badan'])

# Tampilkan 5 baris pertama
print(df.head())

# Plot histogram
plt.figure(figsize=(8, 6))
sns.histplot(df['Tinggi Badan'], kde=True, color='blue')
plt.title('Distribusi Tinggi Badan dalam Populasi')
plt.xlabel('Tinggi Badan (cm)')
plt.ylabel('Frekuensi')
plt.show()

# Hitung probabilitas
prob = np.sum((df['Tinggi Badan'] >= 160) & (df['Tinggi Badan'] <= 180)) / sample_size
print(f"Probabilitas tinggi badan antara 160 cm dan 180 cm: {prob:.2f}")

# Plot CDF
plt.figure(figsize=(8, 6))
sns.ecdfplot(df['Tinggi Badan'], color='green')
plt.title('Probabilitas Kumulatif Tinggi Badan')
plt.xlabel('Tinggi Badan (cm)')
plt.ylabel('Probabilitas Kumulatif')
plt.show()

# Statistik deskriptif
print(df['Tinggi Badan'].describe())