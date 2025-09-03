# 🚦 MITM Flask App

This is a simple Flask web application for monitoring network activity and detecting potential Man-in-the-Middle (MITM) attacks. 🕵️‍♂️

## ✨ Features
- 🖥️ Web interface for starting network monitoring
- 🧩 Modular detection logic (see `utils/detector.py`)

## 🗂️ Project Structure
```
mitm_flask_app/
├── app.py                # Main Flask application
├── templates/
│   └── index.html        # Web UI
└── utils/
    ├── __init__.py       # Makes utils a package
    └── detector.py       # Detection logic
```

## 🚀 Getting Started
1. Create and activate a virtual environment (optional but recommended):
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
2. Install dependencies:
   ```powershell
   pip install flask
   ```
3. Run the app:
   ```powershell
   python app.py
   ```
4. Open your browser and go to `http://127.0.0.1:5000/` 🌐

## 📝 Notes
- ⚠️ The detection logic in `utils/detector.py` is currently a placeholder. Replace it with real packet capture and ML logic as needed.
