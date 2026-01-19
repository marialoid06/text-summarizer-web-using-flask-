## 📝 Text Summarizer Web App (ML Project)

A simple extractive text summarization web application built using Python, NLTK, and Flask.
This project summarizes long text into a concise version by selecting the most important sentences based on word frequency.

## 📌 Project Overview

This Text Summarizer uses Natural Language Processing (NLP) techniques to:

Tokenize text into sentences and words

Remove stopwords

Calculate word frequencies

Score sentences based on important words

Generate a summary with top-ranked sentences

It is a rule-based ML/NLP model (no deep learning), ideal for beginners, mini projects, and internship portfolios.

## Model Type

Type: Extractive Text Summarization

Algorithm: Frequency-based scoring

Libraries Used: NLTK

Framework: Flask (Web App)

## 🗂️ Project Structure

TEXT_SUMMARIZER/
│
├── app.py
├── README.md
│
└── templates/
    └── index.html  (HTML with embedded CSS)

## ⚙️ Technologies Used

Python

Flask

NLTK

HTML (with embedded CSS)

## 📦 Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/your-username/text-summarizer.git
cd text-summarizer

2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py

5️⃣ Open in Browser
http://127.0.0.1:5000/

## 📄 requirements.txt
flask
nltk

## How It Works

User enters text in the web form

Text is tokenized into sentences and words

Stopwords are removed

Word frequencies are calculated and normalized

Each sentence is scored

Top sentences are selected as the summary

## Example Use Case

Input:
A long article or paragraph

Output:
A short, meaningful summary with key sentences
