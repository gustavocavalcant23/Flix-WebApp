import streamlit as st
import pandas as pd

from .services import ActorService

from st_aggrid import AgGrid


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    st.title('Lista de Atores')

    if actors:
        actors_df = pd.json_normalize(actors)
        actors_df = actors_df.drop(columns=['id', ])
        AgGrid(
            data=actors_df,
            reload_data=True,
            key='actors_grid',
            show_toolbar=True,
            show_download_button=True
        )
    else:
        st.warning('Nenhum ator cadastrado')

    st.divider()

    st.title('Cadastrar novo ator')
    name = st.text_input('Nome')
    nationality = st.selectbox(
        'Nacionalidade',
        options=[
            'Estados Unidos',
            'Brasil'
        ]
    )
    if st.button('Enviar'):
        actor_service.create_actor(
            name=name,
            nationality=nationality
        )
        st.rerun()
        st.success(f'Ator {name} cadastrado com sucesso!')
