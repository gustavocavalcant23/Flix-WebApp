import streamlit as st

from .repository import MovieRepository


class MovieService:

    def __init__(self):
        self.movie_repository = MovieRepository()

    def get_movies(self):
        if 'movies' in st.session_state:
            return st.session_state.movies
        movies = self.movie_repository.get_movies()
        st.session_state.movies = movies
        return movies

    def get_movies_name(self):
        movies = self.movie_repository.get_movies()
        movies_list = list()

        for movie in movies:
            movies_list.append(
                movie.get('name')
            )
        return movies_list

    def create_movie(self, name, genre, release_date, actors, synopsis):
        movie = dict(
            name=name,
            genre=genre,
            release_date=int(release_date),
            actors=actors,
            synopsis=synopsis
        )
        new_movie = self.movie_repository.create_movie(movie)
        if 'movies' in st.session_state:
            del st.session_state.movies
            self.get_movies()
        return new_movie

    def get_movie_stats(self):
        if 'movie_stats' in st.session_state:
            return st.session_state.movie_stats
        movie_stats = self.movie_repository.get_movie_stats()
        st.session_state.movie_stats = movie_stats
        return movie_stats
