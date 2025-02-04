# mcq_utils.py
import streamlit as st

DEFAULT_SUCCESS_MESSAGE = "Correct answer!"
DEFAULT_ERROR_MESSAGE = "Incorrect answer."
DEFAULT_BUTTON_MESSAGE = "Check Answer"


def single_choice(question, options, answer_index,
                  success=DEFAULT_SUCCESS_MESSAGE,
                  error=DEFAULT_ERROR_MESSAGE,
                  button=DEFAULT_BUTTON_MESSAGE):
    """Renders a single-choice question"""
    if len(question) == 0:
        st.error("Please provide a question")
        return None, None
    elif len(options) < 2:
        st.error("Must have at least 2 options")
        return None, None

    user_answer = st.radio(question, options=options)
    key = f"single-choice:{question}"

    if st.button(button, key=key):
        is_correct = (options.index(user_answer) == answer_index)
        if is_correct:
            st.success(success)
        else:
            st.error(error)
        return True, is_correct
    return False, None


def multiple_choice(question, answer_dict,
                    success=DEFAULT_SUCCESS_MESSAGE,
                    error=DEFAULT_ERROR_MESSAGE,
                    button=DEFAULT_BUTTON_MESSAGE):
    """Renders a multiple-choice question"""
    if len(question) == 0:
        st.error("Please provide a question")
        return None, None
    elif len(answer_dict) < 2:
        st.error("Must have at least 2 options")
        return None, None

    st.markdown(question)
    cb_list = []
    for option, is_correct in answer_dict.items():
        key = f"multiple-choice:{question}:{option}"
        cb = st.checkbox(option, key=key)
        cb_list.append(cb)

    if st.button(button):
        all_correct = all(
            [cb == answer for cb, answer in zip(cb_list, answer_dict.values())])
        if all_correct:
            st.success(success)
        else:
            st.error(error)
        return True, all_correct
    return False, None
