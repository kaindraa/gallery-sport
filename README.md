# Gallery Sport

Aplikasi web e-commerce berbasis Django bernama Gallery Sport ini menjual berbagai pakaian olahraga, memungkinkan pengguna untuk dengan mudah menelusuri katalog produk, melihat detail seperti nama, harga, deskripsi, kuantitas, dan diskon, serta menambahkan produk ke keranjang belanja mereka. Proyek ini di-deploy secara online menggunakan PWS (Platform-as-a-Service), sehingga pengguna dapat mengaksesnya dari mana saja. Dengan antarmuka yang intuitif dan fitur manajemen produk yang lengkap, Gallery Sport menawarkan pengalaman berbelanja yang nyaman bagi pelanggan yang ingin memenuhi kebutuhan olahraga mereka.


## Deployment 🚀
Aplikasi ini dapat dapat diakses di tautan berikut 
[[Link Aplikasi](http://kaindra-rizq-gallerysport.pbp.cs.ui.ac.id/)]

## Menjawab Pertanyaan-Pertanyaan 📋

### 1. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery penting dalam pengimplementasian platform karena memungkinkan data untuk berpindah dari satu titik ke titik lain (server ke klien atau antar layanan). Dengan data delivery yang baik, platform dapat memberikan respons yang cepat dan efisien kepada pengguna, menjaga integritas data, dan memastikan bahwa informasi dapat diakses secara real-time. Ini juga penting dalam skalabilitas dan interoperabilitas sistem, terutama jika platform melibatkan banyak komponen atau microservices.

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

JSON lebih baik dalam konteks web modern karena lebih ringan, lebih mudah dibaca oleh manusia, dan lebih cepat diproses oleh mesin. JSON juga lebih mudah digunakan dalam bahasa pemrograman seperti JavaScript, yang menjadi salah satu alasan popularitasnya. Sementara XML memiliki struktur yang lebih kompleks dan mendukung skema formal yang lebih baik, JSON lebih efisien untuk pengiriman data dalam aplikasi web dan API karena formatnya yang lebih sederhana dan kompak.

### 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

Method `is_valid()` pada form Django digunakan untuk memvalidasi data yang dikirimkan melalui form. Method ini akan mengecek apakah data yang dimasukkan sesuai dengan aturan validasi yang telah ditentukan (misalnya, format email yang benar atau angka yang berada dalam rentang tertentu). Jika data valid, method ini akan mengembalikan `True`, dan memungkinkan data untuk diproses lebih lanjut, misalnya disimpan ke database. Jika data tidak valid, method ini mengembalikan `False` dan memungkinkan form menampilkan pesan error kepada pengguna.

### 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

`csrf_token` diperlukan untuk melindungi aplikasi Django dari serangan CSRF (Cross-Site Request Forgery). CSRF adalah serangan di mana penyerang mencoba memanipulasi tindakan yang dilakukan oleh pengguna di aplikasi tanpa sepengetahuan mereka. Jika tidak ada `csrf_token`, penyerang dapat membuat pengguna mengirimkan request berbahaya yang tampak sah (misalnya, transfer uang atau pengubahan pengaturan akun). Dengan `csrf_token`, setiap form memiliki token unik yang harus cocok dengan token yang disimpan di server, sehingga memitigasi risiko serangan ini.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)?

Untuk memenuhi checklist, aku membuat empat fungsi views: `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` untuk menampilkan data produk dalam format XML dan JSON, baik untuk semua produk maupun berdasarkan ID. Data diambil menggunakan query ke database dan dikonversi dengan `serializers` dari Django. aku kemudian menambahkan routing di `urls.py` untuk setiap view tersebut dengan path yang sesuai, seperti `/xml/`, `/json/`, dan versi dengan ID untuk menampilkan produk tertentu. Setelah itu, aku menguji setiap view melalui browser untuk memastikan data ditampilkan dengan benar dalam format yang diminta.

