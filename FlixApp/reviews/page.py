import streamlit as st
import pandas as pd

from .service import ReviewService
from movies.service import MovieService
from st_aggrid import AgGrid


def show_reviews():
    reviews_service = ReviewService()
    movies_service = MovieService()
    reviews = reviews_service.get_review()
    movies = movies_service.get_movies()

    movies_names = {
        movie['name']: movie['id'] for movie in movies
    }

    st.title('Lista de Reviews')

    if reviews:
        reviews_df = pd.json_normalize(data=reviews)
        reviews_df = reviews_df.drop(columns=['id',])

        AgGrid(
            data=reviews_df,
            reload_data=True,
            key='reviews_grid'
        )
    else:
        st.warning('Nenhuma review cadastrada...')

    st.divider()

    st.title('Cadastrar Review')

    selected_movie_name = st.selectbox(
        label='Filme',
        options=list(movies_names.keys()),
    )

    stars = st.slider(
        label='Avalie o filme',
        min_value=0,
        max_value=5,
        value=5
    )

    comment = st.text_area("Comentários", height=2)

    if st.button('Enviar'):
        reviews_service.create_review(
            movie=movies_names[selected_movie_name],
            stars=stars,
            comment=comment
        )
        st.rerun()
        st.success('Review cadastrada com sucesso!')
