import streamlit as st

from genres.page import show_genres
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews
from login.page import show_login
from home.page import show_home


def main():
    if 'token' not in st.session_state:
        show_login()

    else:
        MENU = {
            "🏠 Início": "home",
            "🎭 Gêneros": "genres",
            "🎬 Filmes": "movies",
            "👥 Atores": "actors",
            "⭐ Reviews": "reviews",
        }

        with st.sidebar:
            st.markdown("## 🎬 FlixApp")
            st.markdown("---")

            selected_label = st.radio(
                "Menu",
                list(MENU.keys()),
                label_visibility="collapsed"
            )

        menu_option = MENU[selected_label]

        if menu_option == 'home':
            show_home()

        if menu_option == 'genres':
            show_genres()

        if menu_option == 'actors':
            show_actors()

        if menu_option == 'movies':
            show_movies()

        if menu_option == 'reviews':
            show_reviews()


if __name__ == '__main__':
    main()
