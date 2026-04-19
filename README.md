# 🏥 Health Center Management System

[🇹🇷 Türkçe](#-türkçe) | [🇺🇸 English](#-english) | [🇩🇪 Deutsch](#-deutsch)

---

## 🇹🇷 Türkçe

### 📋 Proje Hakkında
Bu proje, bir sağlık merkezi için **randevu yönetimi**, **hasta kayıt işlemleri**, **doktor takibi** ve **ödeme süreçlerini** (Iyzico entegrasyonu) kolaylaştırmak amacıyla geliştirilmiş bir **Django** tabanlı web uygulamasıdır. Kullanıcı dostu arayüzü sayesinde randevu oluşturma ve yönetim süreçleri hızlıca gerçekleştirilebilir.

### 🚀 Özellikler
- 📅 **Randevu Sistemi:** Hastaların bölüm seçerek uygun tarih ve saate göre randevu oluşturması.
- 💳 **Ödeme Entegrasyonu:** Iyzico (Iyzipay) üzerinden güvenli ödeme altyapısı.
- 👩‍⚕️ **Doktor & Ekip Yönetimi:** Sağlık merkezi personelinin ve doktorların profillerinin yönetimi.
- 📰 **Haberler & Duyurular:** Dinamik haber ve duyuru içerikleri.
- 🔐 **Gelişmiş Admin Paneli:** Tüm kayıtların (randevu, hasta, ekip) yönetilebileceği panel.
- 📱 **Responsive Tasarım:** Bootstrap 5 ile tüm cihazlara uyumlu arayüz.

### 🛠️ Kullanılan Teknolojiler
- **Backend:** Python, Django 4.2+
- **Veritabanı:** SQLite3
- **Ödeme:** Iyzico API (Iyzipay)
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5, FontAwesome

### ⚙️ Kurulum
1. Repoyu klonlayın: `git clone https://github.com/mhilmicicek07/py_HealthCenter.git`
2. Dizin içerisine girin: `cd py_HealthCenter`
3. (Tercihen) sanal ortam oluşturun ve aktive edin: `python -m venv .venv && source .venv/bin/activate`
4. Bağımlılıkları yükleyin: `pip install -r requirements.txt`
5. Ortam değişkenlerini ayarlayın (aşağıya bakın). Yerelde bir `.env` dosyası kullanabilirsiniz.
6. Veritabanını güncelleyin: `python manage.py migrate`
7. Yönetici hesabı oluşturun (opsiyonel): `python manage.py createsuperuser`
8. Statik dosyaları toplayın (deploy için önerilir): `python manage.py collectstatic --noinput`
9. Sunucuyu başlatın: `python manage.py runserver`

### 🔑 Ortam Değişkenleri
- `DJANGO_SECRET_KEY` (üretimde kendi anahtarınızı girin; aksi halde varsayılan geliştirme anahtarı kullanılır)
- `DJANGO_DEBUG` (`True` / `False`, varsayılan `True`)
- `DJANGO_ALLOWED_HOSTS` (virgülle ayrılmış host listesi, boş bırakılırsa `[]`)
- `IYZIPAY_API_KEY`, `IYZIPAY_SECRET_KEY`, `IYZIPAY_BASE_URL` (varsayılan: `https://sandbox-api.iyzipay.com`) ödeme entegrasyonu için kullanılır.
- Değer girmezseniz sandbox anahtarları devreye girer; üretim için kendi anahtarlarınızı tanımlayın.

### 🧪 Test
- `python manage.py test`

---

## 🇺🇸 English

### 📋 About the Project
This project is a **Django-based** web application designed to streamline **appointment management**, **patient registration**, **doctor tracking**, and **payment processes** (Iyzico integration) for a health center. Its user-friendly interface allows for quick appointment creation and management.

### 🚀 Features
- 📅 **Appointment System:** Patients can choose a department and schedule appointments based on date and time.
- 💳 **Payment Integration:** Secure payment infrastructure via Iyzico (Iyzipay).
- 👩‍⚕️ **Doctor & Team Management:** Management of profiles for medical staff and doctors.
- 📰 **News & Announcements:** Dynamic news and announcement content.
- 🔐 **Advanced Admin Panel:** A panel to manage all records (appointments, patients, team).
- 📱 **Responsive Design:** Interface compatible with all devices using Bootstrap 5.

### 🛠️ Technologies Used
- **Backend:** Python, Django 4.2+
- **Database:** SQLite3
- **Payment:** Iyzico API (Iyzipay)
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5, FontAwesome

### ⚙️ Installation
1. Clone the repo: `git clone https://github.com/mhilmicicek07/py_HealthCenter.git`
2. Navigate to directory: `cd py_HealthCenter`
3. (Optional) create & activate a virtualenv: `python -m venv .venv && source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Configure environment variables (see below); a local `.env` works fine.
6. Apply migrations: `python manage.py migrate`
7. Create a superuser (optional): `python manage.py createsuperuser`
8. Collect static files for deployment: `python manage.py collectstatic --noinput`
9. Start the server: `python manage.py runserver`

### 🔑 Environment Variables
- `DJANGO_SECRET_KEY` (set your own key for production; otherwise the dev key is used)
- `DJANGO_DEBUG` (`True` / `False`, defaults to `True`)
- `DJANGO_ALLOWED_HOSTS` (comma-separated list; empty means `[]`)
- `IYZIPAY_API_KEY`, `IYZIPAY_SECRET_KEY`, `IYZIPAY_BASE_URL` (default: `https://sandbox-api.iyzipay.com`) for payment integration.
- Sandbox keys are used by default; set your own for production.

### 🧪 Tests
- `python manage.py test`

---

## 🇩🇪 Deutsch

### 📋 Über das Projekt
Dieses Projekt ist eine **Django-basierte** Webanwendung, die entwickelt wurde, um **Terminmanagement**, **Patientenregistrierung**, **Arztverfolgung** und **Zahlungsprozesse** (Iyzico-Integration) für ein Gesundheitszentrum zu optimieren. Die benutzerfreundliche Oberfläche ermöglicht eine schnelle Terminerstellung und -verwaltung.

### 🚀 Funktionen
- 📅 **Terminsystem:** Patienten können eine Abteilung wählen und Termine nach Datum und Uhrzeit vereinbaren.
- 💳 **Zahlungsintegration:** Sichere Zahlungsinfrastruktur über Iyzico (Iyzipay).
- 👩‍⚕️ **Arzt- & Team-Management:** Verwaltung von Profilen für medizinisches Personal und Ärzte.
- 📰 **Nachrichten & Ankündigungen:** Dynamische Inhalte für Nachrichten und Ankündigungen.
- 🔐 **Erweitertes Admin-Panel:** Ein Panel zur Verwaltung aller Datensätze (Termine, Patienten, Team).
- 📱 **Responsive Design:** Mit Bootstrap 5 kompatible Benutzeroberfläche für alle Geräte.

### 🛠️ Verwendete Technologien
- **Backend:** Python, Django 4.2+
- **Datenbank:** SQLite3
- **Zahlung:** Iyzico API (Iyzipay)
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5, FontAwesome

### ⚙️ Installation
1. Repository klonen: `git clone https://github.com/mhilmicicek07/py_HealthCenter.git`
2. In das Verzeichnis wechseln: `cd py_HealthCenter`
3. (Optional) virtuelle Umgebung erstellen & aktivieren: `python -m venv .venv && source .venv/bin/activate`
4. Abhängigkeiten installieren: `pip install -r requirements.txt`
5. Umgebungsvariablen setzen (siehe unten); lokal geht das bequem über eine `.env`.
6. Datenbank migrieren: `python manage.py migrate`
7. Superuser erstellen (optional): `python manage.py createsuperuser`
8. Statische Dateien sammeln (für Deploy empfohlen): `python manage.py collectstatic --noinput`
9. Server starten: `python manage.py runserver`

### 🔑 Umgebungsvariablen
- `DJANGO_SECRET_KEY` (in Produktion einen eigenen Schlüssel setzen, sonst wird der Dev-Schlüssel genutzt)
- `DJANGO_DEBUG` (`True` / `False`, Standard `True`)
- `DJANGO_ALLOWED_HOSTS` (kommagetrennte Liste; leer bedeutet `[]`)
- `IYZIPAY_API_KEY`, `IYZIPAY_SECRET_KEY`, `IYZIPAY_BASE_URL` (Standard: `https://sandbox-api.iyzipay.com`) für die Zahlungsintegration.
- Ohne eigene Werte greifen Sandbox-Schlüssel; für Produktion bitte ersetzen.

### 🧪 Tests
- `python manage.py test`

---

### 👨‍💻 Developer
**Mehmet Hilmi Çiçek**
- 💼 Full Stack Web Developer
- 📍 Geislingen an der Steige

### 🪪 License
This project is open source. Feel free to use and improve it.
