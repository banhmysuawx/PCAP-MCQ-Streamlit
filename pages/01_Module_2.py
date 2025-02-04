import streamlit as st
import streamlit_book as stb
from pathlib import Path

st.set_page_config(page_title="Module 2")
with stb.echo("above", False):

    stb.set_book_config(
        menu_title="Module 2: Python",
        menu_icon="lightbulb",
        options=[
            "Full Question",
            "Quiz Test",
        ],
        paths=[
            "pages/02_module_2/00_full_mcq.py",
            "pages/02_module_2/01_quiz.py",
        ],
        icons=[
            "signpost-2",
            "ui-radios",
        ],
        save_answers=False
    )
