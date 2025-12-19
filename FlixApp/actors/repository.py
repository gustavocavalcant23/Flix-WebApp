import requests
import streamlit as st

from login.service import logout


class ActorsRepository:

    def __init__(self):
        self.__base_url = 'http://localhost:8000/api/v1/'
        self.__actors_url = f'{self.__base_url}actors/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_headers(self):
        token = st.session_state.get('token')
        if not token:
            raise Exception('Token não encontrado')
        return {
            'Authorization': f'Bearer {token}'
        }

    def get_actors(self):
        response = requests.get(
            url=self.__actors_url,
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')

    def create_actor(self, actor):
        response = requests.post(
            url=self.__actors_url,
            headers=self.__headers,
            data=actor,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')
