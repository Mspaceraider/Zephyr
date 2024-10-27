import streamlit as st

def load_css():
    st.markdown("""
    <style>
    .curved-box {
        background-color: #f0f0f0;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .curved-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)
