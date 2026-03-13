# MediPredict – AI Powered Health Risk Predictor

## 🩺 Project Overview

**MediPredict** is an AI-powered healthcare prototype designed to assist in early disease prediction using basic symptom inputs. The system uses a machine learning model to analyze symptoms such as fever, cough, headache, and fatigue to predict potential diseases.

The goal of this project is to demonstrate how **Artificial Intelligence can improve healthcare accessibility, early diagnosis, and preventive care**.

This project was developed for **Codecure – SPIRIT 2026**, the annual **Techno-Pharma Conference of IIT (BHU) Varanasi**.

---

# 🚀 Problem Statement

Many individuals ignore early symptoms or lack immediate medical guidance. This delay can lead to late diagnosis and complications.

MediPredict aims to:

* Provide quick preliminary health insights
* Promote preventive healthcare
* Encourage early medical consultation

---

# 💡 Solution

MediPredict uses a **machine learning model trained on symptom-based data** to predict potential diseases. The system provides an easy-to-use web interface where users can enter symptoms and receive an AI-based prediction.

The project demonstrates how **AI-driven healthcare tools can assist patients and healthcare systems in making faster decisions.**

---

# ✨ Key Features

* AI-based disease prediction
* Simple symptom input interface
* Lightweight web application
* Fast real-time prediction
* Scalable architecture for future healthcare datasets
* Iridescent healthcare-themed UI design

---

# 🧠 Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Pandas
* Pickle

### Backend

* Flask

### Frontend

* HTML
* CSS
* Iridescent gradient UI design

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

# 🏗 Project Architecture

User Input (Symptoms)
⬇
Flask Web Server
⬇
Machine Learning Model
⬇
Prediction Generated
⬇
Result Displayed to User

---

# 📁 Project Folder Structure

```
MediPredict
│
├── app.py
├── model.py
│
├── dataset
│     disease_dataset.csv
│
├── model
│     disease_model.pkl
│
├── templates
│     index.html
│     result.html
│
└── static
      style.css
```

---

# ⚙️ Installation & Setup Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/MediPredict.git
cd MediPredict
```

---

### Step 2: Install Dependencies

```bash
pip install flask pandas scikit-learn
```

---

### Step 3: Train the Model

Run the following command:

```bash
python model.py
```

This will generate the trained model file:

```
model/disease_model.pkl
```

---

### Step 4: Run the Application

```bash
python app.py
```

---

### Step 5: Open the Web Application

Open the browser and visit:

```
http://127.0.0.1:5000
```

---

# 🔬 Machine Learning Workflow

1. Load symptom dataset
2. Preprocess the data
3. Train Decision Tree classifier
4. Save trained model using Pickle
5. Load model in Flask server
6. Predict disease based on user symptoms

---

# 📊 Input Parameters

The model uses the following symptoms:

| Symptom  | Input  |
| -------- | ------ |
| Fever    | 0 or 1 |
| Cough    | 0 or 1 |
| Headache | 0 or 1 |
| Fatigue  | 0 or 1 |

Where:

* **0 = No symptom**
* **1 = Symptom present**

---

# 🎯 Future Improvements

Future versions of MediPredict may include:

* AI chatbot for symptom discussion
* Integration with wearable health devices
* Personalized health recommendations
* Real medical datasets
* Voice-based symptom input
* Mobile application version

---

# 👥 Team Collaboration

All team members contributed to the following areas:

* Machine Learning Model Development
* Web Application Development
* UI/UX Design
* Testing & Debugging
* Documentation

---

# ⚠️ Disclaimer

This project is a **prototype for educational and research purposes only**. It is not intended to replace professional medical diagnosis or treatment.

---

# 🏁 Conclusion

MediPredict demonstrates how AI-driven healthcare tools can assist in improving healthcare accessibility, early diagnosis, and preventive care. The project highlights the potential of integrating **Artificial Intelligence with healthcare systems to create impactful digital health solutions.**

---

# 📜 License

This project is released for academic and demonstration purposes.
