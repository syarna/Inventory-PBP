# Tugas 2 - Membuat Inventory Website
Nama  : Syarna Savitri <br>
NPM   : 2206083565 <br>
Kelas : PBP B <br>
Asdos : EDA <br>

## Hasil Website
Website dapat diakses melalui [link ini](https://inventorywebsite-pbp.adaptable.app).


## Penjelasan Cara Penyelesaian Tugas 2
1. Cara pengimplementasian *checklist* untuk menyelesaikan Tugas 2: <br>
   Setelah mempelajari [Tutorial 0](https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-0) dan [Tutorial 1](https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-1), saya menyelesaikan Tugas 2 dengan mempelajari dari banyak sumber.<br>
   Berikut adalah *step-by-step* yang saya buat dengan menyesuaikan *checklist* yang ada pada berkas soal:
   - [x] Mengaktifkan *virtual environtment* untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer.
   - [x] Membuat proyek Django baru untuk menciptakan situs web.
   - [x] Membuat aplikasi `main` agar aplikasi dapat memiliki model, tampilan, template, dan URL yang terkait dengannya. Aplikasi memungkinkan kita untuk membagi fungsionalitas proyek menjadi bagian-bagian terpisah yang dapat dikelola secara independen.
   - [x] Membuat atribut wajib seperti `name`,`amount` dan `description` sesuai dengan tipe *field* yang telah ditentukan.
   - [x] Mengatur routing URL agar aplikasi `main` dapat diakses melalui peramban web.
   - [x] Menjalankan server untuk mengecek apakah hasil website sudah sesuai dengan ketentuan.
   - [x] Melakukan deploy ke [Adaptable](https://adaptable.io) untuk meng-*hosting* webiste.
   
 

3. Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya:
   
4. Penjelasan pada bagan kaitan antara urls.py, views.py, models.py, dan berkas html:
   
5. Alasan untuk menggunakan ***vitual environment***:

6. Apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya?


1. Tambahkan ***remote*** baru bernama **`upstream`** untuk mendapatkan code dari repository DDP2 dengan perintah:
    ```bash
    git remote add upstream https://gitlab.com/DDP2-CSUI/sp-ddp2-2023/tp3-sp-ddp2.git
    ```
    Jika sebelumnya anda telah menambahkan **`upstream`**, Anda dapat mengganti url **`upstream`** ke DDP2 dengan perintah:
    ```bash
    git remote set-url upstream https://gitlab.com/DDP2-CSUI/sp-ddp2-2023/tp3-sp-ddp2.git
    ```
    > Note: Sekarang, pada git anda terdapat 2 source remote, yakni: **`origin`**, repository milik anda dan **`upstream`**, repository DDP2 tempat soal dan template Tugas Pemrograman 3 berada.
2. Buat direktori baru pada folder TP3 anda kemudian pindahkan terminal ke ***path*** tersebut.
3. Lakukan ***pull*** dari remote **`upstream`** dengan perintah 
    ```bash
    git pull upstream main
    ```

## Deskripsi
Tugas ini merupakan pembuatan sistem untuk apotek bernama HaloDDP menggunakan bahasa pemrograman Java. Sistem ini memungkinkan apoteker untuk melakukan input data obat, kalkulasi harga secara otomatis, dan update stok secara real-time. Sistem juga menyediakan fitur tambah obat, lihat obat, beli obat, dan riwayat transaksi.

Pembuatan Lemari: Apoteker dapat membuat lemari dengan ukuran tertentu. Lemari tersebut memiliki rak-rak yang ditentukan oleh apoteker.

Pembuatan Rak: Setelah membuat lemari, apoteker dapat membuat rak-rak pada lemari sesuai dengan kategori obat yang diinginkan.

Tambah Obat: Apoteker dapat menambahkan obat baru ke dalam rak. Obat akan ditempatkan pada posisi yang diinginkan, dan stok obat juga ditentukan.

Lihat Obat: Apoteker dapat melihat daftar obat yang telah diletakkan pada rak-rak lemari. Daftar obat akan mencantumkan nama obat dan stok obat.

Beli Obat: Fitur ini digunakan apoteker untuk melakukan pembelian obat. Apoteker dapat memasukkan nama obat dan jumlah yang ingin dibeli. Jika stok obat mencukupi, maka transaksi berhasil dilakukan. 

Keluar: Fitur ini mengakhiri program dan mencetak riwayat transaksi hari ini. Jika tidak ada transaksi, akan dicetak pesan motivasi.

## Menyelesaikan konflik

Jika terjadi *merge conflict*, silakan selesaikan konflik yang ada dan
lanjutkan proses *merging*. Kamu bisa mencari [panduan](https://githowto.com/resolving_conflicts) atau meminta bantuan asdos jika mengalami kesulitan.
