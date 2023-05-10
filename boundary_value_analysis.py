# Fungsi "boundary_value_analysis" yang menerima enam parameter sebagai masukan
def boundary_value_analysis(param1_min, param1_max, param2_min, param2_max, param3_min, param3_max):
    # Variabel "test_cases" dideklarasikan sebagai sebuah list kosong
    test_cases = []
    
    # Ada kemungkinan delapan test case (kemungkinan kasus yang terjadi) yang merupakan kombinasi minimum dan maksimum nilai untuk setiap parameter
    
    # Test case 1: nilai minimum untuk semua parameter
    test_cases.append([param1_min, param2_min, param3_min])
    
    # Test case 2: nilai minimum untuk parameter 1, nilai maksimum untuk parameter 2 dan 3
    test_cases.append([param1_min, param2_max, param3_max])
    
    # Test case 3: nilai maksimum untuk parameter 1, nilai minimum untuk parameter 2 dan 3
    test_cases.append([param1_max, param2_min, param3_min])
    
    # Test case 4: nilai maksimum untuk parameter 1, nilai maksimum untuk parameter 2, nilai minimum untuk parameter 3
    test_cases.append([param1_max, param2_max, param3_min])
    
    # Test case 5: nilai maksimum untuk parameter 1, nilai minimum untuk parameter 2, nilai maksimum untuk parameter 3
    test_cases.append([param1_max, param2_min, param3_max])
    
    # Test case 6: nilai minimum untuk parameter 1, nilai maksimum untuk parameter 2, nilai minimum untuk parameter 3
    test_cases.append([param1_min, param2_max, param3_min])
    
    # Test case 7: nilai minimum untuk parameter 1, nilai minimum untuk parameter 2, nilai maksimum untuk parameter 3
    test_cases.append([param1_min, param2_min, param3_max])
    
    # Test case 8: nilai maksimum untuk semua parameter
    test_cases.append([param1_max, param2_max, param3_max])
    
    # fungsi mengembalikan variabel "test_cases" yang berisi delapan test case. 
    return test_cases
    # Test case ini dapat digunakan untuk menguji fungsi atau program yang menggunakan tiga parameter input yang diuji dengan teknik Boundary Value Analysis.