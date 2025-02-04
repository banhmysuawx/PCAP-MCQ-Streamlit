import streamlit as st
import streamlit_book as stb


def main():
    st.set_page_config(
        page_title="PCAP MCQ - Introduction",
        page_icon="👋",
        layout="wide"
    )
    st.sidebar.header("PCAP MCQ")
    st.write("# Welcome to PCAP MCQ! 👋")

    st.markdown(
        """
        This interactive application helps you prepare for the PCAP (Python Certified Associate Programmer) certification 
        through multiple-choice questions (MCQs) covering all exam modules.
        
        ### 🎯 What is PCAP?
        The PCAP certification is a professional credential that validates your Python programming skills. 
        It covers fundamental concepts and demonstrates your ability to understand and use Python features.
        
        ### 📚 What You'll Find Here
        - **Module-based Learning**: Questions organized by PCAP exam modules
        - **Interactive Practice**: Real-time feedback on your answers
        - **Comprehensive Coverage**: All major PCAP topics included
        - **Clear Explanations**: Detailed explanations for each answer
        
        ### 🗺️ Module Overview
        1. **Module 1**: Basics, Input/Output Operations, and Basic Data Types
        2. **Module 2**: Control Flow, Conditional Blocks, and Loops
        3. **Module 3**: Functions and Exceptions
        4. **Module 4**: Data Collections and Standard Library
        5. **Module 5**: Object-Oriented Programming
        
        ### 🚀 Getting Started
        Select any module from the sidebar to begin practicing. Each module contains carefully crafted 
        questions that mirror the style and difficulty of the actual PCAP exam.
        
        ### 💡 Tips for Success
        - Take your time to understand each question
        - Review explanations even for correct answers
        - Practice regularly across all modules
        - Pay attention to code snippets and their outputs
        
        Good luck with your PCAP preparation! 🌟
        """
    )

    # Add a footer with version info
    st.markdown("---")
    st.markdown("*PCAP MCQ v1.0 - Your Path to Python Certification*")
    stb.floating_button("https://dinhtruong.dev")


if __name__ == "__main__":
    main()
