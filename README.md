# 📚 Smart Library Management System

A beginner-friendly **Smart Library Web Application** built using **Python, Flask, and SQLite**.

This guide is written in a way that **even a complete beginner (no coding knowledge)** can run the project successfully 💻✨

---

# 🚀 Features

* 📖 Book management
* 👤 User handling
* 🔄 Issue / Return system
* 🗄️ SQLite database integration
* 🌐 Simple web interface using Flask

---

# 🧰 Prerequisites (Install First)

Before running the project, install these:

## ✅ 1. Install Python

### Windows:

1. Go to: https://www.python.org/downloads/
2. Download latest Python
3. IMPORTANT ⚠️: While installing, tick:
   ✔️ **"Add Python to PATH"**
4. Click Install

### Mac:

Open Terminal and run:

```bash
brew install python
```

---

## ✅ 2. Install Git

### Windows:

Download from: https://git-scm.com/downloads

### Mac:

```bash
brew install git
```

---

## ✅ 3. Install VS Code (Recommended)

Download: https://code.visualstudio.com/

---

# 📥 Download the Project

## 🔹 Option 1 (Easy - ZIP)

1. Go to your GitHub repository
2. Click **Code → Download ZIP**
3. Extract the ZIP file

---

## 🔹 Option 2 (Using Git)

Open terminal / command prompt:

```bash
git clone https://github.com/Devdeepakjha/smart_library.git
cd smart_library
```

---

# 📂 Open Project

1. Open **VS Code**
2. Click **File → Open Folder**
3. Select `smart_library` folder

---

# ⚙️ Setup Project (VERY IMPORTANT)

## 🔹 Step 1: Create Virtual Environment

### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 🔹 Step 2: Install Dependencies

```bash
pip install flask
```

---

# 🗄️ Database Setup

Your project already includes:

* `database.db`
* `schema.sql`

👉 If needed, run:

```bash
python db.py
```

---

# ▶️ Run the Project

```bash
python app.py
```

---

# 🌐 Open in Browser

After running, you will see something like:

```
Running on http://127.0.0.1:5000
```

👉 Open your browser and go to:

```
http://127.0.0.1:5000
```

🎉 Your Smart Library is now running!

---

# 📁 Project Structure

```
smart_library/
│
├── app.py          # Main Flask app
├── db.py           # Database connection
├── database.db     # SQLite database
├── schema.sql      # Database schema
│
├── routes/         # Backend routes
├── templates/      # HTML templates
├── static/         # CSS / JS files
├── utils/          # Helper functions
└── seed/           # Initial data
```

---

# ❗ Common Errors & Fixes

## ❌ Python not recognized

✔️ Reinstall Python and check "Add to PATH"

---

## ❌ ModuleNotFoundError

```bash
pip install flask
```

---

## ❌ Port already in use

```bash
python app.py --port 5001
```

---

## ❌ Virtual environment not activating

Make sure you are inside the project folder

---

# 💡 Tips

* Always activate `venv` before running the project
* Do not delete `database.db`
* Run all commands inside the project folder

---

# 👨‍💻 For Absolute Beginners (Quick Steps)

```bash
# 1. Clone project
git clone https://github.com/Devdeepakjha/smart_library.git

# 2. Go inside folder
cd smart_library

# 3. Create virtual environment
python -m venv venv

# 4. Activate virtual environment
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac

# 5. Install Flask
pip install flask

# 6. Run project
python app.py
```

Then open:

```
http://127.0.0.1:5000
```

---

# 🙌 Author

**Deepak Jha**

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
