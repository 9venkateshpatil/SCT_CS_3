🔐 ForgePass – Password Strength Analyzer Web App

Live Website:
https://forgepass.onrender.com/

📌 Overview

ForgePass is a Flask-based web application that analyzes the strength of a password using multiple criteria including length, character diversity, and overall complexity. The tool evaluates passwords in real time and returns a score, strength label, and improvement suggestions.

The analysis is not cryptographic hashing or encryption — it is a structured evaluation technique meant for learning, security awareness, and improving password hygiene.

🎨 Features

Clean red and black cyber-themed UI

Checks for lowercase, uppercase, digits, special characters

Evaluates password length and complexity

Displays score (0–7) with visual strength badges

Provides improvement suggestions dynamically

Fully Flask-based, easy to extend with more rules

Beginner-friendly and deployment-ready

🧠 How It Works (Simple Explanation)

ForgePass evaluates a password based on five fundamental rules:

Length analysis

Has uppercase characters (A–Z)

Has lowercase characters (a–z)

Contains digits (0–9)

Contains special characters (@, #, $, %, etc.)

Each criteria adds to a total score, which determines the final strength:

Very Weak → Weak → Medium → Strong → Very Strong

Scoring example:

length_points = 0–3
has_upper = 0/1
has_lower = 0/1
has_digit = 0/1
has_special = 0/1


Maximum score = 7.

📁 Project Structure

SCT_CS_3/
│
├── app.py                 Flask backend
├── password_utils.py      Password strength evaluation logic
│
├── templates/
│   └── index.html         Red and black themed UI
│
├── static/
│   └── style.css          Complete frontend styling
│
└── requirements.txt       Dependencies for deployment


🚀 How to Run Locally

Create a virtual environment

python -m venv venv


Activate environment

Windows:

venv\Scripts\activate


Linux/Mac:

source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Run the server

python app.py


Open in browser

http://127.0.0.1:5000


🛠 Technologies Used

Python

Flask

HTML + CSS

Jinja2

Render (Deployment)

🔍 Password Strength Logic

Scores password on character diversity

Detects missing requirements

Generates clear improvement suggestions

Supports real-time UI-based evaluation

Reusable evaluation function in password_utils.py

Core functions inside password_utils.py:

check_password_strength(password)


👨‍💻 Developer

Venkatesh Patil
Python • Flask • Full-Stack • GitHub
Internship Project: ForgePass – Password Strength Analyzer Web App