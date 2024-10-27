import streamlit as st

def journal_page():
    st.markdown("""
    <style>
        body {
            background-color: white;
            color: black;
            font-family: 'Poppins', sans-serif;
        }
        .content {
            width: 90%;
            max-width: 800px;
            margin: 2rem auto;
            padding: 2rem;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            position: relative;
        }
        h1 {
            text-align: center;
            color: #2b0e3a;
            margin-bottom: 1rem;
        }
        textarea {
            width: 100%;
            height: 300px;
            padding: 1rem;
            border: 1px solid #ccc;
            border-radius: 5px;
            resize: vertical;
        }
        .gradient-bar {
            position: absolute;
            top: 0;
            right: 0;
            width: 20px;
            height: 100%;
            background: linear-gradient(to bottom, #ff69b4, #1f1147);
            border-top-right-radius: 10px;
            border-bottom-right-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='content'>", unsafe_allow_html=True)
    st.markdown("<h1>ZEPHRY</h1>", unsafe_allow_html=True)
    st.text_area("Start your journal entry here...", height=300)
    st.button("Save Entry")
    st.markdown("<div class='gradient-bar'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Back to Main Page"):
        st.experimental_set_query_params()
        st.experimental_rerun()

journal_page()