# Tugas - Membuat Inventory Website
Nama  : Syarna Savitri <br>
NPM   : 2206083565 <br>
Kelas : PBP B <br>
Asdos : EDA <br>

## Hasil Website
Website dapat diakses melalui [link ini](https://inventorywebsite-pbp.adaptable.app).


# Penjelasan Cara Penyelesaian Tugas 2
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

# Penjelasan Cara Penyelesaian Tugas 3
Cara pengimplementasian *checklist* untuk menyelesaikan Tugas 3: <br>
   Setelah mempelajari [Tutorial 2](https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-2), saya menyelesaikan Tugas 3 dengan mempelajari dari banyak sumber.<br>
   Berikut adalah *step-by-step* yang saya buat dengan menyesuaikan *checklist* yang ada pada berkas soal:
   
   - [x] Buat berkas baru pada direktori `main` dengan nama `forms.py` untuk membuat struktur form yang dapat menerima data produk baru.
   - [x] Mengubah fungsi `show_main` yang sudah ada pada berkas `views.py`.
   - [x] Membuat sebuah fungsi yang menerima parameter request dengan nama `show_xml`, `show_json`,`show_xml_by_id` dan `show_json_by_id`.
   - [x] Mengatur routing pada masing-masing views.
  
## Perbedaan antara `POST` dan `GET` dalam django
1. Metode Pengiriman Data: <br>
   - **GET**:<br>
     Ketika Anda menggunakan metode GET, data formulir disertakan dalam URL sebagai query string. Ini berarti bahwa data formulir akan terlihat langsung di URL dan dapat dengan mudah diakses oleh pengguna atau oleh siapa pun yang melihat URL tersebut. Metode ini cocok untuk permintaan yang bersifat idempoten (artinya, permintaan dapat diulang tanpa efek samping) dan ketika Anda ingin mengirimkan data ke server untuk pencarian atau pengambilan sederhana.<br> Contoh URL dengan metode GET:<br>
```bash
https://example.com/search/?q=query&category=books
```
   - **POST**:<br>
     Ketika Anda menggunakan metode POST, data formulir disertakan dalam badan permintaan HTTP, dan tidak terlihat langsung di URL. Oleh karena itu, data ini tidak mudah terlihat oleh pengguna atau siapa pun yang melihat URL. Metode ini lebih cocok untuk pengiriman data yang bersifat sensitif atau ketika Anda ingin mengirim data ke server untuk membuat, memperbarui, atau menghapus entitas di server.<br>

2. Jumlah Data yang Dapat Dikirim:
   - **GET**:<br>
     Metode GET memiliki batasan pada jumlah data yang dapat dikirim, karena data dikirim melalui URL. Banyak server web dan browser memiliki batasan panjang URL, dan jika data formulir terlalu besar, Anda mungkin mengalami masalah.
   - **POST**:<br>
     Metode POST tidak memiliki batasan pada jumlah data yang dapat dikirim, karena data dikirim dalam badan permintaan HTTP yang terpisah dari URL.

3. Keamanan:
   - **GET**:<br>
     Data formulir dalam metode GET terlihat di URL, yang berarti data tersebut kurang aman dan dapat dengan mudah diakses oleh pengguna atau pihak ketiga. Oleh karena itu, metode GET tidak cocok untuk mengirim data sensitif seperti kata sandi.
   - **POST**:<br>
     Data formulir dalam metode POST tidak terlihat di URL, sehingga lebih aman daripada GET untuk mengirim data sensitif. Namun, ini bukan jaminan keamanan lengkap, dan Anda harus selalu mengimplementasikan langkah-langkah keamanan tambahan seperti penggunaan HTTPS.

## Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data
XML *(Extensible Markup Language)*, JSON *(JavaScript Object Notation)*, dan HTML *(Hypertext Markup Language)* adalah tiga format yang berbeda untuk mengirim data dalam konteks yang berbeda. Berikut adalah perbedaan utama antara ketiganya dalam konteks pengiriman data:

1. Tujuan Utama:
   - **XML**:<br>
     XML digunakan terutama untuk pertukaran data yang struktural dan semantik, terutama antara aplikasi atau sistem yang berbeda. Ini adalah format yang serbaguna dan dapat digunakan untuk menggambarkan data dengan hierarki yang kompleks dan semantik yang kuat. XML juga sering digunakan dalam konfigurasi dan penyimpanan data.
   - **JSON**:<br>
     JSON awalnya dikembangkan untuk pertukaran data di antara aplikasi web dan server, khususnya dalam konteks JavaScript. Ini adalah format yang ringkas dan mudah dibaca/ditulis oleh manusia, yang membuatnya cocok untuk pertukaran data antara aplikasi web. JSON juga digunakan secara luas untuk penyimpanan data di berbagai aplikasi.
   - **HTML**:<br>
     HTML adalah bahasa markah yang digunakan untuk menggambarkan struktur dan tampilan konten web. HTML tidak digunakan secara eksplisit untuk pertukaran data terstruktur, meskipun data dapat dimasukkan dalam elemen HTML dengan atribut seperti data-*.

2. Struktur Data:
   - **XML**:<br>
     XML memiliki struktur yang sangat fleksibel dan kuat. Data dalam XML dijelaskan oleh dokumen yang dapat memiliki elemen-elemen bersarang dengan atribut dan teks.
   - **JSON**:<br>
     JSON memiliki struktur yang lebih sederhana dibandingkan XML. Data dalam JSON direpresentasikan dalam bentuk pasangan "kunci-nilai" (key-value) dalam bentuk objek atau dalam bentuk array. Ini membuat JSON lebih sederhana untuk diuraikan dan digunakan oleh aplikasi.
   - **HTML**:<br>
     HTML memiliki struktur yang ditentukan oleh elemen-elemen HTML, seperti `<p>`, `<div>`,`<table>`, dan lainnya, yang digunakan untuk mengatur tampilan dan konten halaman web.

3. Penggunaan Khusus:
   - **XML**:<br>
     XML digunakan dalam berbagai konteks, termasuk pertukaran data lintas platform, konfigurasi aplikasi, penyimpanan data berstruktur, dan banyak lagi.
   - **JSON**:<br>
     JSON adalah format yang sangat umum digunakan dalam pengembangan web modern. Ini digunakan untuk pertukaran data antara server dan aplikasi web, penyimpanan data di database NoSQL seperti MongoDB, dan banyak lagi.
   - **HTML**:<br>
     HTML digunakan secara khusus untuk menggambarkan struktur dan tampilan halaman web. Ini adalah bahasa yang digunakan oleh browser web untuk merender halaman web.

4. Contoh Representasi:
   - **XML**:
   ```bash
    <person>
     <name>John Doe</name>
     <age>30</age>
   </person>
     ```
   - **JSON**:
     ```bash
       {
        "person": {
         "name": "John Doe",
          "age": 30
        }
      }
     ```
   - **HTML**:
     ```bash
     <p>Hello, World!</p>
     ```

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
1. Ringkas dan Mudah Dibaca: <br>
   JSON memiliki sintaks yang sederhana dan mudah dipahami oleh manusia. Data dalam JSONdirepresentasikan dalam bentuk pasangan "kunci-nilai" (key-value), yang membuatnya lebih mudah dibaca dan ditulis dibandingkan dengan format lain yang lebih kompleks seperti XML. Ini memungkinkan pengembang untuk dengan cepat memahami struktur data yang dikirim dan diterima.
   
2. Ringan:<br>
   JSON adalah format data yang ringan dalam hal ukuran. Ini menghasilkan payload yang lebih kecil daripada format lain seperti XML, yang mengurangi penggunaan bandwidth dan meningkatkan kinerja transfer data, khususnya dalam lingkungan web dengan koneksi yang terbatas atau lambat. Dukungan untuk Struktur Bersarang: JSON mendukung struktur data bersarang, yang memungkinkan Anda untuk merepresentasikan data yang kompleks dengan cara yang terorganisir. Anda dapat memiliki objek JSON dalam objek JSON, dan ini sangat berguna dalam menggambarkan data yang lebih rumit.
   
3. Dukungan untuk Tipe Data Umum:<br>
   JSON mendukung tipe data umum seperti string, angka, boolean, array, dan objek. Ini memungkinkan Anda untuk merepresentasikan berbagai jenis data dengan mudah. Selain itu, JSON memiliki dukungan yang baik untuk nilai-nilai null.
   
4. Kemampuan untuk Diproses di Sisi Klien:<br>
   JSON cocok dengan baik dengan bahasa pemrograman JavaScript, yang digunakan secara luas di sisi klien (browser web). Oleh karena itu, data JSON dapat dengan mudah diproses oleh JavaScript di dalam browser, membuatnya sangat sesuai untuk aplikasi web yang berinteraksi dengan server.

5. Dukungan di Banyak Bahasa Pemrograman:<br>
   Selain JavaScript, hampir semua bahasa pemrograman modern memiliki dukungan JSON yang baik. Ini membuatnya mudah untuk mengirim dan menerima data JSON di berbagai platform dan teknologi.

6. Standar Industri:<br>
   JSON telah menjadi standar de facto dalam pertukaran data di lingkungan web. Banyak API web dan layanan daring menggunakan JSON sebagai format data standar, sehingga memudahkan integrasi dan interoperabilitas antara berbagai sistem.
   
7. Sistem yang Mudah Dikelola:<br>
   JSON adalah format data yang mudah dikelola, baik dalam hal pembuatan, pemrosesan, atau pemecahan masalah. Ini membuatnya cocok untuk pengembangan dan pemeliharaan aplikasi web. Karena kombinasi dari keunggulan-keunggulan ini, JSON telah menjadi pilihan yang populer dan dominan dalam pertukaran data antara aplikasi web modern, baik dalam konteks API web, pertukaran data antara server dan klien, maupun penyimpanan data di database NoSQL seperti MongoDB.

## Screenshoot Hasil Akses URL pada Postman:
