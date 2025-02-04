import streamlit as st
import streamlit_book as stb

st.set_page_config(page_title="Module 1")

with stb.echo("above", False):
    stb.set_chapter_config(path="pages/01_module_1", save_answers=False)
