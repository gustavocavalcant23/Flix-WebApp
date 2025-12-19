import streamlit as st

from .repository import ActorsRepository


class ActorService:

    def __init__(self):
        self.actor_repository = ActorsRepository()

    def get_actors(self):
        if 'actors' in st.session_state:
            return st.session_state.actors

        NATIONALITY_FORMATER = {
            'BRL': 'Brasil',
            'USA': 'Estados Unidos',
        }

        actors = self.actor_repository.get_actors()
        actors_list = list()

        for actor in actors:
            actor_nationality = NATIONALITY_FORMATER.get(actor.get('nationality'))
            actors_list.append(
                {
                    "id": actor.get('id'),
                    "name": actor.get('name'),
                    "nationality": actor_nationality,
                }
            )
        st.session_state.actors = actors_list
        return actors_list

    def create_actor(self, name, nationality):
        NATIONALITY_CHOICES = {
            'Estados Unidos': 'USA',
            'Brasil': 'BRL'
        }

        nationality_choice = NATIONALITY_CHOICES.get(nationality)

        actor = dict(
            name=name,
            nationality=nationality_choice
        )

        new_actor = self.actor_repository.create_actor(
            actor=actor
        )
        if 'actors' in st.session_state:
            del st.session_state.actors
            self.get_actors()
        return new_actor
