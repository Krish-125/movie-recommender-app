# 🎬 Movie Recommender Web App

A simple, interactive movie recommender system built using **Flask**, **Pandas**, and **Scikit-learn**. This app suggests similar movies based on your selection from a dropdown list.

## 🚀 Features

- 🔍 Searchable dropdown to select a movie
- 🎯 Recommends 5 similar movies using content-based filtering
- ⚡ Lightweight and fast Flask backend
- 🌐 Clean web interface with HTML/CSS

## 📷 Preview

<img width="1919" height="869" alt="Screenshot 2025-07-20 023013" src="https://github.com/user-attachments/assets/31d46011-efe5-4b31-845d-95cd1bf0ca94" />


## 🧠 How It Works

- The app loads a preprocessed movie dataset.
- When a user selects a movie, it finds the most similar movies using cosine similarity based on genres, cast, crew, and overview.
- It then displays the top 5 similar movie recommendations.

## 🛠️ Tech Stack

- Python 🐍
  - Flask
  - Pandas
  - Scikit-learn
  - NLTK
- Frontend 🌐
  - HTML5
  - CSS3
  - JavaScript (for dropdown)
 
## 📁 Project Structure

movie-recommender/
├── app.py
├── recommend.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── tmdb_5000_credits.csv
├── tmdb_5000_movies.csv
├── requirements.txt
└── README.md
