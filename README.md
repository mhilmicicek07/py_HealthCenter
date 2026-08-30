# Health Center Management System

[🇹🇷 Türkçe](#-türkçe) | [🇺🇸 English](#-english) | [🇩🇪 Deutsch](#-deutsch)

---

## 🇹🇷 Türkçe

### Proje Hakkında

Django tabanlı bir sağlık merkezi yönetim uygulaması. Randevu oluşturma, ödeme işlemleri, doktor/ekip profil yönetimi ve haber yayınlama gibi işlevleri kapsar.

### Özellikler

- **Randevu Sistemi:** Hastalar bölüm seçerek tarih ve saate göre randevu oluşturur. Çakışan randevular engellenir.
- **Ödeme Entegrasyonu:** Başarılı randevu kaydının ardından Iyzipay checkout formu açılır; ödeme sonucu `/payment/result/` callback'i ile işlenir.
- **Doktor & Ekip Yönetimi:** `Team` uygulaması; isim, branş, dahili numara, e-posta, özgeçmiş ve fotoğraf alanlarını yönetir.
- **Haberler:** `News` uygulaması; kategori, yazar ve slug tabanlı haber içerikleri sunar; en son haberler tüm şablonlarda context processor aracılığıyla erişilebilir.
- **Admin Paneli:** Django'nun yerleşik admin arayüzü; tüm modeller kayıtlıdır.
- **Responsive Tasarım:** Bootstrap 5 ile tüm cihazlara uyumlu arayüz.

### Teknolojiler

- **Backend:** Python, Django 4.2+
- **Veritabanı:** SQLite3
- **Ödeme:** Iyzipay API
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5, FontAwesome

### Gereksinimler

- Python 3.10+
- Paketler: `Django`, `Pillow`, `iyzipay`

### Kurulum

```bash
git clone https://github.com/mhilmicicek07/py_HealthCenter.git
cd py_HealthCenter
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Ortam Değişkenleri

Ödeme modülü (`Payment/views.py`) aşağıdaki değişkenleri okur; tanımlanmazsa sandbox anahtarları kullanılır:

| Değişken | Varsayılan |
|---|---|
| `IYZIPAY_API_KEY` | Sandbox anahtarı |
| `IYZIPAY_SECRET_KEY` | Sandbox anahtarı |
| `IYZIPAY_BASE_URL` | `sandbox-api.iyzipay.com` |

Üretim ortamı için bu değişkenleri kendi anahtarlarınızla tanımlayın.

### Test

```bash
python manage.py test
```

---

## 🇺🇸 English

### About the Project

A Django-based health center management application covering appointment booking, payment processing, doctor/team profile management, and news publishing.

### Features

- **Appointment System:** Patients select a department, date, and time. Conflicting slots are blocked.
- **Payment Integration:** After a successful appointment, an Iyzipay checkout form is presented. The result is handled via the `/payment/result/` callback.
- **Doctor & Team Management:** The `Team` app manages name, specialty, extension, e-mail, bio, and photo for each staff member.
- **News:** The `News` app provides category- and author-based articles with slug-based URLs; latest news is available in all templates via a context processor.
- **Admin Panel:** Django's built-in admin; all models are registered.
- **Responsive Design:** Bootstrap 5 interface compatible with all devices.

### Technologies

- **Backend:** Python, Django 4.2+
- **Database:** SQLite3
- **Payment:** Iyzipay API
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5, FontAwesome

### Requirements

- Python 3.10+
- Packages: `Django`, `Pillow`, `iyzipay`

### Installation

```bash
git clone https://github.com/mhilmicicek07/py_HealthCenter.git
cd py_HealthCenter
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Environment Variables

The payment module (`Payment/views.py`) reads the following variables; sandbox keys are used when they are not set:

| Variable | Default |
|---|---|
| `IYZIPAY_API_KEY` | Sandbox key |
| `IYZIPAY_SECRET_KEY` | Sandbox key |
| `IYZIPAY_BASE_URL` | `sandbox-api.iyzipay.com` |

Set these to your own keys for production.

### Tests

```bash
python manage.py test
```

---

## 🇩🇪 Deutsch

### Über das Projekt

Eine Django-basierte Webanwendung für Gesundheitszentren mit Terminbuchung, Zahlungsabwicklung, Arzt-/Team-Profilverwaltung und Nachrichtenpublikation.

### Funktionen

- **Terminsystem:** Patienten wählen Abteilung, Datum und Uhrzeit. Doppelbuchungen werden verhindert.
- **Zahlungsintegration:** Nach erfolgreicher Terminbuchung wird ein Iyzipay-Checkout-Formular angezeigt; das Ergebnis wird über den `/payment/result/`-Callback verarbeitet.
- **Arzt- & Teamverwaltung:** Die `Team`-App verwaltet Name, Fachgebiet, Durchwahl, E-Mail, Lebenslauf und Foto.
- **Nachrichten:** Die `News`-App bietet kategorie- und autorenbasierte Artikel mit Slug-URLs; aktuelle Nachrichten sind über einen Context Processor in allen Templates verfügbar.
- **Admin-Panel:** Djangos eingebaute Admin-Oberfläche; alle Modelle sind registriert.
- **Responsive Design:** Bootstrap-5-Oberfläche für alle Geräte.

### Technologien

- **Backend:** Python, Django 4.2+
- **Datenbank:** SQLite3
- **Zahlung:** Iyzipay API
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5, FontAwesome

### Voraussetzungen

- Python 3.10+
- Pakete: `Django`, `Pillow`, `iyzipay`

### Installation

```bash
git clone https://github.com/mhilmicicek07/py_HealthCenter.git
cd py_HealthCenter
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Umgebungsvariablen

Das Zahlungsmodul (`Payment/views.py`) liest die folgenden Variablen; ohne Angabe werden Sandbox-Schlüssel genutzt:

| Variable | Standard |
|---|---|
| `IYZIPAY_API_KEY` | Sandbox-Schlüssel |
| `IYZIPAY_SECRET_KEY` | Sandbox-Schlüssel |
| `IYZIPAY_BASE_URL` | `sandbox-api.iyzipay.com` |

Für Produktion eigene Schlüssel setzen.

### Tests

```bash
python manage.py test
```

---

### Developer

**Mehmet Hilmi Çiçek**

### License

This project is open source. Feel free to use and improve it.
