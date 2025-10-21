# 🏥 Health Center Yönetim Sistemi

Bu proje, bir sağlık merkezi için **randevu yönetimi**, **hasta kayıt işlemleri** ve **doktor takibi** süreçlerini kolaylaştırmak amacıyla geliştirilmiş bir **Django tabanlı web uygulamasıdır**.  
Kullanıcı dostu arayüzü ve yönetim paneli sayesinde, hasta ve doktor bilgilerinin yönetimi, randevu oluşturma ve sistemdeki kayıtların düzenlenmesi kolayca yapılabilir.

---

## 🚀 Özellikler

- 👩‍⚕️ **Hasta Yönetimi:** Yeni hasta ekleme, bilgileri güncelleme, kayıt silme.  
- 🧑‍⚕️ **Doktor Yönetimi:** Doktor profilleri oluşturma ve düzenleme.  
- 📅 **Randevu Sistemi:** Hastalar için uygun tarih ve saate göre randevu oluşturma.  
- 🔐 **Kullanıcı Girişi ve Yetkilendirme:** Admin paneli üzerinden güvenli erişim.  
- 💬 **İletişim Formu:** Ziyaretçilerin sağlık merkeziyle iletişim kurmasını sağlar.  
- 📊 **Dashboard:** Yönetici için genel istatistiklerin görüntülenmesi.  
- 💾 **SQLite Veritabanı:** Verilerin güvenli ve kalıcı şekilde saklanması.  
- 💻 **Responsive Arayüz:** Tüm cihazlarda uyumlu, Bootstrap tabanlı tasarım.  

---

## 🧩 Kullanılan Teknolojiler

| Teknoloji | Rolü |
|------------|-------|
| **Python (Django Framework)** | Sunucu tarafı geliştirme, veri yönetimi ve URL yönlendirme. |
| **SQLite3** | Hafif ve dahili veritabanı sistemi. |
| **HTML5** | Sayfa yapısının oluşturulması. |
| **CSS3 & Bootstrap 5** | Modern, responsive ve düzenli kullanıcı arayüzü. |
| **JavaScript (ES6)** | Dinamik içerik ve etkileşimli özellikler. |
| **FontAwesome** | İkon ve görsel bileşenler. |

---

## 📂 Proje Dosya Yapısı

📁 py_HealthCenter
├── 📁 healthcenter # Ana Django uygulaması
│ ├── settings.py
│ ├── urls.py
│ └── views.py
├── 📁 static # CSS, JS, görseller
│ ├── 📁 css
│ ├── 📁 js
│ └── 📁 images
├── 📁 templates # HTML şablonları
│ ├── index.html
│ ├── about.html
│ ├── contact.html
│ ├── appointment.html
│ └── base.html
├── 📄 manage.py
├── 📄 db.sqlite3
└── 📄 README.md


---

## ⚙️ Kurulum ve Çalıştırma

Bu projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyin:

1. Bu projeyi klonlayın:  
   ```bash
   git clone https://github.com/mhilmicicek07/py_HealthCenter.git
Proje dizinine geçin:


cd py_HealthCenter
Gerekli bağımlılıkları yükleyin (örnek requirements.txt oluşturabilirsiniz):


pip install django pillow
Veritabanını hazırlayın:


python manage.py migrate
Geliştirme sunucusunu başlatın:


python manage.py runserver
Tarayıcıda açın:
👉 http://127.0.0.1:8000

🧠 Teknik Açıklama
Uygulama Django MVC (Model-View-Template) mimarisiyle geliştirilmiştir.
Veritabanı işlemleri models.py dosyasında tanımlanmış, kullanıcı etkileşimleri views.py tarafından yönetilmektedir.
Tüm sayfa tasarımları templates klasöründe düzenlenmiş olup, Bootstrap yardımıyla modern bir arayüz oluşturulmuştur.
Randevu sistemi, kullanıcıların form üzerinden veri girişi yapmasını ve bu verilerin admin panelinde saklanmasını sağlar.

👨‍💻 Geliştirici
Mehmet Hilmi Çiçek
💼 Full Stack Web Developer
📍 Geislingen an der Steige
💬 “Basit ama tutarlı kod, karmaşık olandan her zaman üstündür.”

🪪 Lisans
Bu proje açık kaynaklıdır.
İsteyen herkes kodu inceleyebilir, geliştirebilir veya kişisel projelerinde kullanabilir.