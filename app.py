from flask import Flask, request, render_template
from recommend import recommend, new_df

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    selected_movie = None
    movie_titles = new_df['title'].tolist()  # Extract movie titles from new_df
    
    if request.method == 'POST':
        selected_movie = request.form.get('movie')
        if selected_movie:
            recommendations = recommend(selected_movie)

    return render_template(
        'index.html',
        movies=movie_titles,
        recommendations=recommendations,
        selected_movie=selected_movie
    )

if __name__ == "__main__":
    app.run(debug=True)