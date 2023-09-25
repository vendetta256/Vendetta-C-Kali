#!/usr/bin/env python3

import os
import signal

# Tampilkan versi Kali Linux secara detail
print("=== Vendetta-C-Kali V1 ===")
os.system("lsb_release -a")
print("======================")

# Periksa apakah ada pesan "zsh: corrupt history file"
zsh_history_path = os.path.expanduser("~/.zsh_history")
if os.path.exists(zsh_history_path):
    with open(zsh_history_path, "r", encoding="ISO-8859-1") as f:
        try:
            if "zsh: corrupt history file" in f.read():
                print("Mengatasi masalah zsh: corrupt history file...")
                os.system(f"mv {zsh_history_path} {zsh_history_path}_bad && strings {zsh_history_path}_bad > {zsh_history_path}")
                print("File history telah diperbaiki.")
        except UnicodeDecodeError:
            print("Tidak dapat membaca file history. Pastikan file menggunakan encoding yang benar.")

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
