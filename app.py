# app.py
import streamlit as st

# Function to navigate to the journal page
def go_to_journal():
    st.session_state.page = "journal"

# Main Function
def main():
    st.set_page_config(page_title="ZEPHRY", layout="wide", initial_sidebar_state="collapsed")

    if 'page' not in st.session_state:
        st.session_state.page = "main"
    
    if st.session_state.page == "main":
        st.title("Welcome to ZEPHRY")
        st.write("This is the main page of your app.")
        
        # Button to navigate to the journal page
        if st.button("Go to Journal"):
            go_to_journal()

    elif st.session_state.page == "journal":
        from pages import journal  # Adjusting the import to reference the pages directory
        journal.journal_page()  # Call the journal page function directly

if __name__ == "__main__":
    main()
