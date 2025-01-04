# Menampilkan pesan pembuka permainan
print('Game Kalkulator Faktorial')
print('Selamat datang di Kalkulator Faktorial!')

while True:  # Loop utama program agar berjalan terus hingga pengguna keluar
    print("Masukkan bilangan bulat positif (atau ketik 'exit' untuk keluar): ")

    # Meminta input dari pengguna
    user_number = input('Masukkan angka 1 - 10: ')
    
    # Opsi keluar permainan
    if user_number.lower() == "exit":  # Jika pengguna mengetik "exit" (case insensitive)
        print('Terima kasih telah memainkan game ini!')
        break  # Keluar dari loop utama

    # Validasi apakah input adalah angka
    if user_number.isdigit():  # Cek apakah input hanya terdiri dari digit (bilangan bulat positif)
        user_input = int(user_number)  # Mengonversi input string menjadi integer
        
        # Validasi apakah angka negatif (meskipun `isdigit` sudah menghindari negatif, tetap dicek untuk kejelasan)
        if user_input < 0:
            print('Input tidak valid. Silakan masukkan bilangan bulat positif.')
            continue  # Kembali ke awal loop tanpa melanjutkan kode di bawah

        # Inisialisasi variabel untuk hasil faktorial
        result = 1  # Faktorial dimulai dari 1
        steps = []  # Daftar untuk menyimpan langkah-langkah perhitungan

        # Loop untuk menghitung faktorial
        for i in range(1, user_input + 1):  # Iterasi dari 1 hingga angka yang dimasukkan
            result *= i  # Mengalikan hasil sebelumnya dengan angka saat ini
            steps.append(str(i))  # Menyimpan angka ke daftar langkah

        # Gabungkan langkah-langkah menjadi string untuk ditampilkan
        steps_display = " x ".join(steps)  # Gabungkan angka dengan simbol "x" di antaranya
        print(f"Faktorial dari {user_input}! = {steps_display} = {result}.")  # Tampilkan hasil

    else:
        # Jika input bukan angka atau "exit"
        print("Input tidak valid. Masukkan bilangan bulat positif atau ketik 'exit' untuk keluar.")
