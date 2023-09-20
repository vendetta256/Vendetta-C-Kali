<div>
  <img src="https://camo.githubusercontent.com/3c0b054a8de90e002d439d60011f23cfbbcb2f385723bbc76cf371a9628e236c/68747470733a2f2f7777772e706e676d6172742e636f6d2f66696c65732f342f562d466f722d56656e64657474612d5472616e73706172656e742d4261636b67726f756e642e706e67" alt="Vendetta-C-Kali logo" width="200" align="left">
  <h1>Vendetta-C-Kali</h1>
</div>

Vendetta-C-Kali adalah tools untuk membersihkan file sampah sementara dan seluruh file sampah di semua direktori pada sistem operasi Kali Linux. Tools ini juga dapat memperbaiki file history jika terdapat pesan "zsh: corrupt history file".

## =W=H=I=T=E==H=A=C=K=E=R=
## =W=H=I=T=E==H=A=C=K=E=R=

## Update Fitur Terbaru :
   - Penyesuaian fitur sekarang tidak lagi membersihkan secara offline tapi sudah menggunakan pembersihan secara online. Yaitu dengan memanggil source kode induk dari github untuk melakukan tugasnya di Kali Linux.

`Catatan:`
`Pastikan memliki koneksi internet dalam melakukan pembersihan. menjalankan aplikasi tanpa koneksi internet, tidak akan berproses sebagaimana mestinya`

## Cara Penggunaan

1. Download script dari [repository GitHub ini](https://github.com/vendetta256/Vendetta-C-Kali.git).
2. Buka terminal dan masuk ke direktori tempat script disimpan.
3. Jalankan script dengan perintah `sudo python3 vendetta-c-kali.py`.
4. Pilih opsi penghapusan file sampah yang diinginkan.
5. Tunggu hingga proses penghapusan selesai.
6. Script akan menampilkan total file sampah yang dihapus.
7. Tekan Ctrl+C untuk keluar dari program.

## Dependensi

- Python 3

Anda dapat menginstal Python 3 dengan perintah `sudo apt-get install python3`.

## Catatan

Pastikan untuk menjalankan script ini dengan hak akses superuser (sudo) agar dapat menghapus file sampah di seluruh lokasi pada sistem operasi Anda.

Script ini telah diuji coba pada versi Kali Linux dengan informasi sebagai berikut:

- Distributor ID: Kali
- Description: Kali GNU/Linux Rolling
- Release: 2023.3
- Codename: kali-rolling

Pastikan versi Kali Linux Anda sesuai dengan informasi di atas untuk memastikan script ini dapat berjalan dengan baik.

## Lisensi

Script ini di distribusikan oleh Komunitas White Hacker seluruh indonesia dan dilisensikan di bawah lisensi MIT. Silakan merujuk ke file LICENSE untuk informasi lebih lanjut.

---
</br>

## Perbaikan Bug dan Penyesuaian Fitur
# Deskripsi Script

Berikut adalah daftar perbaikan, penyesuaian, dan penambahan fitur pada skrip yang telah diperbarui:

1. **Perbaikan Sintaks dan Format**:
   - Memastikan sintaks dan format teks sesuai dengan standar Python.

2. **Penggunaan Variabel untuk Jalur .zsh_history**:
   - Menyimpan jalur `.zsh_history` dalam variabel `zsh_history_path` untuk menghindari pengulangan pemanggilan `os.path.expanduser`.

3. **Pemberian Komentar untuk Penjelasan Kode**:
   - Menambahkan komentar untuk memberikan penjelasan tentang apa yang dilakukan oleh setiap bagian dari kode.

4. **Penambahan Pemeriksaan Eksistensi File .zsh_history**:
   - Memeriksa apakah file `.zsh_history` ada sebelum mencoba membukanya. Ini mencegah kesalahan jika file tersebut tidak ada.

5. **Penggunaan Fungsi os.path.expanduser**:
   - Menggunakan `os.path.expanduser` untuk memperluas jalur rumah pengguna.

6. **Pemindahan String Format**:
   - Memindahkan string format dari `os.system` ke variabel sebelumnya untuk memungkinkan interpolasi string.

7. **Penyesuaian Pesan Output**:
   - Mengubah pesan output untuk memberikan informasi yang lebih jelas tentang tindakan yang diambil.

8. **Penambahan Fitur atau Bugfix**:
   - Tidak ada penambahan fitur baru atau bugfix yang dilakukan.

9. **Peningkatan Keseluruhan Keterbacaan**:
   - Dengan memperbaiki sintaks dan memberikan komentar, skrip ini sekarang lebih mudah dibaca dan dipahami.

10. **Kekurangan atau Masalah**:
    - Tidak ada masalah besar dalam skrip ini, namun ada beberapa pertimbangan keamanan dan risiko yang perlu diingat.
        - Penggunaan `sudo` dapat menyebabkan masalah jika tidak dijalankan dengan hati-hati.
        - Penghapusan file harus dilakukan dengan hati-hati karena tidak dapat dikembalikan.

11. **Saran**:
    - Menambahkan dokumentasi atau komentar tambahan untuk memberikan konteks lebih lanjut tentang tujuan dan penggunaan skrip ini.

Pastikan untuk melakukan pengujian ekstensif sebelum menggunakan skrip ini di lingkungan produksi. Jika Anda mempertimbangkan penggunaan di lingkungan produksi yang penting, pertimbangkan untuk meminta ulasan dari rekan atau profesional IT yang berpengalaman.
