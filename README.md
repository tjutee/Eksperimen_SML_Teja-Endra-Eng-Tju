# Eksperimen_SML_Teja Endra Eng Tju

Repository ini berisi dataset, notebook eksperimen, dan skrip automatisasi preprocessing untuk tugas SMSML.

## Struktur Repository

- `.github/workflows/` - workflow GitHub Actions untuk menjalankan preprocessing otomatis
- `Customer-Segmentation_raw.csv` - dataset mentah
- `requirements.txt` - daftar library Python yang diperlukan
- `preprocessing/` - folder preprocessing
  - `Eksperimen_Teja_Endra_Eng_Tju.ipynb` - notebook eksperimen preprocessing
  - `automate_Teja Endra Eng Tju.py` - skrip automatisasi preprocessing
  - `Customer-Segmentation_preprocessing.csv` - hasil preprocessing

## Cara Menjalankan Preprocessing

Jalankan perintah berikut dari root repository:

```bash
cd preprocessing
python "automate_Teja Endra Eng Tju.py"
```

Skrip akan membaca dataset dari:

```text
Customer-Segmentation_raw.csv
```

Kemudian hasil preprocessing akan disimpan ke:

```text
preprocessing/Customer-Segmentation_preprocessing.csv
```

## Tahapan Preprocessing

Tahapan preprocessing yang dilakukan oleh skrip:

1. Memuat dataset mentah.
2. Melakukan standardisasi pada kolom numerik:
   - `Age`
   - `AnnualIncome`
   - `AverageTransactionValue`
3. Melakukan capping outlier pada:
   - `AnnualIncome`
   - `AverageTransactionValue`
4. Melakukan ordinal encoding pada:
   - `DiscountSensitivity`
   - `ShoppingFrequency`
5. Membuat kolom baru `AgeGroup`.
6. Menyimpan hasil preprocessing ke file CSV.

## Output

File `Customer-Segmentation_preprocessing.csv` berisi data yang sudah siap digunakan untuk proses analisis atau pemodelan berikutnya.
