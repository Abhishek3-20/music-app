🎵 Django Music Streaming App

A sleek and responsive music streaming web application built using **Django** and **custom HTML/CSS templates**. Users can browse music, select artists, play songs, and save playlists — all within a beautiful UI with responsive background images.

## 🚀 Live Preview
🔗 [View Live on GitHub Pages](https://abhishek3-20.github.io/)

> **Note**: The live link above hosts the frontend. For full functionality, clone and run locally or deploy the backend.

---

## 📸 Screenshots

![Landing Page](screenshots/landing.png)
![Music Player](screenshots/player.png)
![Playlist Page](screenshots/playlist.png)

---

## ✨ Features

- 🎧 Artist selection and personalized player
- 📁 Save and manage playlists
- 🎨 Responsive UI with dynamic background images
- 🔐 Custom login & signup pages
- 📱 Mobile-friendly design

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Custom templates)
- **Database**: SQLite (default), can upgrade to PostgreSQL
- **Deployment**: (optional) Vercel / PythonAnywhere / Render

---

## 📂 Project Structure

music_site/
├── music/ # Django app for music features
│ ├── templates/music/ # Custom HTML templates
│ └── static/music/ # Static files (CSS, images)
├── music_site/ # Django project settings
├── db.sqlite3 # Default database
├── manage.py
└── README.md

yaml
Copy
Edit

---

## ⚙️ Local Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/abhishek3-20/music_site.git
   cd music_site
Create virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run migrations

bash
Copy
Edit
python manage.py migrate
Run the server

bash
Copy
Edit
python manage.py runserver
Visit: http://127.0.0.1:8000/

🚀 Deployment Options
Vercel (with vercel-python or vercel-wsgi)

Render.com

PythonAnywhere

Railway.app

🙌 Credits
Developed by Abhishek Unni

📜 License
This project is open-source and available under the MIT License.
