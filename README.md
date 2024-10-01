# Gallery Sport

Aplikasi web e-commerce berbasis Django bernama Gallery Sport ini menjual berbagai pakaian olahraga, memungkinkan pengguna untuk dengan mudah menelusuri katalog produk, melihat detail seperti nama, harga, deskripsi, kuantitas, dan diskon, serta menambahkan produk ke keranjang belanja mereka. Proyek ini di-deploy secara online menggunakan PWS (Platform-as-a-Service), sehingga pengguna dapat mengaksesnya dari mana saja. Dengan antarmuka yang intuitif dan fitur manajemen produk yang lengkap, Gallery Sport menawarkan pengalaman berbelanja yang nyaman bagi pelanggan yang ingin memenuhi kebutuhan olahraga mereka.


## Deployment 🚀
Aplikasi ini dapat dapat diakses di tautan berikut 
[[Link Aplikasi](http://kaindra-rizq-gallerysport.pbp.cs.ui.ac.id/)]

## Menjawab Pertanyaan Tugas 4 📋

### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
- **Inline Style**: CSS yang langsung didefinisikan pada elemen HTML memiliki prioritas tertinggi dan akan diterapkan di atas semua jenis CSS lainnya.
- **External dan Internal Style Sheets**: Jika ada konflik antara CSS di file eksternal dan internal, CSS yang ditulis paling akhir akan diutamakan. Style sheet internal lebih spesifik jika ditulis setelah external.
- **Browser Default**: Ini adalah gaya bawaan browser dan memiliki prioritas paling rendah. Gaya ini hanya akan diterapkan jika tidak ada aturan CSS lain yang mengubah elemen tersebut.

### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
- **Pentingnya**: Responsive design memungkinkan website untuk beradaptasi dengan berbagai ukuran layar, sehingga meningkatkan pengalaman pengguna di berbagai perangkat (desktop, tablet, mobile). Hal ini penting karena pengguna bisa mengakses website dari perangkat apapun.
- **Contoh Aplikasi**:
  - **Sudah Menerapkan**: Aplikasi seperti Spotify yang tata letaknya berubah dengan baik saat dilihat di perangkat berbeda.
  - **Belum Menerapkan**: Beberapa situs web lama yang hanya dirancang untuk layar desktop dan terlihat buruk saat dibuka di perangkat mobile.

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
- **Margin**: Ruang di luar elemen, memberikan jarak antara elemen tersebut dengan elemen lainnya. Contoh: `margin: 10px;`
- **Border**: Garis yang mengelilingi elemen, berada di antara margin dan padding. Contoh: `border: 2px solid black;`
- **Padding**: Ruang di dalam elemen, memberikan jarak antara konten elemen dengan batas dalam elemen. Contoh: `padding: 10px;`

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
- **Flexbox**: Sebuah layout model yang digunakan untuk mengatur elemen dalam satu dimensi (baris atau kolom). Sangat berguna untuk membuat tata letak yang responsif dan mengatur distribusi ruang antar elemen. Contoh implementasi: `display: flex;`
- **Grid Layout**: Sebuah layout model dua dimensi yang memungkinkan kita untuk mengatur elemen dalam baris dan kolom. Berguna untuk membuat tata letak yang lebih kompleks dan terstruktur. Contoh implementasi: `display: grid;`

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- **Langkah 1: Membuat Fungsi Edit dan Delete Product**: Aku memulai dengan membuat fungsi `edit_product` dan `delete_product` di `views.py`, kemudian mengonfigurasinya di `urls.py` agar rute-rute ini dapat diakses. Setelah itu, aku membuat file `edit_product.html` untuk tampilan halaman edit produk.

- **Langkah 2: Integrasi dengan Tailwind CSS**: Selanjutnya, aku mengintegrasikan proyek ini dengan Tailwind CSS untuk memudahkan proses desain dan memastikan tampilan yang konsisten.

- **Langkah 3: Mendesain Semua Halaman HTML**: Aku mendesain ulang semua halaman HTML agar memiliki tata letak yang konsisten, menggunakan Tailwind CSS untuk menciptakan tampilan yang menarik dan responsif.

- **Langkah 4: Membuat card_info.html**: Aku membuat file `card_info.html` untuk menampilkan informasi produk dalam bentuk kartu yang rapi. Di dalam card ini, aku menambahkan tombol "Edit" dan "Delete" yang terhubung dengan fungsi `edit_product` dan `delete_product`.

- **Langkah 5: Membuat dan Mengintegrasikan Navbar yang Responsif**: Aku membuat *navbar* yang responsif menggunakan Tailwind CSS dan JavaScript. Navbar ini memiliki ikon burger menu yang muncul ketika dilihat di perangkat mobile, sehingga memudahkan navigasi di berbagai ukuran layar.




