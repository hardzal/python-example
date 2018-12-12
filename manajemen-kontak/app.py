# Program Manajemen Kontak
import function

# List of dictionary
daftar_kontak = []

daftar_kontak.append({
    "nama": "luffy",
    "email": "luffymagami@gmail.com",
    "telepon": "021820939"
})

# Men program
while True:
    print("# MENU")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("5. Edit Kontak")
    print("0. Keluar")

    menu = input("Pilih menu : ")

    if menu == "0":
        break
    elif menu == "1":
        print("\nDaftar Kontak\n")
        function.display_kontak(daftar_kontak)
    elif menu == "2":
        print("\nTambah Kontak\n")
        daftar_kontak.append(function.new_kontak())
        print("\n")
    elif menu == "3":   
        print("\nHapus Kontak\n")
        function.delete_kontak(daftar_kontak)
        print("\n")
    elif menu == "4":
        print("\nCari Kontak\n")
        function.search_kontak(daftar_kontak)
        print("\n")
    elif menu == "5":
        print("\nEdit Kontak\n")
        print("\n")
    else:
        print("Menu tidak ditemukan")
        print("\n")

print("\n")
print("Program telah berakhir.")