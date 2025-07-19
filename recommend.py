import numpy as np
import pandas as pd
import ast

movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

movies = movies.merge(credits, on = 'title')
movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

movies.isnull().sum()
movies.dropna(inplace=True)
movies.duplicated().sum()

def convert(obj): # There will be error since the genre value is string
    l=[]
    for i in ast.literal_eval(obj):  # Therefore we took ast.literal_eval()
        l.append(i['name'])
    return l

movies['genres'] = movies['genres'].apply(convert) #We got list of genres of every movie
movies['keywords'] = movies['keywords'].apply(convert)

def convert3(obj): 
    l=[]
    c=0
    for i in ast.literal_eval(obj):  
        if c!=3:
            c+=1
            l.append(i['name'])
        else:
            break
    return l

movies['cast'] = movies['cast'].apply(convert3)

def fetch_director(obj): # There will be error since the genre value is string
    l=[]
    for i in ast.literal_eval(obj):  # Therefore we took ast.literal_eval()
        if i['job']=='Director':
            l.append(i['name'])
            break
    return l

movies['crew'] = movies['crew'].apply(fetch_director)

movies['overview'] = movies['overview'].apply(lambda x:x.split())

movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])

movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

new_df = movies[['movie_id','title','tags']]

new_df['tags'] = new_df['tags'].apply(lambda x:" ".join(x))
new_df['tags'] = new_df['tags'].apply(lambda x:x.lower())

import nltk
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def stem(text):
    y=[]
    
    for i in text.split():
        y.append(ps.stem(i))
        
    return " ".join(y)

new_df['tags'] = new_df['tags'].apply(stem)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')

vectors = cv.fit_transform(new_df['tags']).toarray()

from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vectors)

def recommend(movie):
    try:
        movie_index = new_df[new_df['title'] == movie].index[0]
    except IndexError:
        return ["Movie not found"]
    
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(new_df.iloc[i[0]].title)
    
    return recommended_movies

#recommend('Avatar')  # Example usage
# Expose the processed DataFrame
new_df = new_df
