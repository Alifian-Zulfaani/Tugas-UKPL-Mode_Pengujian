def kategori_umur(umur):
    umur = int(umur)
    if umur < 0 or umur > 100:
        return "Umur tidak valid"
    elif umur < 12:
        return "Anak-anak"
    elif umur < 18:
        return "Remaja"
    elif umur < 60:
        return "Dewasa"
    else:
        return "Lansia"


# Menentukan test case berdasarkan boundary value analysis
test_cases = [[-1], [0], [11], [12], [17], [18], [59], [60], [100], [101]]

# Menjalankan pengujian
for test_case in test_cases:
    umur = test_case[0]
    hasil = kategori_umur(umur)
    print(f"Input umur: {umur}, Hasil kategori: {hasil}")
