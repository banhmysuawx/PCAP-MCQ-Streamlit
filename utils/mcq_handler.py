# mcq_handler.py
import streamlit as st
import pandas as pd
from pathlib import Path
from utils.mcq_utils import single_choice, multiple_choice


def load_questions(module_name):
    """Load questions from CSV for specified module"""
    current_dir = Path(__file__).parent
    csv_path = current_dir / f"../data/{module_name}/questions.csv"
    try:
        return pd.read_csv(csv_path)
    except FileNotFoundError:
        st.error(f"Questions file not found for module: {module_name}")
        return pd.DataFrame()


def show_questions(questions):
    """Display questions from DataFrame"""
    for _, row in questions.iterrows():
        question_type = row['type']
        question_text = row['question']
        options = row['options'].split(';')
        correct_answer = row['correct_answer']

        if question_type == 'single':
            answer_index = int(correct_answer)
            single_choice(
                question=question_text,
                options=options,
                answer_index=answer_index
            )
        elif question_type == 'multiple':
            correct_indices = list(map(int, correct_answer.split(';')))
            answer_dict = {
                opt: (i in correct_indices)
                for i, opt in enumerate(options)
            }
            multiple_choice(
                question=question_text,
                answer_dict=answer_dict
            )
