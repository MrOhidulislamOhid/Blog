# Django REST Blog API

This is a Django REST Framework based Blog API project with user profiles, posts, categories, and comments system.

---
# ER Diagram 
- https://drawsql.app/teams/me-1934/diagrams/blog

---

## 🚀 Features

- User Profile Management
- Post Creation (Draft & Published)
- Category System
- Comment System (Pending & Approved)
- Image Upload (Profile & Posts)

---

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (default database)

---

## ⚙️ Installation

```bash
git clone <your-repo-url>
cd your-project

python -m venv venv
# activate venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver