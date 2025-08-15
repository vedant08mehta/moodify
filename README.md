# 🎵 Moodify – Your Mood. Your Music. 🎶
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


*"Let your face set the playlist."*

Moodify is an AI-powered web app that detects your **facial emotion** in real time and recommends a personalized playlist based on your mood. Whether you’re feeling happy, sad, angry, or relaxed — Moodify has the perfect soundtrack for you.

---

## ✨ Features

- **🎭 Emotion Detection:** Uses **DeepFace** and **TensorFlow/Keras** to identify your mood from a live camera feed or uploaded image.  
- **🎵 Mood-Based Music Suggestions:** Automatically recommends songs based on detected emotions.  
- **🌐 Web-Based Interface:** Powered by **Streamlit** for quick, interactive, and responsive UI.  
- **📷 Easy Input:** Upload an image or use your webcam to detect mood instantly.  
- **⚡ Fast & Lightweight:** Minimal setup required, works on most modern systems.  

---

## 🛠️ Tech Stack

- **Python 3.x**  
- **Streamlit** – Web app framework  
- **DeepFace** – Facial emotion recognition  
- **TensorFlow + Keras** – Machine learning models  
- **NumPy** – Data handling  
- **Pillow** – Image processing  
- **Protobuf** – TensorFlow compatibility  

---

## 📂 Project Structure
```bash
moodify/
│
├── app.py             # Main Streamlit app
├── requirements.txt   # All dependencies with exact versions
├── README.md          # This file 
```
--- 

## 🚀 How to Run Locally

1️⃣ Clone the Repository  

```bash git clone https://github.com/vedant08mehta/moodify.git ```
```bash cd moodify ```

2️⃣ Install Dependencies
```bash pip install -r requirements.txt ```

3️⃣ Run the App
```bash streamlit run app.py ```

Your default browser will open at:
➡️ http://localhost:8501

---

## 📦 Requirements

All dependencies are version-locked for stability:

```bash streamlit==1.22.0
tensorflow==2.10.0
keras==2.10.0
deepface==0.0.95
numpy==1.26.4
protobuf==3.19.6
Pillow==11.3.0 
```

---

## 💡 Future Enhancements

🎶 Integration with Spotify/YouTube APIs for live playlist streaming.

📊 Mood tracking over time.

📱 Mobile-friendly UI.

---

## 📜 License

This project is open-source under the MIT License.
