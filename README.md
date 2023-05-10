## *boundary_value_analysis.py*
#### Pada file ini, digunakan fungsi kategori_umur() untuk menentukan kategori umur seseorang berdasarkan nilai umur yang diberikan. Fungsi ini akan mengembalikan string yang menyatakan kategori umur yang sesuai.
- Umur tidak valid: umur < 0 atau umur > 100
- Anak-anak: 0 <= umur < 12
- Remaja: 12 <= umur < 18
- Dewasa: 18 <= umur < 60
- Lansia: umur >= 60

#### Kemudian, kita menentukan test case berdasarkan Boundary Value Analysis dengan memperhatikan batas-batas nilai umur yang mungkin, yaitu -1, 0, 11, 12, 17, 18, 59, 60, 100, dan 101. Test case ini kemudian disimpan dalam variabel test_cases.

#### Selanjutnya, kita menjalankan pengujian dengan melakukan iterasi pada setiap test case yang telah ditentukan. Untuk setiap test case, kita memanggil fungsi kategori_umur() dengan argumen nilai umur yang sesuai, kemudian membandingkan nilai yang dikembalikan oleh fungsi tersebut dengan nilai yang diharapkan. Hasil pengujian ditampilkan ke layar dengan menggunakan fungsi print().

![image](https://github.com/Alifian-Zulfaani/Tugas-UKPL-Mode_Pengujian/assets/73049862/1d86323e-e2e0-4580-82c2-4e6fde21fe36)
<br /><br />

## *state_transition_testing.py*
#### Pada file ini, digunakan 3 state, yaitu "idle", "entering username", dan "entering password", serta 1 kondisi khusus saat pengguna salah memasukkan password sebanyak 3 kali.

#### Kode di atas dimulai dengan state "idle" dan akan mencetak pesan "Selamat datang!". Kemudian, program akan meminta pengguna untuk memasukkan username melalui input(). Jika pengguna memasukkan username, program akan menyimpan username tersebut dan berpindah ke state "entering password". Jika pengguna tidak memasukkan username dan membatalkan login dengan menekan Enter, program akan kembali ke state "idle".

#### Di state "entering password", program akan meminta pengguna untuk memasukkan password melalui input(). Jika pengguna memasukkan password yang valid, yaitu "1234" pada contoh kode di atas, program akan berpindah ke state "logged in" dan mencetak pesan "Selamat datang, [username]!". Jika pengguna membatalkan login dengan tidak memasukkan password, program akan kembali ke state "idle". Jika pengguna memasukkan password yang tidak valid, program akan mencetak pesan "Password salah!" dan menambah jumlah password_attempts. Jika jumlah password_attempts mencapai 3, program akan mencetak pesan "Akun dikunci" dan program akan berhenti.

#### Jika program berhasil masuk ke state "logged in", program akan mencetak pesan "Selamat datang, [username]!" dan berhenti.

- Jika password benar

![image](https://github.com/Alifian-Zulfaani/Tugas-UKPL-Mode_Pengujian/assets/73049862/02fa135c-3702-4214-b37d-384886ceda54)

- Jika password salah hingga 3 kali

![image](https://github.com/Alifian-Zulfaani/Tugas-UKPL-Mode_Pengujian/assets/73049862/7f712c12-00cc-488b-bf57-e0d6a8bbfdd2)


