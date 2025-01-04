import random

print('Selamat datang di permainan tebak angka!')
print('Saya telah memilih angka antara 1 dan 100.')
print('Cobalah tebak angkanya, atau ketik "exit" untuk keluar.')
print('-' * 50)

# Membuat angka acak di luar loop
random_number = random.randint(1, 5)

while True:
    user_input = input('Masukkan tebakan Anda: ')
    
    # Opsi keluar
    if user_input.lower() == "exit":
        print('Terima kasih sudah bermain!')
        break

    # Validasi apakah input adalah angka
    if user_input.isdigit():
        user_input = int(user_input)  # Ubah input menjadi integer
        
        if user_input == random_number:
            print('Selamat! Anda berhasil menebak angkanya.')
            break  # Permainan selesai
        elif user_input > random_number:
            print('Terlalu tinggi!')
        else:
            print('Terlalu rendah!')
    else:
        print('Masukkan angka yang valid atau ketik "exit" untuk keluar.')
