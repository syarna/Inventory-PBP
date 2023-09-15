# Tugas 2 - Membuat Inventory Website
Nama  : Syarna Savitri <br>
NPM   : 2206083565 <br>
Kelas : PBP B <br>
Asdos : EDA <br>

## Hasil Website
Website dapat diakses melalui [link ini](https://inventorywebsite-pbp.adaptable.app).


## Penjelasan Cara Penyelesaian Tugas 2
Cara pengimplementasian *checklist* untuk menyelesaikan Tugas 2: <br>
   Setelah mempelajari [Tutorial 0](https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-0) dan [Tutorial 1](https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-1), saya menyelesaikan Tugas 2 dengan mempelajari dari banyak sumber.<br>
   Berikut adalah *step-by-step* yang saya buat dengan menyesuaikan *checklist* yang ada pada berkas soal:
   - [x] Mengaktifkan *virtual environtment* untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer.
   - [x] Membuat proyek Django baru untuk menciptakan situs web.
   - [x] Membuat aplikasi `main` agar aplikasi dapat memiliki model, tampilan, template, dan URL yang terkait dengannya. Aplikasi memungkinkan kita untuk membagi fungsionalitas proyek menjadi bagian-bagian terpisah yang dapat dikelola secara independen.
   - [x] Membuat atribut wajib seperti `name`,`amount` dan `description` sesuai dengan tipe *field* yang telah ditentukan.
   - [x] Mengatur routing URL agar aplikasi `main` dapat diakses melalui peramban web.
   - [x] Menjalankan server untuk mengecek apakah hasil website sudah sesuai dengan ketentuan.
   - [x] Melakukan deploy ke [Adaptable](https://adaptable.io) untuk meng-*hosting* website.
   
## Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya:
![Bagan Django](https://github.com/syarna/Inventory_PBP/assets/112332315/0a3442b5-4152-4171-9dac-3d7ea3f3b9f7)<br>

Setiap request yang datang dari client (browser) akan dipetakan oleh URLS dan akan diteruskan ke View yang mana View akan memroses request tersebut. View akan memanggil Model untuk melakukan proses membaca atau menulis data ke Database. Setelah itu View akan memanggil template untuk merender data dalam format tertentu(html, xml, json) dan mengirimkan kembali hasilnya dalam bentuk HTTP Response ke client.
   
## Alasan untuk menggunakan ***vitual environment***:
Untuk menjaga ruang terpisah untuk sebuah proyek dengan pustaka dan dependensi di satu tempat. Environment ini spesifik ke proyek tertentu dan tidak berinterfer dengan dependensi proyek lainnya.

## Apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya?
* **MVC** atau yang biasa disebut **Model-View-Controller** adalah suatu model yang seringkali digunakan oleh para pengembang software. Komponen-komponen di dalam arsiteuktur ini yaitu sebagai berikut.
  * Model: Di dalam komponen ini berisi tentang logika bisnis dan status data yang ada di dalam aplikasi. Kompnen ini bertugas untuk mendapatkan dan memanipulasi data, berkomunikasi dengan controller, berinteraksi dengan database, terkadang memperbarui tampilan dari aplikasi yang dikembangkan.
    Di dalam komponen ini berisi tentang logika bisnis dan status data yang ada di dalam aplikasi. Kompnen ini bertugas untuk mendapatkan dan memanipulasi data, berkomunikasi dengan controller, berinteraksi dengan database, terkadang memperbarui tampilan dari aplikasi yang dikembangkan.

  * View: Komponen ini berhubungan dengan antarmuka pengguna yang terdiri dari HTML/CSS.XML. Komponen ini berkomunikasi dengan pengontrol dan terkadang berinteraksi dengan model. View berkerja sama dengan controller untuk menciptakan tampilan dinamis pada aplikasi yang dikembangkan. Selain bertugas untuk menangani antarmuka dan interaksi pengguna, komponen view juga memiliki tugas untuk menyajikan data yang sesuai untuk pengguna.
    
  * Controller: Controller adalah suatu aktivitas/fragmen yang berfungsi sebagai komunikator antara view dan model. Komponen ini membutuhkan suatu input pengguna dari layanan view/REST. Lalu Permintaan “Get Data” diproses dari model dan diteruskan ke view untuk ditampilkan ke pengguna.

  * Kelebihan **MVC**:<br>
    + MVC membuat logika bisnis terpisah dalam Model.
    + Mendukung teknik asynchronous.
    + Jika terjadi suatu modifikasi, maka tidak akan mempengaruhi keseluruhan Model.
    + Proses pengembangan aplikasi yang dilakukan dapat lebih cepat.

  * Kekurangan **MVC**: <br>
    - Arsitektur ini dapat meningkatkan kompleksitas.
    - Pengujian unit terhalang.
    - Controller kode yang besar yang membuat pengembang tidak bisa mengelolahnya.

* **MVT** adalah singkatan dari **Model-View-Template** adalah sebuah konsep arsitektur yang digunakan dalam pengembangan web untuk memisahkan komponen-komponen utama dari sebuah aplikasi. Konsep ini memungkinkan pengembang web untuk mengorganisasi dan mengelola kode dengan lebih terstruktur.
  * **Model**: komponen dalam konsep MVT yang bertanggung jawab untuk mengatur dan mengelola data dari aplikasi. Model mewakili struktur data dan logika aplikasi yang berada di belakang tampilan. Model menghubungkan aplikasi dengan basis data dan mengatur interaksi dengan data tersebut.
    
  * **View**: komponen yang menangani logika presentasi dalam konsep MVT. View mengontrol bagaimana data yang dikelola oleh model akan ditampilkan kepada pengguna. Dalam konteks MVT, view berperan sebagai pengatur tampilan dan mengambil data dari model untuk disajikan kepada pengguna.

  * **Template**: komponen yang berfungsi untuk mengatur tampilan atau antarmuka pengguna. Template memisahkan kode HTML dari logika aplikasi. Dalam MVT, template digunakan untuk merancang tampilan yang akhirnya akan diisi dengan data dari model melalui view.

  * Kelebihan **MVT**:
    + Memisahkan tugas antara logika aplikasi, tampilan, dan data, sehingga memungkinkan pengembang untuk bekerja pada setiap komponen secara terpisah.
    + Kode yang Mudah Dikelola
    + Kode dapat digunakan kembali dalam berbagai bagian aplikasi yang berbeda.
    + Struktur MVT mendukung skalabilitas dengan memungkinkan pengembangan paralel pada setiap komponen.

* **MVVM** atau **Model-View-ViewModel** yang merupakan gabungan dari MVC dan MVP. MVVM awalnya digunakan di dalam Windows Presentation Foundation (WPF) dan Silverlight, yang secara resmi diumumkan pada tahun 2005 oleh John Grossman dalam sebuah posting blog tentang Avalon. Pola yang digunakan berdasarkan gabungan dari MVC dan MVP mencoba untuk lebih jelas dalam memisahkan pengembangan UI dari logika bisnis dan perilaku dalam aplikasi.

  * Model: digunakan untuk MVVM mirip dengan model yang digunakan MVC, dimana model tersebut terdiri dari data dasar yang digunakan untuk menjalankan perangkat lunak.

  * View: digunakan sebagai antarmuka grafis antara pengguna dan pola desain, serta menampilkan output dari data yang telah diproses. View yang digunakan MVVM mirip dengan View yang digunakan dalam MVC.

  * ViewModel: di satu sisi adalah abstraksi dari View, lalu di sisi yang lain, sebagai penyedia pembungkus data model untuk ditautkan. ViewModel terdiri dair Model yang diubah menjadi View, dan berisi perintah yang dapat digunakan oleh View untuk mempengaruhi Model.

  * Kelebihan **MVVP**:
    + Tidak memiliki hubungan (ketergantungan) antara View dan ViewModel.
    + Tidak ada antarmuka antara View dan Model.
    + Pengujian unit yang mudah dan kode yang digerakkan oleh peristiwa (event-driven).
      
  * Kekurangan **MVVP**:
    - Pengembang harus membuat suatu kuantitas yang dapat diukur di setiap komponen UI.
    - Ukuran kode yang terlalu besar.
