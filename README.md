🎵 Django Music Streaming App

A sleek and responsive music streaming web application built using **Django** and **custom HTML/CSS templates**. Users can browse music, select artists, play songs, and save playlists — all within a beautiful UI with responsive background images.

## 🚀 Live Preview
🔗 [View Live on GitHub Pages](https://abhishek3-20.github.io/)

> **Note**: The live link above hosts the frontend. For full functionality, clone and run locally or deploy the backend.

---

## 📸 Screenshots

![Landing Page]
<img width="1338" height="581" alt="Screenshot (12)" src="https://github.com/user-attachments/assets/028f22ca-1446-43d0-9613-3b945dba23cf" />

![login page]
<img width="1351" height="575" alt="Screenshot (11)" src="https://github.com/user-attachments/assets/0970acc9-793a-4e6e-9420-eb335bbd3eae" />

![artist Page]
<img width="1366" height="638" alt="Screenshot (14)" src="https://github.com/user-attachments/assets/29b3b29f-8e2b-45fb-8cd9-9a7ffb4934cf" />


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




## ⚙️ Local Setup

1. **Clone the repo**
2. 
   git clone https://github.com/abhishek3-20/music_site.git

    cd music_site
    Create virtual environment


    python -m venv venv
    source venv/bin/activate
    # Windows: venv\Scripts\activate.bat

Install dependencies


pip install -r requirements.txt
Run migrations


python manage.py migrate

Run the server

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








# requirements

Django>=4.2,<5.0
gunicorn>=21.2.0
whitenoise>=6.6.0
dj-database-url>=2.1.0
python-dotenv>=1.0.1

# Optional (if using Vercel or WSGI-based deployment)
vercel-wsgi>=0.5.6

# If you're using Pillow for image handling (optional)
Pillow>=10.2.0

