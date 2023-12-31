def main_menu():
    print("Menu Layanan Telkomsel:")
    print("1. Transfer Pulsa")
    print("2. Request Pulsa")
    print("3. Auto Transfer Pulsa")
    print("4. Delete Auto Transfer Pulsa")
    print("5. List Auto Transfer Pulsa")
    print("6. Cek Kupon Undian Transfer Pulsa")

data_pulsa = {}
jumlah_kupon = 0

def transfer_pulsa(jumlah_kupon):
    print("Anda memilih Transfer Pulsa")
    nomor_tujuan = input("Masukkan nomor telepon tujuan Transfer Pulsa : ")
    try:
        jumlah_pulsa = float(input("Masukkan jumlah pulsa yang akan ditransfer (min. Rp. 5000) : "))
        if jumlah_pulsa < 5000:
            print("Jumlah pulsa harus lebih dari Rp. 5000.")
        elif jumlah_pulsa > 1000000:
            print("Jumlah pulsa tidak boleh lebih dari Rp. 1.000.000")
        else:
            while True:
                pilihan = input(f"Anda akan mengirim pulsa ke {nomor_tujuan}. Masukkan angka: 1 (Lanjut), 9 (Kembali ke Menu), 0 (Keluar): ")
                if pilihan == '1':
                    print(f"Anda telah berhasil mengirim pulsa kepada {nomor_tujuan} sebesar Rp. {jumlah_pulsa} .")
                    jumlah_kupon += 1
                    return jumlah_kupon
                elif pilihan == '9':
                    break
                elif pilihan == '0':
                    exit_program()
                else:
                    print("Pilihan tidak valid.")   
            return jumlah_kupon
    except ValueError:
        print("Masukkan jumlah pulsa yang valid.")
    return jumlah_kupon

def request_pulsa():
    print("Anda memilih Request Pulsa")
    nomor_tujuan = input("Masukkan nomor telepon tujuan Minta Pulsa: ")
    try:
        jumlah_pulsa = float(input("Masukkan jumlah pulsa yang akan diminta (min. Rp. 5000) : "))
        if jumlah_pulsa < 5000:
            print("Jumlah pulsa harus lebih dari Rp. 5000.")
        elif jumlah_pulsa > 1000000:
            print("Jumlah pulsa tidak boleh lebih dari Rp. 1.000.000")
        else:
            while True:
                pilihan = input(f"Anda akan meminta pulsa ke {nomor_tujuan}. Masukkan angka: 1 (Lanjut), 9 (Kembali ke Menu), 0 (Keluar): ")
                if pilihan == '1':
                    print(f"Anda telah berhasil meminta pulsa kepada {nomor_tujuan} sebesar Rp. {jumlah_pulsa} .")
                    return 
                elif pilihan == '9':
                    break
                elif pilihan == '0':
                    exit_program()
                else:
                    print("Pilihan tidak valid.")
    except ValueError:
        print("Masukkan jumlah pulsa yang valid.")

def auto_transfer_pulsa():
    print("Anda memilih Auto Transfer Pulsa")
    nomor_tujuan = input("Masukkan nomor telepon tujuan: ")
    try:
        jumlah_pulsa = float(input("Masukkan jumlah pulsa yang akan dikirim (min. Rp. 5000) : "))
        if jumlah_pulsa < 5000:
            print("Jumlah pulsa harus lebih dari Rp. 5000.")
        elif jumlah_pulsa > 1000000:
            print("Jumlah pulsa tidak boleh lebih dari Rp. 1.000.000")
        else:
            while True:
                pilihan = input(f"Anda akan menyimpan nomor {nomor_tujuan} untuk Auto Transfer Pulsa. Masukkan angka: 1 (Lanjut), 9 (Kembali ke Menu), 0 (Keluar): ")
                if pilihan == '1':
                    data_pulsa[nomor_tujuan] = jumlah_pulsa
                    print(f"Data telah tersimpan: {nomor_tujuan} - Rp. {jumlah_pulsa}.")
                    return
                elif pilihan == '9':
                    break
                elif pilihan == '0':
                    exit_program()
                else:
                    print("Pilihan tidak valid.")
    except ValueError:
        print("Masukkan jumlah pulsa yang valid.")

def delete_auto_transfer_pulsa():
    print("Anda memilih Delete Auto Transfer Pulsa")
    nomor_tujuan = input("Masukkan nomor telepon yang ingin dihapus: ")
    if nomor_tujuan in data_pulsa:
        while True:
                pilihan = input(f"Anda akan menghapus nomor {nomor_tujuan} dari Auto Transfer Pulsa. Masukkan angka: 1 (Lanjut), 9 (Kembali ke Menu), 0 (Keluar): ")
                if pilihan == '1':
                    del data_pulsa[nomor_tujuan]
                    print(f"Nomor telepon {nomor_tujuan} telah dihapus dari daftar Auto Transfer Pulsa.")
                    return
                elif pilihan == '9':
                    break
                elif pilihan == '0':
                    exit_program()
                else:
                    print("Pilihan tidak valid.")
    else:
        print(f"Nomor telepon {nomor_tujuan} tidak ditemukan dalam daftar Auto Transfer Pulsa.")

def list_auto_transfer_pulsa():
    print("Anda memilih List Auto Transfer Pulsa")
    print("Daftar Nomor Telepon Auto Transfer Pulsa:")
    for idx, (nomor, pulsa) in enumerate(data_pulsa.items(), start=1):
        print(f"{idx}. {nomor} - {pulsa} pulsa")
    pilihan = input("Masukkan angka : 9 (Kembali ke Menu), 0 (Keluar) :")
    if pilihan == '9':
        return
    elif pilihan == '0':
        exit_program()
    else:
        print("Pilihan tidak valid.")

def cek_kupon_undian_transfer_pulsa(jumlah_kupon):
    print("Anda memilih Cek Kupon Undian Transfer Pulsa")
    print(f"Anda memiliki {jumlah_kupon} Kupon Undian Transfer Pulsa")
    return jumlah_kupon


def exit_program():
    print("Terima kasih telah menggunakan layanan Telkomsel.")
    exit(0)

def main():
    jumlah_kupon = 0
    while True:
        main_menu()
        try:
            pilihan = int(input("Pilih angka (1-6) atau tekan 0 untuk keluar: "))
            if pilihan == 1:
                transfer_pulsa(jumlah_kupon)
            elif pilihan == 2:
                request_pulsa()
            elif pilihan == 3:
                auto_transfer_pulsa()
            elif pilihan == 4:
                delete_auto_transfer_pulsa()
            elif pilihan == 5:
                list_auto_transfer_pulsa()
            elif pilihan == 6:
                cek_kupon_undian_transfer_pulsa(jumlah_kupon)
            elif pilihan == 0:
                exit_program()
            else:
                print("Pilihan tidak valid. Silakan pilih angka (1-6) atau tekan 0 untuk keluar.")
        except ValueError:
            print("Masukkan angka yang valid.")

if __name__ == "__main__":
    main()
