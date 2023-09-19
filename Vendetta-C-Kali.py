#!/usr/bin/env python3

import os

# Tampilkan versi Kali Linux secara detail
print("=== Vendetta-C-Kali ===")
os.system("lsb_release -a")
print("======================")

# Periksa apakah ada pesan "zsh: corrupt history file"
if os.path.exists(os.path.expanduser("~/.zsh_history")):
    with open(os.path.expanduser("~/.zsh_history"), "r") as f:
        if "zsh: corrupt history file" in f.read():
            print("Mengatasi masalah zsh: corrupt history file...")
            os.system("mv ~/.zsh_history ~/.zsh_history_bad && strings ~/.zsh_history_bad > ~/.zsh_history")
            print("File history telah diperbaiki.")

# Pilihan penghapusan file sampah
print("Pilihan penghapusan file sampah:")
print("1. Hapus file sampah sementara")
print("2. Hapus komplit sampah tanpa terkecuali")
choice = input("Masukkan nomor pilihan: ")

if choice == "1":
    # Hapus file sampah sementara
    print("Mencari file sampah sementara...")
    os.system("sudo locate '*~'")
    confirm = input("Apakah Anda yakin ingin menghapus file-file tersebut? (y/n): ")
    if confirm == "y":
        os.system("sudo locate '*~' | xargs sudo rm")
        print("File sampah sementara telah dihapus.")
    else:
        print("Penghapusan file sampah sementara dibatalkan.")
elif choice == "2":
    # Hapus komplit sampah tanpa terkecuali
    print("Mencari semua file sampah...")
    os.system("sudo updatedb")
    os.system("sudo locate '*~'")
    confirm = input("Apakah Anda yakin ingin menghapus semua file sampah? (y/n): ")
    if confirm == "y":
        os.system("sudo locate '*~' | xargs sudo rm")
        print("Semua file sampah telah dihapus.")
    else:
        print("Penghapusan semua file sampah dibatalkan.")
else:
    print("Pilihan tidak valid.")

# Tampilkan total file sampah yang dihapus
print("Total file sampah yang dihapus:")
os.system("sudo locate '*~' | wc -l")

# Keluar dari program
def exit_program(signal, frame):
    print("Keluar dari program.")
    exit(0)

signal.signal(signal.SIGINT, exit_program)
print("Tekan Ctrl+C untuk keluar.")
while True:
    pass