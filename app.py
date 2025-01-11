from tkinter.font import names

import streamlit as st
import pickle
import pandas as pd

# Define recommendation function
def recommend(movie):
    movie_index = movies[movies['names'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for movie in movie_list:
        recommended_movies.append(movies.iloc[movie[0]]['names'])
    return recommended_movies

# Load pre-saved data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Search with the name of a movie',
    movies['names'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.write("Here are some recommendations:")
    for i in recommendations:
        st.write(i)
