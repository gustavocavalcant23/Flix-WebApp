import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

from .service import GenreService


def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    st.title('Lista de Gêneros')

    if genres:
        genres_df = pd.json_normalize(genres)
        genres_df = genres_df.drop(columns=['id', ])
        AgGrid(
            data=genres_df,
            reload_data=True,
            key='genres_grid'
        )
    else:
        st.warning('Nenhum gênero cadastrado...')

    st.divider()

    st.title('Cadastrar novo gênero')
    name = st.text_input('Nome do gênero')
    if st.button('Enviar'):
        genre_service.create_genre(name=name)
        st.rerun()
