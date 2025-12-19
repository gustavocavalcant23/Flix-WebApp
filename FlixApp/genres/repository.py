import requests
import streamlit as st

from login.service import logout


class GenreRepository:

    def __init__(self):
        self.__base_url = 'http://127.0.0.1:8000/api/v1/'
        self.__genres_url = f'{self.__base_url}genres/'
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

    def get_response(self, response):
        if response.status_code == 200 or 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status Code: {response.status_code}')

    def get_genres(self):
        response = requests.get(
            url=self.__genres_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status Code: {response.status_code}')

    def create_genre(self, genre):
        response = requests.post(
            url=self.__genres_url,
            headers=self.__headers,
            data=genre
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status Code: {response.status_code}')
