# Futbolcu Performansı Bulanık Mantık Kontrolcüsü

Merhaba! Ben İbrahim, 23 yaşındayım ve 7 yaşından beri futbol ile aktif olarak ilgileniyorum. Lisanslı bir futbolcu olarak kariyerimde 4 Süper Amatör Lig şampiyonluğu kazandım ve Doğu Anadolu ile Güneydoğu Anadolu bölgelerinde gol krallıkları elde ettim. Futbola olan tutkum ve antreman deneyimlerim sayesinde, futbolcuların performansını verilerle ve bilimsel yöntemlerle değerlendirebilecek bir uygulama geliştirmek istedim.

Bu proje, futbolcu performansını bulanık mantık kullanarak değerlendiren ve kondisyon önerilerinde bulunan bir Python uygulamasıdır. Tkinter tabanlı kullanıcı dostu arayüzü ile hem kolay kullanım hem de esnek analiz imkanı sağlar.

---

## Özellikler

- 5 adet girdi kabul eder:  
  - Pas İsabet Oranı (%)  
  - Top Kapma Sayısı  
  - Şut İsabet Oranı (%)  
  - Koşu Mesafesi (km)  
  - Faul Sayısı  
- 2 çıktı üretir:  
  - Genel Performans (Düşük, Orta, Yüksek)  
  - Kondisyon Önerisi (Dinlenmeli, Normal, Ekstra Antrenman)  
- Bulanık mantık kuralları ile gerçekçi ve esnek değerlendirme  
- Tkinter arayüzü ile kolay ve anlaşılır kullanım  
- Matplotlib ile grafiksel sonuç gösterimi  

---

## Kurulum

1. Python 3 yüklü olmalıdır.  
2. Gerekli kütüphaneleri yükleyin:


pip install numpy scikit-fuzzy matplotlib


Teknik Detaylar
5 giriş ve 2 çıkış değişkenli bulanık mantık sistemi tasarlandı.

Her değişken için uygun üyelik fonksiyonları belirlendi.

Kurallar futbolcunun sahadaki gerçek performansına uygun şekilde kurgulandı.

scikit-fuzzy kütüphanesi kullanılarak bulanık mantık hesaplamaları yapıldı.

Tkinter arayüzü ile kolay veri giriş ve sonuç görüntüleme sağlandı.

Matplotlib ile sonuçların grafiksel gösterimi yapıldı.


Kullanılan Teknolojiler
Python 3

Tkinter

NumPy

scikit-fuzzy

Matplotlib



