<div align="center">

# 🛒 Django E-Commerce Website

**A product-selling website built with Python Django (Django ile Python ürün satış sitesi)**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

</div>

---

## ✨ Features

- User registration, login and profile
- Product catalogue with images and prices
- Shopping cart and orders
- Contact form
- Admin panel for products & categories
- SQLite database

## 🚀 Getting Started

```bash
git clone https://github.com/erensolmaz/Django-Project.git
cd Django-Project
pip install django pillow
python manage.py migrate
python manage.py runserver
```
Open `http://127.0.0.1:8000/`. For the admin panel run `python manage.py createsuperuser`.

## 🗄️ Data Models

`Category` · `add_product` · `cart` · `order` · `register_table` (user profile) · `Contact_Us` · `Student`

## 📖 Detailed Setup Guide (Turkish, Visual Studio Code)

## Install Project




#### 1)	Program kurulumu: Visual studio programını işletim sistemimize uygun kuruyoruz.

![1](https://user-images.githubusercontent.com/40443383/190001635-8ce64f63-5f6f-4929-8381-be46a4c0798d.png)

 
#### 2)	Programı Açma ve Klasörü açma:
- Programı açtıktan sonra klasörü aç seçeğine basıyoruz

![2](https://user-images.githubusercontent.com/40443383/190001669-daf80dda-3e61-4b7c-b42e-f8eb690530e0.png)



- Projemizi bulup açıyoruz
 
![3](https://user-images.githubusercontent.com/40443383/190001717-8d00acc0-7c7a-40b8-8d9f-58d7aa5f3b2d.png)

- Daha sonra önümüze kütüphane geliyor

 
![4](https://user-images.githubusercontent.com/40443383/190001727-4ee9be5b-7aa2-4e2a-ae90-f00d7197ed04.png)

![5](https://user-images.githubusercontent.com/40443383/190001792-26fae939-6ef4-4c91-af43-59e6a81f631a.png)

 
- Bu kütüphanede projemizin tüm dosyalarını, kodlarını barındıyıor.
- Media>projede bulunan resimleri barındıran klasör
- Secondapp/secondproject>django projemizin kodları
- Static>css ve js kodlarımız
- Template>html kodları
- Db.sqlite3>database (Projede bulunan kayıt, giriş işlemleri,sitede bulunan ve ileride ekleyeceğimiz tüm ürünler, siteye bırakılan mesajlar burada depolanıyor.)
Manage.py> django projemizi çalıştıracağımız dosya


#### 3)	Projeyi çalıştırma:
- Projemizi çalıştırmak için cmd açıyoruz bu bölümden.

![6](https://user-images.githubusercontent.com/40443383/190001865-de74bdc9-7593-4181-8dd3-f3543a1ab255.png)


- Altta açılan cmd’ye bu kodu yazıyoruz ve projemiz çalışıyor.

 
![Picture7](https://user-images.githubusercontent.com/40443383/190001902-59afd02c-ef66-40d0-9911-91e4c8ef26e2.png)



#### 4)	Siteye giriş:

- İnternet sayfasını açıp, localhost:8000 yazıp siteye giriş yapabiliriz.
 
![Picture8](https://user-images.githubusercontent.com/40443383/190001933-d56f35c7-db02-41e1-9867-d441adc86872.png)






## Sitenin özellikleri:

#### 1)	Anasayfa:

- Sitede gözüktüğü üzere; anasayfa, hakkında, iletişim, tüm ürünler, ürünler, kayıt olma ve profil menüleri mevcuttur. Siteye üyelerin bıraktığı mesajlar alt kısımda gözüküyor. Sitenin teması doku vs olduğundan dolayı uzay vibe’ı veriyordu, uzayı yansıtmasını istediğim için resimleri verileri genelde uzay temasına uyarlamaya çalıştım. Mouse ile desenler, dokular veya yapıların üzerine geldiğimizde renk geçişi oluyor ve bunlara tıkladığımızda, filtreleme oluyor yani desenleri seçersek sadece desenlerin bulunduğu ürünler filtreleniyor.

![Picture9](https://user-images.githubusercontent.com/40443383/190001972-602bab46-1008-4755-b2c8-57ca69a9fe2e.png)

#### 2)	Hakkında
- Sitenin hakkında bilgi verilen sayfa.

![Picture10](https://user-images.githubusercontent.com/40443383/190002185-92f55ca9-92fd-4497-8f27-201a22e907dd.png)

#### 3)	İletişim:
- Sitendeki müşterilerin açık alanda paylaşılmak üzere (geri bildirimlerde gozukuyor) site hakkında yaptığı yorumları yazmasını sağlayan iletişim bölümü. Burda girilen veriler database’te depolanıyor ve geri bildirim bölümüne yazılıyor. Ayrıca temaya uyumlu olması için Mars map’i koydum.
 
![Picture11](https://user-images.githubusercontent.com/40443383/190002225-86438438-d03e-4f0a-97ef-46f24e428c33.png)

 
#### 4)	Tüm ürünler:
- Tüm ürünlerimiz ve fiyatları bu bölümde yazmaktadır, tıklayarak sepete ekleyebiliriz.

![Picture12](https://user-images.githubusercontent.com/40443383/190002248-f6b7d088-c337-45a3-b8d0-378d89ebddae.png)


#### 5)	Sepete ekleme ve ürün alma:

- Ürünleri sepete eklediğimizde bu bölüm geliyor miktarını arttırabiliyoruz, ürünleri çıkarabiliyoruz, inceleyebiliyoruz, sepeti boşaltabiliyoruz veya iptal edebiliyoruz. Ürünleri almak istersek tamamladığımızda bizi paypal siteye bilgilerimizi almaya yönlendiriyor.

![Picture13](https://user-images.githubusercontent.com/40443383/190002287-03ac9663-e49a-4507-bf1c-24836a2e4eea.png)

#### 6)	Kayıt olma:

- Bu bölümden bilgilerimizi girip siteye kayıt olabiliyoruz. Kayıt olduğumuzda verilerimiz database’e yedekleniyor ve giriş yapacağımız zaman verileri ordan alabiliyoruz. Eğer kayıt olurken aynı kullanıcı adı kayıtlı ise hata veriyor. Kayıt olurken satıcı veya alıcı olduğumuzu seçebiliyoruz eğer satıcı seçeneğini seçersek profilden siteye ürün ekleyebiliyoruz.

![Picture14](https://user-images.githubusercontent.com/40443383/190002346-87c2af01-2eb8-473e-bd7a-02d5591d8d81.png)

 

#### 7)	Giriş yapma:

- Kayıt olduğumuz bilgileri girip giriş yapıyoruz.

 ![Picture15](https://user-images.githubusercontent.com/40443383/190002359-aadf87ad-1adf-475c-af9c-8ba8d980964f.png)



#### 8)	Profil bölümü:
- Profil bölümünde profilimiz hakkında bilgileri öğrenebiliyoruz ve bir çok farklı özellik mevcut.
 
![Picture16](https://user-images.githubusercontent.com/40443383/190002380-e87595f9-fff7-4488-a12c-0f84c0fb86b3.png)


## SqLite database:

#### 1)	Database inceleme
- Sqlite database’i kurup klasörümüzden db’i açıyoruz
 
![Picture17](https://user-images.githubusercontent.com/40443383/190002416-bdf9dab4-1f6b-4df5-bc7c-0c59b6dbdda0.png)

- Anasayfada mevcut olduğumuz ürün sayfalarını buradan yenilerini ekleyebir ve sitemizi geliştirebiliriz. Tüm verilerimiz burada mevcut.
 
![Picture18](https://user-images.githubusercontent.com/40443383/190002441-82f4d800-fda8-4efd-919b-23b27250ee65.png)


- Ürünlerimizin tamamı burada mevcut buradan yeni ürünleri ekleyebilir ve satıştan kaldırabiliriz.
 
![Picture19](https://user-images.githubusercontent.com/40443383/190002459-04a36214-23f3-4011-9471-3c6e0762600a.png)

---

<div align="center">

Made by [Eren Solmaz](https://github.com/erensolmaz) · [LinkedIn](https://linkedin.com/in/noiren)

</div>
