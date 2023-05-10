state = "idle"
password_attempts = 0

while True:
    if state == "idle":
        print("Selamat datang!")
        username = input("Masukkan username: ")
        if username:
            state = "entering username"
    elif state == "entering username":
        username = username
        state = "entering password"
    elif state == "entering password":
        password = input("Masukkan password: ")
        if password == "1234": # contoh password yang valid
            state = "logged in"
        elif not password:
            state = "idle"
        else:
            print("Password salah!")
            password_attempts += 1
            if password_attempts >= 3:
                print("Akun dikunci")
                break
    elif state == "logged in":
        username = username
        print("Selamat datang,", username, "!")
        break
