<div align="center">

# 🛒 Django E-Commerce Website

**A product-selling website built with Python Django**

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

## 📖 Detailed Setup Guide (Visual Studio Code)

## Install Project




#### 1) Install the program: install Visual Studio Code for your operating system.

![1](https://user-images.githubusercontent.com/40443383/190001635-8ce64f63-5f6f-4929-8381-be46a4c0798d.png)

 
#### 2) Open the program and the project folder:
- After opening the program, click the "Open Folder" option

![2](https://user-images.githubusercontent.com/40443383/190001669-daf80dda-3e61-4b7c-b42e-f8eb690530e0.png)



- Find and open the project
 
![3](https://user-images.githubusercontent.com/40443383/190001717-8d00acc0-7c7a-40b8-8d9f-58d7aa5f3b2d.png)

- The project explorer then appears

 
![4](https://user-images.githubusercontent.com/40443383/190001727-4ee9be5b-7aa2-4e2a-ae90-f00d7197ed04.png)

![5](https://user-images.githubusercontent.com/40443383/190001792-26fae939-6ef4-4c91-af43-59e6a81f631a.png)

 
- It contains all the files and code of the project:
- `media` – folder holding the images used in the project
- `secondapp` / `secondproject` – the Django project code
- `static` – CSS and JS files
- `templates` – HTML files
- `db.sqlite3` – the database (registrations, logins, all products on the site and messages left on the site are stored here)
- `manage.py` – the file used to run the Django project


#### 3) Run the project:
- Open a terminal from this section to run the project.

![6](https://user-images.githubusercontent.com/40443383/190001865-de74bdc9-7593-4181-8dd3-f3543a1ab255.png)


- Type this command in the terminal that opens at the bottom and the project starts running.

 
![Picture7](https://user-images.githubusercontent.com/40443383/190001902-59afd02c-ef66-40d0-9911-91e4c8ef26e2.png)



#### 4) Open the site:

- Open your browser and go to `localhost:8000`.
 
![Picture8](https://user-images.githubusercontent.com/40443383/190001933-d56f35c7-db02-41e1-9867-d441adc86872.png)






## Site Features

#### 1) Home page:

- The site has the following menus: home, about, contact, all products, products, registration and profile. Messages left by members appear at the bottom. The site has a space theme, so images and data were adapted to it. Hovering over patterns, textures or structures changes their colour, and clicking them filters the products (for example, choosing patterns shows only products with patterns).

![Picture9](https://user-images.githubusercontent.com/40443383/190001972-602bab46-1008-4755-b2c8-57ca69a9fe2e.png)

#### 2) About
- The page that gives information about the site.

![Picture10](https://user-images.githubusercontent.com/40443383/190002185-92f55ca9-92fd-4497-8f27-201a22e907dd.png)

#### 3) Contact:
- A contact section where customers write comments about the site that are shown publicly in the feedback area. Submitted data is stored in the database and displayed in the feedback section. A Mars map was added to match the theme.
 
![Picture11](https://user-images.githubusercontent.com/40443383/190002225-86438438-d03e-4f0a-97ef-46f24e428c33.png)

 
#### 4) All products:
- All products and their prices are listed here; click a product to add it to the cart.

![Picture12](https://user-images.githubusercontent.com/40443383/190002248-f6b7d088-c337-45a3-b8d0-378d89ebddae.png)


#### 5) Cart and checkout:

- When products are added to the cart you can increase quantities, remove items, review them, empty the cart or cancel. When you complete the order you are redirected to PayPal to enter your payment details.

![Picture13](https://user-images.githubusercontent.com/40443383/190002287-03ac9663-e49a-4507-bf1c-24836a2e4eea.png)

#### 6) Registration:

- Enter your details to register on the site. Registration data is saved in the database and used at login. An error is shown if the username is already taken. You can register as a seller or a buyer; sellers can add products to the site from their profile.

![Picture14](https://user-images.githubusercontent.com/40443383/190002346-87c2af01-2eb8-473e-bd7a-02d5591d8d81.png)

 

#### 7) Login:

- Log in with the credentials used during registration.

 ![Picture15](https://user-images.githubusercontent.com/40443383/190002359-aadf87ad-1adf-475c-af9c-8ba8d980964f.png)



#### 8) Profile:
- The profile section shows information about your account and offers several other features.
 
![Picture16](https://user-images.githubusercontent.com/40443383/190002380-e87595f9-fff7-4488-a12c-0f84c0fb86b3.png)


## SQLite Database

#### 1) Inspecting the database
- Install a SQLite viewer and open `db.sqlite3` from the project folder.
 
![Picture17](https://user-images.githubusercontent.com/40443383/190002416-bdf9dab4-1f6b-4df5-bc7c-0c59b6dbdda0.png)

- New product pages shown on the home page can be added from here; all site data lives in this database.
 
![Picture18](https://user-images.githubusercontent.com/40443383/190002441-82f4d800-fda8-4efd-919b-23b27250ee65.png)


- All products are stored here; you can add new products or remove them from sale.
 
![Picture19](https://user-images.githubusercontent.com/40443383/190002459-04a36214-23f3-4011-9471-3c6e0762600a.png)

---

<div align="center">

Made by [Eren Solmaz](https://github.com/erensolmaz) · [LinkedIn](https://linkedin.com/in/noiren)

</div>
