https://rashika-maharani-eshoppbp.pbp.cs.ui.ac.id/

# Tugas 2
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Hal pertama yang saya lakukan adalah membuat proyek Django baru dengan menyalakan virtual environment dan menginstal aplikasi-aplikasi yang dibutuhkan pada <requirements.txt>. Setelah itu saya menjalankan perintah <django-admin startproject eshop_pbp .> sehingga terciptalah proyek <eshop_pbp>.
    - Selanjutnya saya membuat aplikasi baru yaitu main dengan menjalankan perintah <py manage.py startapp main> sehingga terbentuk folder <main> di dalam proyek.
    - Untuk melakukan routing proyek ke aplikasi main, saya menambahkan baris <path('', include('main.urls'))> pada file <urls.py> di bagian <urlpatterns> sehingga semua request ke root dapat diarahkan ke aplikasi <main>.
    - Untuk membuat model product di aplikasi main, saya mengisi <model.py> dengan <product> yang memiliki atribut:
        - <name>:<CharField>
        - <price>:<IntegerField>
        - <descriptiom>:<TextField>
        - <thumbnail>:<UrlField>
        - <cetgory>:<CharField>
        - <isFeatured>:<BooleanField>
        - saya juga menambahkan variabel <stock>:<PositiveIntegerField>
    - Selanjutnya saya membuat fungsi di <views.py> untuk template HTML dengan menambahkan fungsi <show_main> yang akan mengirim context nama aplikasi, nama saya, dan kelas ke template <main.html>.
    - Untuk routing pada <url.py> di aplikasi main, saya menambahkan <path('', show_main, name='show_main')> di bagian <urlpatterns> untuk memetakan root aplikasi ke fungsi <show_main>.
    - Terakhir untuk deployment ke PWS, saya telah menyiapkan file <.env.prod> sebelumnya dan mengatur setting database PostreSQL di <settings.py>, lalu melakukan deploy ke PWS
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    https://drive.google.com/file/d/1kaNdpuV34fBlfQ0zA85iuWSas7c4Cfqe/view?usp=sharing
    Pertama, permintaan yang masuk ke dalam server Django akan diproses melalui <urls.py> untuk diteruskan ke <views.py>. Apabila terdapat proses yang membutuhkan keterlibatan database, maka nantinya <views.py> akan memanggil query ke <models.py> dan database akan mengembalikan hasil dari query tersebut ke <views.py>. Setelah permintaan telah selesai diproses, hasil proses tersebut akan dipetakan ke dalam HTML yang sudah didefinisikan sebelum <main.html> akhirnya HTML tersebut dikembalikan ke pengguna sebagai respons.
3. Jelaskan peran settings.py dalam proyek Django!
    Peran <settings.py> di Django ialah, <settings.py> berisi seluruh konfigurasi proyek Django, seperti database, aplikasi yang digunakan, middleware, pengaturan keamanan, path static files, dan konfigurasi lainnya.
4. Bagaimana cara kerja migrasi database di Django?
    - Model diubah di <models.py>.
    - Jalankan perintah <py manage.py makemigrations> pada (env) untuk membuat file migrasi.
    - Jalankan perintah <py manage.py migrate> pada (env) untuk menerapkan perubahan ke database.
5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    - Dokumentasinya lengkap dan memiliki komunitas yang besar.
    - Memiliki konsep MVC (Model-View-Controller) yang jelas.
    - Banyak fitur built-in (seperti: admin, ORM, dan keamanan).
    - Cocok untuk belajar pengembangan web secara terstruktur.
6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    Saya sangat mengapresiasi hasil bimbingan dari asisten dosen kepada mahasiswa karena sudah sabar dan cepat tanggap. Mungkin untuk saran kedepannya asisten dosen bisa bersikap adil atau bisa lebih membagi waktu dalam memberikan bantuan lab ke mahasiswa lain, bukan hanya terpaku pada 1 orang dalam waktu yang lama. Terimakasih.

# Tugas 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Data delivery diperlukan agar data dapat dipertukarkan antara server dan client ataupun antar sistem yang berbeda. Dengan data delivery, aplikasi dapat menampilkan, mengirim, dan menerima data secara dinamis baik dalam bentuk API (JSON/XML) maupun file. Hal ini tentunya penting untuk integrasi serta pengalaman pengguna secara real-time.
2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    JSON lebih baik untuk kebanyakan aplikasi web karena:
    - Lebih ringan dan mudah dibaca.
    - Parsing lebih cepat dan mudah diimplementasikan di berbagai bahasa pemrograman.
    - Struktur data yang lebih sederhana dan langsung cocok dengan objek di JavaScript.
    JSON lebih populer kemungkinan karena alasan di atas, sedangkan XML parsingnya lebih berat.
3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    Method <is_valid()> digunakan untuk memeriksa apakah data yang dikirimkan melalui form sudah sesuai dengan aturan validasi yang ditentukan pada form. Jika valid, method ini akan mengisi atribut <cleaned_data> pada form. Kita tentunya membutuhkan method ini agar data yang masuk ke database dapat dipastikan sudah benar dan aman, serta untuk mencegah error atau munculnya data yang tidak valid.
4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    <csrf_token> dibutuhkan untuk mencegah serangan CSRF (Cross Site Request Forgery) yaitu serangan di mana penyerang memanfaatkan sesi login user untuk mengirim permintaan tanpa sepengetahuan user. Jika tidak menambahkan <csrf_token>, form bisa dieksploitasi oleh penyerang untuk melakukan aksi berbahaya seperti mengganti password maupun melakukan transaksi atas nama user yang sedang login.
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Saya menambahkan fungsi <show_xml>, <show_json>, <show_xml_by_id>, dan <show_json_by_id> di <views.py> menggunakan import <serializers> dari Django untuk mengembalikan data dalam format yang diminta.
    - Saya menambahkan path baru di <urls.py>:
    <path('xml/', show_xml, name='show_xml')>, 
    <path('json/', show_json, name='show_json')>, 
    <path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id')>, 
    <path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id')>
    - Di halaman utama <main.html> akan menampilkan halaman awal dengan tombol "Add" (redirect ke form tambah produk) dan jika sudah terdapat produk yang terdaftar akan muncuk tombol "Detail" pada setiap produk (redirect ke halaman detail produk tersebut).
    - Saya membuat form di <add_product.html> dan fungsi <add_product> di <views.py> yang menggunakan <ProductForm> untuk menambah produk baru.
    - Saya membuat template <product_detail.html> dan fungsi <show_product> untuk menampilkan detail produk berdasarkan <ID>.
    - Saya menjawab pertanyaan dengan melanjutkan <README.md> dari tugas sebelumnya
    - Saya mengakses endpoint </xml/>, </json/>, </xml/<product_id>/>, dan </json/<peoduct_id>/> di Postman, lalu mengambil screenshot hasilnya dan menambahkannya ke google drive <https://drive.google.com/drive/folders/1QtjxIK2Gqd3tVreBXKvaXjVkdyj33KWf?usp=sharing> pada README.md yang sama dengan tugas sebelumnya.
    - Setelah semua selesai, saya melakukan <git add .>, <git commit -m "Finish tugas 3">, <git push origin master> (untuk push ke repository GitHub), dan <git push pws master> (untuk push ke pws).
6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
    Masih sama seperti sebelumnya.

# Tugas 4
1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
    - Django AuthenticationForm adalah form bawaan Django untuk proses login, yang memvalidasi username dan password terhadap data user di database.
    - Kelebihan:
        1. Mudah digunakan, karena sudah terintegrasi dengan sistem autentikasi Django.
        2. Otomatis melakukan validasi dan error handling.
        3. Aman, karena sudah mengikuti best practice Django.
    - Kekurangan:
        1. Kurang fleksibel untuk custom field atau tampilan.
        2. Hanya mendukung autentikasi berbasis username dan password secara default.
2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
    - Autentikasi adalah proses verifikasi identitas pengguna (login). Menggunakan sistem user dan login/logout bawaan (<AuthenticationForm>, <login>, <logout>).
    - Otorisasi adalah proses pengecekan hak akses pengguna terhadap fitur/data tertentu. Menggunakan decorator seperti <@login_required> dan sistem permission/group pada model dan view.
3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
    - Session:
        Kelebihan: Data disimpan di server, lebih aman, bisa menyimpan data besar.
        Kekurangan: Membebani server, butuh mekanisme session management.
    - Cookies:
        Kelebihan: Disimpan di client, cocok untuk data kecil (misal: preferensi user).
        Kekurangan: Rentan terhadap manipulasi, kapasitas terbatas, bisa dihapus user.
4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
    - Penggunaan cookies tidak sepenuhnya aman secara default. Risiko: pencurian data (XSS), manipulasi cookies, dan CSRF. Django menangani dengan:
    1. Menggunakan HttpOnly dan Secure flag pada cookies.
    2. CSRF protection dengan csrf_token.
    3. Session data tidak disimpan langsung di cookies, hanya session key.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Menambahkan fungsi <registrasi>, <login>, dan <logout> di <views.py> menggunakan <UserCreationForm> dan <AuthenticationForm>.
    - Membuat dua akun user (chazelnut dan chelle) dan masing-masing menambahkan tiga dummy data produk di lokal.
    - Menghubungkan model <Product> dengan <User> menggunakan <ForeignKey>.
    - Menampilkan detail user yang sedang login (<username>) dan menampilkan cookies <last_login> di halaman utama.