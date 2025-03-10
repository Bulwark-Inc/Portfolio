# 🧑‍💻 Personal Portfolio Website - Django + Tailwind

This is my **personal portfolio website**, built with **Django**, styled using **Tailwind CSS**, and deployed on **PythonAnywhere**.  
It showcases my projects, services, and includes a contact form that sends emails through Gmail SMTP.

---

## 🚀 Tech Stack

- **Frontend**: HTML, Tailwind CSS (with some custom CSS)
- **Backend**: Django
- **Database**: SQLite (for now)
- **Email Service**: Gmail SMTP
- **Deployment**: PythonAnywhere
- **Version Control**: Git + GitHub

---

## 📂 Project Structure (Simplified)

portfolio/ # Django project root ├── portfolio/ # Django project settings ├── home/ # Main app (views, URLs, templates) │ ├── templates/home/ # HTML templates │ ├── static/home/ # CSS, JS, Images │ ├── views.py # Views for home, about, services, etc. │ ├── urls.py # App-level URL routing │ ├── forms.py # Contact form logic ├── theme/ # Tailwind CSS project (Node/NPM) │ ├── src/input.css # Tailwind CSS input file │ ├── package.json # NPM packages (tailwind, autoprefixer) │ ├── tailwind.config.js │ └── postcss.config.js ├── db.sqlite3 # SQLite database └── manage.py # Django management script


---

## 🌟 Key Features

- ✅ Hero Section (Name, tagline, profile pic, social links)
- ✅ About Me (Bio, tech stack)
- ✅ Projects (Dynamic, stored in the database)
- ✅ Services (What I offer)
- ✅ Contact Form (Sends emails via Gmail SMTP)
- ✅ Footer (Social links: GitHub, LinkedIn, Twitter)
- ✅ Dark Mode + Animations (AOS and Tailwind hover effects)

---

## ⚙️ Setup Instructions (Local Development)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```
Create Virtual Environment & Install Django
```bash
python -m venv venv
source venv/bin/activate
pip install django
```
Install Tailwind CSS Dependencies (inside theme/)
```bash
cd theme
npm install
npm run build  # Builds the production CSS
cd ..
```

Run Django Server
```bash
python manage.py migrate
python manage.py runserver
```

## Contact
For inquiries or freelance services, contact me through the Contact Form or directly via:

- **GitHub**: https://github.com/Bulwark-Inc
- **LinkedIn**: https://linkedin.com/in/shiloh-egwuatu
- **Twitter/X**: @ShilohE_AI

---

## ✅ What To Edit
- Replace **`yourusername`**, **`your-repo`**, **`YourGitHub`**, etc.
- Optional: Add screenshots or a live link if you deploy!
