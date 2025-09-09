https://rashika-maharani-eshoppbp.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Hal pertama yang saya lakukan adalah membuat proyek Django baru dengan menyalakan virtual environment dan menginstal aplikasi-aplikasi yang dibutuhkan pada <requrements.txt>. Setelah itu saya menjalankan perintah <django-admin startproject eshop_pbp .> sehingga terciptalah proyek <eshop_pbp>.
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