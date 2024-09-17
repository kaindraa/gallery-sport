# Gallery Sport

Aplikasi web e-commerce berbasis Django bernama Gallery Sport ini menjual berbagai pakaian olahraga, memungkinkan pengguna untuk dengan mudah menelusuri katalog produk, melihat detail seperti nama, harga, deskripsi, kuantitas, dan diskon, serta menambahkan produk ke keranjang belanja mereka. Proyek ini di-deploy secara online menggunakan PWS (Platform-as-a-Service), sehingga pengguna dapat mengaksesnya dari mana saja. Dengan antarmuka yang intuitif dan fitur manajemen produk yang lengkap, Gallery Sport menawarkan pengalaman berbelanja yang nyaman bagi pelanggan yang ingin memenuhi kebutuhan olahraga mereka.


## Deployment 🚀
Aplikasi ini dapat dapat diakses di tautan berikut 
[[Link Aplikasi](http://kaindra-rizq-gallerysport.pbp.cs.ui.ac.id/)]

## Langkah Implementasi 🛠

1. **Membuat proyek Django baru**
   - Inisialisasi proyek dengan perintah `django-admin startproject [nama_proyek]` untuk membuat struktur direktori dasar.

2. **Membuat aplikasi dengan nama "main" pada proyek**
   - Tambahkan aplikasi dengan perintah `python manage.py startapp main` yang akan berisi semua logika aplikasi.

3. **Routing proyek ke aplikasi "main"**
   - Di `urls.py` proyek, tambahkan route yang mengarahkan request ke aplikasi "main".

4. **Membuat model Product**
   - Di `models.py` aplikasi "main", buat model `Product` dengan atribut `name`, `description`, `price`, `quantity`, dan `discount`.

5. **Membuat fungsi di views.py**
   - Buat fungsi di `views.py` yang merender template HTML berisi nama aplikasi, nama, dan kelas.

6. **Routing di urls.py aplikasi "main"**
   - Tambahkan route di `urls.py` aplikasi "main" untuk memetakan URL ke fungsi di `views.py`.

7. **Deployment ke PWS**
   - Upload proyek ke PWS agar dapat diakses online.

8. **Membuat README.md**
   - Buat README.md berisi deskripsi proyek, langkah-langkah implementasi, dan tautan aplikasi yang di-deploy.


## Bagan Alur Request dan Response pada Django 🌐

Berikut ini adalah alur request client ke web aplikasi berbasis Django beserta responnya:
![Assignment_1_Diagram_PBP](https://github.com/user-attachments/assets/016725f5-68af-4970-bf6e-07fb564e1066)
**Alur Request Client**


- **Client Request**: Klien mengirimkan request melalui browser ke server.
- **URLs.py**: Request diarahkan oleh `urls.py` ke fungsi di `views.py` yang sesuai.
- **Views.py**: `Views.py` menjalankan logika aplikasi dan berinteraksi dengan `models.py` jika diperlukan.
- **Models.py**: `Models.py` digunakan untuk mengambil atau menyimpan data di database.
- **HTML Response**: Setelah data diperoleh, `views.py` merender template HTML yang sesuai dari folder templates dan mengirimnya kembali sebagai respons ke klien.

## Fungsi Git dalam Pengembangan Perangkat Lunak 👨‍💻

Git adalah sistem kontrol versi yang digunakan untuk melacak perubahan kode, memungkinkan pengembang mengakses dan memulihkan versi sebelumnya. Ini memfasilitasi kolaborasi tim dengan membiarkan setiap orang bekerja pada salinan proyek mereka sendiri, yang dapat digabungkan dengan aman ke repositori utama. Git juga mendukung branching, memungkinkan pengembang mengerjakan fitur atau perbaikan secara terpisah tanpa mengganggu kode utama. Dengan repositori remote, Git memberikan backup terpusat yang aman, serta mendukung code review melalui pull request dan memfasilitasi integrasi berkelanjutan (CI/CD) untuk otomatisasi pengujian dan deployment.

## Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak? 🧐

Django dipilih sebagai framework permulaan pembelajaran pengembangan perangkat lunak karena mendukung pengembangan cepat (rapid development) dan menerapkan praktik terbaik seperti arsitektur Model-View-Template (MVT). Kesederhanaannya memungkinkan pemula untuk memahami konsep dasar seperti routing, templating, dan pengelolaan database tanpa terjebak dalam kode yang kompleks. Selain itu, dokumentasinya yang lengkap dan komunitas yang luas memudahkan pemula untuk menemukan sumber belajar dan solusi atas masalah yang dihadapi.

## Mengapa model pada Django disebut sebagai ORM? 🤖

Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena berfungsi sebagai jembatan antara objek dalam kode Python dan tabel dalam database relasional. ORM memungkinkan pengembang untuk bekerja dengan database menggunakan objek Python tanpa perlu menulis query SQL secara langsung. Dengan ORM, setiap model dalam Django direpresentasikan sebagai kelas Python, di mana atribut kelas mewakili kolom tabel database. Ini memudahkan pengembang untuk berinteraksi dengan database melalui operasi seperti menyimpan, mengambil, memperbarui, dan menghapus data menggunakan sintaks Python yang sederhana.

