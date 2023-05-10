# Tugas-UKPL-Mode_Pengujian
## File mode_pengujian.py adalah file inti yang dapat diganti nilai argumen/variabelnya dan dirun, karena file boundary_value_analysis.py dan state_transition_testing.py adalah file racikan mode pengujiannya.

### ***boundary_value_analysis.py***
### *dideklarasikan fungsi "boundary_value_analysis" yang menerima enam parameter sebagai masukan yaitu "param1_min", "param1_max", "param2_min", "param2_max", "param3_min", dan "param3_max". Fungsi ini digunakan untuk menghasilkan test case dengan teknik pengujian Boundary Value Analysis.*

### *Pertama-tama, variabel "test_cases" dideklarasikan sebagai sebuah list kosong. Kemudian, kode memasukkan delapan test case ke dalam variabel "test_cases" menggunakan teknik Boundary Value Analysis. Test case yang dihasilkan meliputi kombinasi minimum dan maksimum nilai untuk setiap parameter.*

### *Setiap test case dihasilkan dengan membuat sebuah list yang berisi tiga nilai yaitu nilai untuk "param1", "param2", dan "param3". Setelah delapan test case selesai dibuat, variabel "test_cases" berisi delapan list, masing-masing list berisi tiga nilai.*

### *Terakhir, fungsi mengembalikan variabel "test_cases" yang berisi delapan test case. Test case ini dapat digunakan untuk menguji fungsi atau program yang menggunakan tiga parameter input yang diuji dengan teknik Boundary Value Analysis.*
