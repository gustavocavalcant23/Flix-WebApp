import streamlit as st
import pandas as pd

from .service import MovieService
from actors.services import ActorService
from genres.service import GenreService

from st_aggrid import AgGrid
from datetime import datetime


def show_movies():
    movie_service = MovieService()

    movies = movie_service.get_movies()

    st.title('Lista de Filmes')

    if movies:
        movies_df = pd.json_normalize(data=movies)
        movies_df = movies_df.drop(columns=['id', 'actors', 'genre.id', 'synopsis'])
        # movies_df = movies_df.

        AgGrid(
            data=movies_df,
            reload_data=True,
            key='movies_grid',
            show_download_button=True,
            show_toolbar=True
        )
    else:
        st.warning('Nenhum Filme encontrado...')

    st.divider()

    st.title('Cadastrar novo filme')
    name = st.text_input('Título')

    release_date = st.number_input(
        'Ano de Lançamento',
        min_value=1800,
        max_value=datetime.today().year,
        value=datetime.today().year,
    )

    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {
        genre['name']: genre['id'] for genre in genres
    }

    selected_genre_name = st.selectbox(
        'Gênero',
        options=list(genre_names.keys())
    )

    actors_service = ActorService()
    actors = actors_service.get_actors()
    actors_name = {
        actor['name']: actor['id'] for actor in actors
    }

    selected_actor_name = st.multiselect(
        'Atores/Atrizes',
        options=list(actors_name.keys())
    )

    selected_actors_id = [actors_name[name] for name in selected_actor_name]

    synopsis = st.text_area(
        'Sinopse'
    )

    if st.button('Enviar'):
        new_movie = movie_service.create_movie(
            name=name,
            genre=genre_names[selected_genre_name],
            release_date=release_date,
            actors=selected_actors_id,
            synopsis=synopsis
        )
        if new_movie:
            st.rerun()
            st.success(f'Filme {name} cadastrado com sucesso!')
        else:
            st.error('Erro ao cadastrar filme...')
