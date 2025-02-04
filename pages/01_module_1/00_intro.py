# module_1_page.py
import streamlit as st
from utils.mcq_handler import load_questions, show_questions


def main():
    st.title("Module 1: Basic Math")
    questions = load_questions("module_1")
    show_questions(questions)


if __name__ == "__main__":
    main()
