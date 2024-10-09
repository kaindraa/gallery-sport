# Gallery Sport

Aplikasi web e-commerce berbasis Django bernama Gallery Sport ini menjual berbagai pakaian olahraga, memungkinkan pengguna untuk dengan mudah menelusuri katalog produk, melihat detail seperti nama, harga, deskripsi, kuantitas, dan diskon, serta menambahkan produk ke keranjang belanja mereka. Proyek ini di-deploy secara online menggunakan PWS (Platform-as-a-Service), sehingga pengguna dapat mengaksesnya dari mana saja. Dengan antarmuka yang intuitif dan fitur manajemen produk yang lengkap, Gallery Sport menawarkan pengalaman berbelanja yang nyaman bagi pelanggan yang ingin memenuhi kebutuhan olahraga mereka.


## Deployment 🚀
Aplikasi ini dapat dapat diakses di tautan berikut 
[[Link Aplikasi](http://kaindra-rizq-gallerysport.pbp.cs.ui.ac.id/)]

## Menjawab Pertanyaan Tugas 5 📋

### 1. Manfaat Penggunaan JavaScript dalam Pengembangan Aplikasi Web
JavaScript memiliki peran penting dalam pengembangan aplikasi web modern karena mampu menambah interaktivitas pada halaman web, seperti animasi, validasi formulir, dan dropdown menu. Selain itu, JavaScript membuat aplikasi lebih responsif dengan memungkinkan pembaruan konten halaman tanpa perlu reload seluruh halaman, misalnya dengan AJAX. Di sisi lain, JavaScript memudahkan manipulasi struktur HTML (DOM), yang memungkinkan perubahan dinamis berdasarkan interaksi pengguna, serta memungkinkan validasi data di sisi klien sebelum dikirim ke server untuk mengurangi beban backend.

### 2. Fungsi Await dalam Fetch
Saat menggunakan `fetch()` yang mengembalikan Promise, `await` digunakan untuk menunggu hingga permintaan selesai dan respons diterima sebelum melanjutkan eksekusi kode. `await` menghentikan sementara eksekusi fungsi asinkron hingga Promise selesai, yang membuat pengolahan data lebih mudah dan sinkron. Jika `await` tidak digunakan, fetch akan mengembalikan Promise yang belum diselesaikan, yang berarti bahwa kode berikutnya dapat berjalan tanpa menunggu data, menyebabkan kemungkinan error karena data yang diharapkan belum siap.

### 3. Mengapa Menggunakan Decorator csrf_exempt pada View untuk AJAX POST
Dalam Django, CSRF (Cross-Site Request Forgery) protection secara default mengharuskan setiap permintaan POST disertai dengan token CSRF yang sah. Jika kita menggunakan AJAX POST, Django akan memvalidasi token tersebut. Dengan menambahkan decorator `@csrf_exempt`, kita menonaktifkan validasi CSRF pada view tertentu, yang mempermudah pengiriman AJAX tanpa harus menyertakan token CSRF. Namun, ini dapat berisiko dan sebaiknya digunakan dengan hati-hati. Alternatif yang lebih aman adalah mengirim token CSRF dalam header permintaan AJAX.

### 4. Mengapa Pembersihan Data Input Pengguna Tidak Hanya Dilakukan di Frontend
Pembersihan dan validasi data input di backend penting karena frontend bisa dengan mudah dimanipulasi oleh pengguna jahat. Mereka bisa melewati validasi frontend dan mengirimkan data berbahaya langsung ke server menggunakan alat seperti Postman. Backend memiliki tanggung jawab untuk menjaga integritas data dan melindungi sistem dari serangan seperti Cross-Site Scripting (XSS) dan injeksi. Dengan demikian, backend memastikan bahwa data yang diterima dari berbagai sumber selalu valid dan sesuai aturan bisnis, tidak hanya yang berasal dari antarmuka web.

### 5. Langkah-langkah Implementasi Checklist
Pertama, saya menambahkan fitur AJAX GET untuk menampilkan produk dengan membuat endpoint JSON yang mengambil data produk dari server dan menggunakan fetch untuk menampilkan data di halaman tanpa reload. Kemudian, saya menambahkan fitur AJAX POST untuk menambah produk baru dengan form yang diimplementasikan dalam modal. Data dari form dikirim ke server melalui AJAX POST, lalu daftar produk diperbarui tanpa refresh halaman. Setelah itu, saya memastikan keamanan aplikasi dengan menambahkan validasi CSRF dan sanitasi input di backend menggunakan `strip_tags` untuk mencegah serangan XSS. Akhirnya, saya melakukan pengujian untuk memastikan bahwa semua fitur berfungsi dengan baik, dan data ditampilkan dengan aman di halaman.





