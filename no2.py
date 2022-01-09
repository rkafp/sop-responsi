#By @rkafp
import os

programs = {"Putty": 4, "Sublime": 7, "Paint": 3, "Chrome": 9, "Calculator": 3}
programs_temp = {}

def showMenu():
    menu = -1
    while menu != 0:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

        print("-"*50,"M E N U","-"*50)
        print("[1] Tambah program baru")
        print("[2] Lihat program yang sudah diurutkan")
        print("[3] Lihat program yang belum diurutkan")
        print("[4] Hapus Program")
        print("[0] Kelar")
        print("-"*109)

        menu = int(input("Pilih menu: "))
        if (menu == 1):
            add()
        elif (menu == 2):
            sort()
        elif (menu == 3):
            unsort()
        elif (menu == 4):
            delete()
        elif (menu == 0):
            print("\nTerima kasih sudah berkunjung!")
        else:
            print("\nMenu pilihan tidak ada!\n")
            input()

    
def add():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print("-"*51,"A D D","-"*51)
    more = "Y"
    while more == "Y":
        program_name = input("Masukkan Nama Program: ")
        process_time = int(input("Masukkan Lama Waktu Pemprosesan: "))

        global programs_temp
        if (programs_temp == {}):
            programs_temp = {**programs}

        programs[program_name] = process_time
        programs_temp[program_name] = process_time

        more = input("\nTambah data lagi? (Y/T): ").upper()
        print()

        while more not in ("Y", "T"):
            print("\nSilahkan untuk hanya memasukkan 'Y' atau 'T' saja!\n")
            more = input("Tambah data lagi? (Y/T): ").upper()

        if (more == "T"):
            break

def sort():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    quantum_time = int(input("Masukkan Time Quantum: "))

    global programs_temp
    programs_temp = {**programs}

    for k, v in programs_temp.items():
        if quantum_time < v:
            programs.pop(k)
            programs[k] = v
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print("-"*52,"S O R T","-"*52)

    num = 0
    print("-"*109)
    print("Nomor".ljust(20), "Nama Program".ljust(30), "Lama Waktu Pemrosesan".ljust(40), "Time Quantum")
    print("-"*109)

    for k, v in programs.items():
        num += 1
        print(str(num).ljust(20), "{}".format(k).ljust(30), "{}".format(v).ljust(40), quantum_time)
    input("\nTekan ENTER untuk melanjutkan...")

def unsort():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print("-"*48,"U N S O R T","-"*48)

    global programs_temp
    if (programs_temp == {}):
        programs_temp = {**programs}

    num = 0
    print("-"*109)
    print("Nomor".ljust(20), "Nama Program".ljust(50), "Lama Waktu Pemrosesan")
    print("-"*109)
    for k, v in programs_temp.items():
        num += 1
        print(str(num).ljust(20), "{}".format(k).ljust(50), "{}".format(v))
    input("\nTekan ENTER untuk melanjutkan...")

def delete():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print("-"*48,"D E L E T E","-"*48) 

    global programs_temp
    if (programs_temp == {}):
        programs_temp = {**programs}

    program_name = input("Masukkan Nama Program: ")

    x = 0
    programs_del_temp = {**programs}
    for k in programs_del_temp:
        if (program_name == k):
            x = 1
            del programs[k]
            del programs_temp[k]
            print("\nPROGRAM BERHASIL DIHAPUS")
            input("\nTekan ENTER untuk melanjutkan...")
            
    if (x == 0):
        print("\nPROGRAM TIDAK DITEMUKAN")
        input("\nTekan ENTER untuk melanjutkan...")


if __name__ == "__main__":
    showMenu()
#By @rkafp