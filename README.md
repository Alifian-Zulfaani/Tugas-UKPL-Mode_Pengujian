# Tugas-UKPL-Mode_Pengujian

<div style="text-align: justify">
    File mode_pengujian.py adalah file inti yang dapat diganti nilai argumen/variabelnya dan dirun, karena file boundary_value_analysis.py dan state_transition_testing.py adalah file racikan mode pengujiannya.
</div>


+ ### ***boundary_value_analysis.py***
<div style="text-align: justify">
    Dideklarasikan fungsi "boundary_value_analysis" yang menerima enam parameter sebagai masukan yaitu "param1_min", "param1_max", "param2_min", "param2_max", "param3_min", dan "param3_max". Fungsi ini digunakan untuk menghasilkan test case dengan teknik pengujian Boundary Value Analysis.
</div>

#### 1. Pertama-tama, variabel "test_cases" dideklarasikan sebagai sebuah list kosong. Kemudian, kode memasukkan delapan test case ke dalam variabel "test_cases" menggunakan teknik Boundary Value Analysis. Test case yang dihasilkan meliputi kombinasi minimum dan maksimum nilai untuk setiap parameter.

#### 2. Setiap test case dihasilkan dengan membuat sebuah list yang berisi tiga nilai yaitu nilai untuk "param1", "param2", dan "param3". Setelah delapan test case selesai dibuat, variabel "test_cases" berisi delapan list, masing-masing list berisi tiga nilai.

#### 3. Terakhir, fungsi mengembalikan variabel "test_cases" yang berisi delapan test case. Test case ini dapat digunakan untuk menguji fungsi atau program yang menggunakan tiga parameter input yang diuji dengan teknik Boundary Value Analysis.


+ ### ***state_transition_testing.py***
<div style="text-align: justify">
    Dideklarasikan sebuah class dengan nama StateTransitionTest, yang memiliki beberapa metode atau fungsi:
</div>

- Pada method __init__(), terdapat beberapa parameter yaitu states, transitions, dan initial_state. Parameter states merepresentasikan kumpulan state/state yang ada pada sistem yang akan diuji, transitions merepresentasikan transisi antar state, dan initial_state merepresentasikan state awal ketika testing dilakukan.

- Pada method reset(), fungsi ini digunakan untuk mengembalikan nilai dari current_state ke initial_state.

- Pada method get_current_state(), fungsi ini digunakan untuk mengembalikan nilai dari current_state.

- Pada method execute_transition(), fungsi ini digunakan untuk mengecek apakah transisi yang akan dilakukan benar atau tidak dengan memeriksa apakah transisi tersebut ada di dalam transitions state yang sedang diproses. Jika transisi ada, maka current_state akan diubah sesuai dengan transisi yang dipilih dan fungsi akan mengembalikan nilai True. Jika transisi tidak ada, maka current_state tidak berubah dan fungsi akan mengembalikan nilai False.

<div style="text-align: justify">
    Fungsi ini akan berguna ketika melakukan pengujian dengan metode state transition testing, dimana StateTransitionTest akan digunakan untuk membangkitkan test case dari semua kemungkinan transisi pada sistem yang akan diuji.
</div>

<div style="text-align: justify">
    Dideklarasikan juga fungsi "state_transition_testing" yang menerima tiga parameter sebagai masukan yaitu "states", "transitions", dan "initial_state". Fungsi ini digunakan untuk menghasilkan test case dengan teknik pengujian State Transition Testing.
</div>


#### 1. Pertama-tama, variabel "test_cases" dideklarasikan sebagai sebuah list kosong. Kemudian, kode membuat sebuah objek "StateTransitionTest" dengan menggunakan tiga parameter input: "states", "transitions", dan "initial_state". Objek "StateTransitionTest" ini digunakan untuk melakukan pengujian pada setiap transisi.

#### 2. Setelah objek "StateTransitionTest" dibuat, kode akan memulai pengujian dengan melakukan loop pada setiap state dan transition. Loop akan dimulai dengan mengatur objek "current_state" menjadi state yang sedang diuji. Kemudian, kode akan mengambil setiap transisi dari state tersebut dan melakukan pengujian dengan mengubah "current_state" sesuai dengan hasil transisi.

#### 3. Setelah setiap transisi pada setiap state diuji, kode akan menambahkan hasil pengujian ke dalam variabel "test_cases". Hasil pengujian dihasilkan sebagai tuple yang berisi tiga nilai yaitu state awal, transisi yang diambil, dan state akhir.

#### 4. Setelah semua transisi pada setiap state selesai diuji, objek "StateTransitionTest" direset ke state awal menggunakan metode "reset()". Akhirnya, variabel "test_cases" yang berisi test case dihasilkan di dalam loop, kemudian dikembalikan sebagai hasil fungsi.

#### 5. Dengan menggunakan test case yang dihasilkan, dapat dilakukan pengujian pada fungsi atau program yang menggunakan state dan transisi dengan teknik State Transition Testing.


+ ### ***mode_pengujian.py***
<div style="text-align: justify">
    Ini adalah file inti yang akan dirun untuk melakukan 2 mode pengujian, boundary_value_analysis dan state_transition_testing
</div>

#### 1. Pertama, program mengimport fungsi boundary_value_analysis dan state_transition_testing dari file boundary_value_analysis.py dan state_transition_testing.py secara berurutan.
#### 2. Kemudian, fungsi boundary_value_analysis dipanggil dengan argumen 1, 10, 20, 30, 100, 200 dan nilai kembaliannya disimpan dalam variabel boundary_test_cases.
#### 3. Selanjutnya, variabel boundary_test_cases dicetak ke layar.
#### 4. Setelah itu, program mendefinisikan variabel states, transitions, dan initial_state yang merepresentasikan keadaan awal dan transisi antara keadaan-keadaan yang ada pada suatu sistem.
#### 5. Kemudian, fungsi state_transition_testing dipanggil dengan argumen states, transitions, dan initial_state dan nilai kembaliannya disimpan dalam variabel state_test_cases.
#### 6. Terakhir, variabel state_test_cases dicetak ke layar.
