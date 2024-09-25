# Gallery Sport

Aplikasi web e-commerce berbasis Django bernama Gallery Sport ini menjual berbagai pakaian olahraga, memungkinkan pengguna untuk dengan mudah menelusuri katalog produk, melihat detail seperti nama, harga, deskripsi, kuantitas, dan diskon, serta menambahkan produk ke keranjang belanja mereka. Proyek ini di-deploy secara online menggunakan PWS (Platform-as-a-Service), sehingga pengguna dapat mengaksesnya dari mana saja. Dengan antarmuka yang intuitif dan fitur manajemen produk yang lengkap, Gallery Sport menawarkan pengalaman berbelanja yang nyaman bagi pelanggan yang ingin memenuhi kebutuhan olahraga mereka.


## Deployment 🚀
Aplikasi ini dapat dapat diakses di tautan berikut 
[[Link Aplikasi](http://kaindra-rizq-gallerysport.pbp.cs.ui.ac.id/)]

## Menjawab Pertanyaan Tugas 3 📋

### 1. Perbedaan antara `HttpResponseRedirect()` dan `redirect()`
- **`HttpResponseRedirect(url)`**: Fungsi ini mengarahkan pengguna ke URL tertentu dan mengembalikan `HttpResponseRedirect` sebagai respons. Untuk menggunakan fungsi ini, kita harus menyediakan URL lengkap yang ingin dituju. Biasanya digunakan jika kita ingin memberikan respons pengalihan secara langsung dari suatu URL.
  
- **`redirect(viewname, *args, **kwargs)`**: Fungsi ini lebih fleksibel karena dapat menerima nama view, URL, atau objek dan mengonversinya secara otomatis menjadi URL yang benar sebelum mengarahkan pengguna. Fungsi ini mengembalikan `redirect`. Hal ini memungkinkan penggunaan pengalihan yang lebih mudah terutama ketika bekerja dengan URL patterns yang didefinisikan dalam proyek.

### 2. Cara Kerja Penghubungan Model `Product` dengan `User`
Penghubungan antara `Product` dan `User` dilakukan dengan menggunakan `ForeignKey` pada model `Product`. `ForeignKey` ini memungkinkan setiap entri `Product` memiliki keterkaitan dengan satu entri `User`. 
- Misalnya, jika pengguna membuat produk, produk tersebut akan menyimpan referensi pengguna sebagai pemiliknya. Jika pengguna dihapus dari database, maka seluruh produk yang dimilikinya juga ikut terhapus karena adanya parameter `on_delete=models.CASCADE` pada `ForeignKey`.
- Hubungan ini membuat data `Product` bersifat dinamis dan terkait langsung dengan data pengguna yang membuatnya, menciptakan keterkaitan one-to-many, di mana satu pengguna dapat memiliki banyak produk, tetapi setiap produk hanya bisa dimiliki oleh satu pengguna.

### 3. Perbedaan antara Authentication dan Authorization, serta Implementasinya dalam Django
- **Authentication**: Proses untuk memastikan identitas pengguna, di mana sistem memverifikasi apakah pengguna benar-benar adalah siapa yang mereka klaim. Misalnya, saat pengguna login, mereka diminta memasukkan `username` dan `password`. Jika data ini cocok dengan yang ada di database, maka pengguna dianggap telah terotentikasi dan dapat mengakses platform.
  
- **Authorization**: Proses untuk menentukan hak akses pengguna setelah terotentikasi. Ini berarti memastikan apakah pengguna yang telah login memiliki izin untuk mengakses halaman tertentu atau melakukan tindakan tertentu. 
- **Implementasi di Django**:
  - Saat pengguna login, fungsi `login_user(request)` digunakan untuk mengautentikasi pengguna dengan `AuthenticationForm`. Jika valid, pengguna akan diarahkan ke halaman utama, dan Django membuat sesi untuk pengguna tersebut.
  - Untuk Authorization, Django menggunakan dekorator seperti `@login_required` untuk memastikan hanya pengguna terautentikasi yang dapat mengakses fungsi view tertentu. Django juga memiliki mekanisme izin yang lebih spesifik untuk mengontrol akses ke fitur aplikasi.

### 4. Bagaimana Django Mengingat Pengguna yang Telah Login
Django menggunakan **session cookies** untuk mengingat pengguna yang telah login. Setelah pengguna berhasil login, Django membuat sesi yang berisi informasi pengguna, dan menyimpan `session_id` pada cookie di browser pengguna.
- Saat pengguna mengunjungi halaman lain, `session_id` ini dikirim ke server untuk mencocokkan dengan data sesi yang ada, sehingga Django mengetahui siapa pengguna tersebut.
- Selain itu, cookies juga dapat digunakan untuk menyimpan preferensi pengguna atau data tertentu. Namun, tidak semua cookies aman, karena cookies dapat digunakan oleh pihak ketiga untuk melacak aktivitas pengguna. Oleh karena itu, Django menyediakan opsi untuk membuat secure cookies yang hanya dikirim melalui HTTPS.

### 5. Penjelasan Implementasi Checklist Secara Step-by-Step

#### **Mengimplementasikan Fungsi Registrasi, Login, dan Logout**
- Aku membuat fungsi `register(request)` yang menggunakan `UserCreationForm` untuk memungkinkan pengguna mendaftar akun baru. Setelah registrasi berhasil, `redirect` akan membawa pengguna ke halaman login.
- Untuk login, aku membuat fungsi `login_user(request)` yang menggunakan `AuthenticationForm`. Jika form valid, fungsi `login()` akan mengautentikasi pengguna dan mengarahkan mereka ke halaman utama dengan `redirect`.
- Fungsi `logout_user(request)` digunakan untuk mengakhiri sesi pengguna dengan memanggil `logout()` dan menghapus informasi sesi. Ini mengarahkan pengguna kembali ke halaman login menggunakan `HttpResponseRedirect`.

#### **Membuat Dua Akun Pengguna dengan Tiga Dummy Data untuk Setiap Akun**
- Setelah mengimplementasikan fungsi login dan registrasi, aku membuat dua akun pengguna melalui halaman registrasi.
- Aku login menggunakan setiap akun dan membuat tiga dummy data produk untuk masing-masing akun menggunakan fitur `create_product_entry`. Produk ini kemudian disimpan dalam database dan dihubungkan dengan pengguna yang membuatnya.

#### **Menghubungkan Model Product dengan User**
- Dalam model `Product`, aku menambahkan `ForeignKey` ke model `User`. Ini memastikan bahwa setiap produk yang dibuat terkait langsung dengan pengguna yang membuatnya.
- Dalam `create_product_entry(request)`, aku memastikan `product_entry.user = request.user` sebelum menyimpan produk, sehingga produk selalu terasosiasi dengan pengguna yang sedang login.

#### **Menampilkan Detail Informasi Pengguna yang Sedang Login**
- Aku membuat fungsi `show_main(request)` yang mengambil data produk yang terkait dengan `request.user`. Hal ini memastikan hanya produk yang dimiliki oleh pengguna yang sedang login yang akan ditampilkan di halaman utama.
- Informasi pengguna seperti `username` ditampilkan di halaman utama, bersama dengan data `last_login` yang disimpan dalam cookies.

#### **Menggunakan Cookies untuk Last Login**
- Saat pengguna login melalui `login_user(request)`, aku menyimpan waktu login terakhir menggunakan `response.set_cookie('last_login', str(datetime.datetime.now()))`.
- Data `last_login` ini kemudian ditampilkan di halaman utama untuk menunjukkan kapan terakhir kali pengguna login. Dengan demikian, pengguna mendapatkan pengalaman yang lebih personal.



