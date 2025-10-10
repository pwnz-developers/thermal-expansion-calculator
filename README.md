# 🧮 Thermal Expansion Calculator

A high-precision web application built with [Django](https://www.djangoproject.com/) that calculates:

- Linear expansion (ΔL)  
- Area expansion (ΔS)  
- Volume expansion (ΔV)  
- Thermal stress (σ)  

The project leverages Python’s `Decimal` module to ensure engineering-grade calculation accuracy.

---

## 📦 Features

- ✅ Accurate thermal expansion calculations  
- 🖥️ Clean and responsive user interface  
- 🔐 Secure form handling with CSRF protection  
- 🌐 Easy tunneling support with tools like `jprq` or `ngrok`  

---

## 🧰 Tech Stack

- **Backend:** Django 5  
- **Frontend:** HTML + CSS (Django templates)  
- **Precision:** Python `decimal` module  
- **Runtime:** Python 3.13+  

---

## ⚙️ Installation & Run

Follow these steps to set up the project on your local machine 👇

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/thermal-expansion-calculator.git
cd thermal-expansion-calculator
```

### 2. Create and activate a virtual environment
### For macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### For Windows
```bash
.venv\Scripts\activate      
```
### 3. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the development server
```bash
python manage.py runserver
```

### Go to [localhost](http://127.0.0.1:8000/) in your browser to view the app.
