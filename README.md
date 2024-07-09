# Hava Durumu Uygulaması

Bu basit hava durumu uygulaması, tkinter kullanılarak geliştirilmiştir. Kullanıcı bir şehir seçer ve butona tıklar tıklamaz seçilen şehrin o anki hava durumu verilerini getirir.

## Nasıl Kullanılır

1. **Başlangıç Ekranı**

   Uygulama başlatıldığında kullanıcıya şehir seçme menüsü ve bir "Get Weather" butonu sunulur.

2. **Şehir Seçme**

   Menüden istediğiniz şehri seçin. Varsayılan olarak Berlin ayarlanmıştır.

3. **Hava Durumu Alma**

   "Get Weather" butonuna tıklayarak seçtiğiniz şehrin hava durumu bilgilerini alabilirsiniz.

4. **Sonuçlar**

   Uygulama seçilen şehrin sıcaklık bilgisini ekranda gösterir.

## Gereksinimler

- Python 3.x
- `requests` kütüphanesi (`pip install requests` ile yüklenebilir)

## API Bilgileri

Bu uygulama, Meteomatics API'sini kullanarak hava durumu verilerini çeker. API erişimi için bir kullanıcı adı ve şifre gereklidir. Kod içerisinde bu bilgilerinizi belirtmeniz gerekmektedir.

## Hata Durumları

- Seçilen şehir listede bulunmuyorsa hata mesajı gösterilir.
- Hava durumu verileri başarıyla alınamazsa bir hata mesajı görüntülenir.

## Notlar

- Güvenlik amacıyla, API erişim bilgilerinizi kod içerisine hardcode olarak eklemek yerine, güvenli bir şekilde yönettiğinizden emin olun.

