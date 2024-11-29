dosen = {}
mahasiswa = {}
nama_mahasiswa = {}
matkul = []
matkul_pilihan = {}
daftar_tugas = {}

def daftar(user):
    if user == "1":
        username = input("Masukkan Username Dosen : ")
        if username in dosen:
            print("Username Dosen telah digunakan, silakan masukkan username yang lain")
            return False
        password = input("Masukkan Password : ")
        dosen[username] = password  
        print("Anda berhasil mendaftar sebagai Dosen")
    elif user == "2":
        username = input("Masukkan Username Mahasiswa : ")
        if username in mahasiswa:
            print("Username Mahasiswa telah digunakan, silakan masukkan username yang lain")
            return False
        password = input("Masukkan Password : ")
        mahasiswa[username] = password
        nama = input("Masukkan Nama Mahasiswa : ")
        if nama in nama_mahasiswa:
            print("Nama Mahasiswa telah digunakan, silakan masukkan Nama yang lain")
            return False
        NIM = input("Masukkan NIM Mahasiswa : ")
        if NIM in nama_mahasiswa.values():
            print("NIM telah digunakan, silakan masukkan NIM yang sesuai")
            return False
        nama_mahasiswa[username] = NIM
        
        print("Anda berhasil mendaftar sebagai Mahasiswa")
    else:
        print("Pilihan tidak valid! Silakan pilih 1/2/3")
        return False

def login(user):
    if user == "1":
        username = input("Masukkan username Dosen: ")
        password = input("Masukkan password : ")
        if username in dosen and dosen[username] == password:
            print("Login sebagai Dosen berhasil")
            return username  
        else:
            print("Username atau password Dosen salah, silakan coba lagi")
            return None
    elif user == "2":
        username = input("Masukkan username Mahasiswa: ")
        password = input("Masukkan password : ")
        if username in mahasiswa and mahasiswa[username] == password:
            print("Login sebagai Mahasiswa berhasil")
            return username  
        else:
            print("Username atau password Mahasiswa salah, silakan coba lagi")
            return None
    else:
        print("Pilihan tidak ada di daftar, Harap pilih yang sesuai")
        return None

def menu_dosen():
    while True:
        print("\nMenu akses Dosen")
        print("1. Tambah Matkul")  
        print("2. Tampilkan Matkul")
        print("3. Tambah Tugas Matkul")
        print("4. Update Kode Matkul")
        print("5. Hapus Matkul")
        print("6. Keluar/Back")  
        pilihan_dosen = input("Masukkan Pilihan Anda : ")

        if pilihan_dosen == "1":
            nama_matkul = input("Masukkan Nama Matkul : ")
            kode_matkul = input("Buat Kode Matkul : ")
            matkul.append({"Nama Matkul": nama_matkul, "Kode Matkul": kode_matkul, "Tugas": []})  
            print(f"Matkul {nama_matkul} berhasil ditambahkan")

        elif pilihan_dosen == "2":
            if matkul:
                print("\nDaftar Matkul:")
                for i, m in enumerate(matkul, start=1):
                    tugas_list = ', '.join(m['Tugas']) if m['Tugas'] else "Tidak ada tugas"
                    print(f"{i}. {m['Nama Matkul']} - {m['Kode Matkul']} | Tugas: {tugas_list}")
            else:
                print("Belum ada matkul yang ditambahkan")

        elif pilihan_dosen == "3":
            if matkul:
                print("\nDaftar Matkul:")
                for i, m in enumerate(matkul, start=1):
                    print(f"{i}. {m['Nama Matkul']} - {m['Kode Matkul']}")
                pilih_matkul = int(input("Pilih nomor Matkul untuk menambahkan tugas: ")) - 1
                if 0 <= pilih_matkul < len(matkul):
                    tugas_baru = input("Masukkan nama tugas: ")
                    matkul[pilih_matkul]['Tugas'].append(tugas_baru) 
                    print(f"Tugas '{tugas_baru}' berhasil ditambahkan pada matkul {matkul[pilih_matkul]['Nama Matkul']}.")
                else:
                    print("Nomor mata kuliah tidak terdaftar")
            else:
                print("Belum ada matkul yang ditambahkan")

        elif pilihan_dosen == "4":
            if matkul:
                print("\nDaftar Matkul untuk Diperbarui:")
                for i, m in enumerate(matkul, start=1):
                    print(f"{i}. {m['Nama Matkul']} - {m['Kode Matkul']}")
                update_i = int(input("Masukkan nomor mata kuliah yang ingin diupdate: ")) - 1
                if 0 <= update_i < len(matkul):
                    kode_baru = input("Masukkan kode baru: ")
                    matkul[update_i]['Kode Matkul'] = kode_baru
                    print("Kode mata kuliah berhasil diperbarui")
                else:
                    print("Nomor mata kuliah tidak terdaftar")
            else:
                print("Belum ada mata kuliah yang ditambahkan")

        elif pilihan_dosen == "5":
            if matkul:
                print("\nDaftar Matkul untuk Dihapus:")
                for i, m in enumerate(matkul, start=1):
                    print(f"{i}. {m['Nama Matkul']} - {m['Kode Matkul']}")
                hapus_i = int(input("Masukkan nomor mata kuliah yang ingin dihapus: ")) - 1
                if 0 <= hapus_i < len(matkul):
                    matkul.pop(hapus_i)
                    print(f"Mata kuliah nomor {hapus_i + 1} berhasil dihapus")
                else:
                    print("Nomor mata kuliah tidak terdaftar")
            else:
                print("Belum ada mata kuliah yang ditambahkan")

        elif pilihan_dosen == "6":
            print("Keluar dari menu")
            break
            
        else:
            print("Pilihan tidak ada di daftar, Silakan pilih antara 1-6")


def menu_mahasiswa(username):  
    global matkul_pilihan  
    while True:
        print("\nMenu akses Mahasiswa")
        print("1. Ambil Matkul")
        print("2. Tampilkan Tugas dan Matkul yang diambil") 
        print("3. Hapus Matkul")
        print("4. Update Nama Pengguna")
        print("5. Keluar/Back")
        pilihan_mahasiswa = input("Masukkan Pilihan Anda : ")

        if pilihan_mahasiswa == "1":
            if matkul:
                print("\nBerikut adalah daftar Mata Kuliah yang tersedia:")
                for i, matkul_item in enumerate(matkul, start=1):
                    print(f"{i}. {matkul_item['Nama Matkul']} (Kode: {matkul_item['Kode Matkul']})")

            pilihan = []
            while True:
                pilih_matkul = input(f"Masukkan kode matkul yang ingin Anda ambil (ketik '0' untuk mengakhiri pemilihan): ")
                if pilih_matkul == "0":
                    break  

                if any(matkul_item['Kode Matkul'] == pilih_matkul for matkul_item in matkul):
                    if pilih_matkul not in pilihan:
                        pilihan.append(pilih_matkul)
                        print(f"Anda berhasil memilih mata kuliah dengan kode {pilih_matkul}")
                    else:
                        print("Anda sudah memilih mata kuliah ini")
                else:
                    print("Kode mata kuliah tidak terdaftar, Silakan coba lagi")

            if pilihan:
                print("\nDaftar mata kuliah yang Anda pilih:")
                for pilih in pilihan:
                    matkul_item = next((item for item in matkul if item['Kode Matkul'] == pilih), None)
                    if matkul_item:
                        print(f"- {matkul_item['Nama Matkul']} (Kode: {pilih})")
        
                matkul_pilihan[username] = [matkul_item for matkul_item in matkul if matkul_item['Kode Matkul'] in pilihan]
                print(f"Anda telah memilih {len(matkul_pilihan[username])} mata kuliah")
            else:
                print("Anda belum memilih mata kuliah")

        elif pilihan_mahasiswa == "2":
            if username in matkul_pilihan:
                print("\nMata Kuliah yang Anda pilih:")
                for i, matkul_item in enumerate(matkul_pilihan[username], start=1):
                    print(f"{i}. {matkul_item['Nama Matkul']} - {matkul_item['Kode Matkul']}")
                
                lihat_tugas = input("\nLihat tugas yang diberikan oleh dosen (ya/tidak): ").lower()
                if lihat_tugas == "ya":
                    pilih_matkul_tugas = int(input("Masukkan nomor mata kuliah untuk melihat tugas: ")) - 1
                    if 0 <= pilih_matkul_tugas < len(matkul_pilihan[username]):
                        matkul_pilihan_item = matkul_pilihan[username][pilih_matkul_tugas]
                        if matkul_pilihan_item['Tugas']:  
                            print("\nTugas yang diberikan untuk mata kuliah ini:")
                            for tugas in matkul_pilihan_item['Tugas']:
                                print(f"- {tugas}")
                        else:
                            print("Belum ada tugas yang diberikan untuk mata kuliah ini")
                    else:
                        print("Nomor mata kuliah tidak terdaftar")
            else:
                print("Anda belum memilih mata kuliah")
        
        elif pilihan_mahasiswa == "3":
            if username in matkul_pilihan:
                print("\nMata Kuliah yang ingin dihapus:")
                for i, matkul_item in enumerate(matkul_pilihan[username], start=1):
                    print(f"{i}. {matkul_item['Nama Matkul']} - {matkul_item['Kode Matkul']}")
                hapus_i = int(input("Masukkan nomor mata kuliah yang ingin dihapus: ")) - 1
                if 0 <= hapus_i < len(matkul_pilihan[username]):
                    matkul_pilihan[username].pop(hapus_i)
                    print("Mata kuliah berhasil dihapus")
                else:
                    print("Nomor mata kuliah tidak terdaftar")
            else:
                print("Anda belum memilih mata kuliah")
        
        elif pilihan_mahasiswa == "4":
            username_lama = input("Masukkan username lama Anda: ")
    
            if username_lama in mahasiswa:
                nim_mahasiswa = nama_mahasiswa[username_lama]
        
                print("\nAnda dapat mengupdate:")
                print("1. Username")
                print("2. Nama")
                print("3. Password")
                update_pilihan = input("Masukkan pilihan yang ingin diupdate (1/2/3): ")

                if update_pilihan == "1":
                    username_baru = input("Masukkan username baru Anda: ")
                    if username_baru in mahasiswa:
                        print("Username baru sudah terdaftar, silakan pilih username yang lain.")
                    else:
                        mahasiswa[username_baru] = mahasiswa.pop(username_lama)  
                        nama_mahasiswa[username_baru] = nim_mahasiswa
                        print(f"Username Anda berhasil diperbarui menjadi {username_baru}")

                elif update_pilihan == "2":
                    nama_baru = input("Masukkan nama baru Anda: ")
                    print(f"Nama Anda berhasil diperbarui menjadi {nama_baru}")
                    nama_mahasiswa[username_lama] = nim_mahasiswa  

                elif update_pilihan == "3":
                    password_baru = input("Masukkan password baru Anda: ")
                    mahasiswa[username_lama] = password_baru 
                    print("Password Anda berhasil diperbarui")
                else:
                    print("Pilihan tidak terdaftar, kembali ke menu utama")
            else:
                print("Username lama tidak ditemukan")
                
        elif pilihan_mahasiswa == "5":
            print("Keluar dari menu")
            break

        else:
            print("Pilihan tidak ada di daftar, Silakan pilih antara 1-5")

           



def main():
    print("---------------------------------------------------------------------------------")
    print("SELAMAT DATANG DI PROGRAM SISTEM GOOGLE CLASSROOM PENGELOLA TUGAS DAN MATA KULIAH")
    print("---------------------------------------------------------------------------------")
    while True:
        print("\n1. Daftar")
        print("2. Login")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            print("\nPilih pengguna/user untuk mendaftar :")
            print("1. Dosen")            
            print("2. Mahasiswa")
            user = input("Masukkan pilihan Anda : ")
            daftar(user)  
            
        elif pilihan == "2":
            print("Pilih Login Sebagai :")
            print("1. Dosen")
            print("2. Mahasiswa")
            user = input("Masukkan pilihan Anda : ")
            username = login(user)  
            if username:  
                if user == "1":
                    menu_dosen()  
                elif user == "2":
                    menu_mahasiswa(username)  
            else:
                print("Login gagal, silakan coba lagi")
        elif pilihan == "3":
            print("----Keluar dari program----")
            break
        else:
            print("Pilihan tidak terdaftar, Silakan coba lagi")

main()