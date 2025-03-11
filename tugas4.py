import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# Parameter distribusi normal
mean = 5
std_dev = 2

# Simulasi 1000 data pengiriman
np.random.seed(42)
data_simulasi = np.random.normal(loc=mean, scale=std_dev, size=1000)

# Hindari nilai negatif
data_simulasi = np.clip(data_simulasi, 0, None)

# Buat DataFrame
df = pd.DataFrame({'waktu_pengiriman': data_simulasi})

# Lihat 5 data awal
df.head()

plt.figure(figsize=(9, 7))
sns.histplot(df['waktu_pengiriman'], kde=True, color='lightgreen', bins=30)

plt.title("Distribusi Waktu Pengiriman")
plt.xlabel("Hari")
plt.ylabel("Frekuensi")
plt.show()

# Probabilitas teoritis
prob_teoritis_kurang_3 = stats.norm.cdf(3, mean, std_dev)
print(f"Probabilitas (teoritis) pengiriman < 3 hari: {prob_teoritis_kurang_3:.4f}")

# Hitungan berdasarkan data
jumlah_kurang_3 = (df['waktu_pengiriman'] < 3).sum()
persen_kurang_3 = jumlah_kurang_3 / len(df) * 100
print(f"Jumlah pengiriman < 3 hari (simulasi): {jumlah_kurang_3} paket ({persen_kurang_3:.2f}%)")

# Probabilitas teoritis
prob_teoritis_4_7 = stats.norm.cdf(7, mean, std_dev) - stats.norm.cdf(4, mean, std_dev)
print(f"Probabilitas (teoritis) pengiriman antara 4–7 hari: {prob_teoritis_4_7:.4f}")

# Hitungan berdasarkan data
jumlah_4_7 = df[(df['waktu_pengiriman'] >= 4) & (df['waktu_pengiriman'] <= 7)].shape[0]
persen_4_7 = jumlah_4_7 / len(df) * 100
print(f"Jumlah pengiriman antara 4–7 hari (simulasi): {jumlah_4_7} paket ({persen_4_7:.2f}%)")

# Tambah kolom kategori ke DataFrame
def kategori_pengiriman(hari):
    if hari < 3:
        return "< 3 hari"
    elif 4 <= hari <= 7:
        return "4–7 hari"
    else:
        return "> 7 hari"

df['kategori'] = df['waktu_pengiriman'].apply(kategori_pengiriman)

# Visualisasi kategori
plt.figure(figsize=(6, 5))
sns.countplot(data=df, x='kategori', order=["< 3 hari", "4–7 hari", "> 7 hari"], color='pink')
plt.title("Kategori Waktu Pengiriman Paket")
plt.xlabel("Kategori Waktu")
plt.ylabel("Jumlah Paket")
plt.show()