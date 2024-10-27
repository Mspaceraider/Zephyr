# pages/journal.py
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_webrtc import webrtc_streamer
import speech_recognition as sr
import streamlit.components.v1 as components  # Add this import
import hashlib

# Function to save journal entry
def save_entry():
    journal_content = st.session_state.journal_entry
    if journal_content:
        st.success("Journal entry saved!")
    else:
        st.warning("Please enter some text to save!")

# Function to toggle chat visibility
def toggle_chat():
    st.session_state.chat_visible = not st.session_state.get('chat_visible', False)

# Function to perform speech-to-text
def perform_speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening... Speak now!")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            st.session_state.journal_entry += " " + text
            st.experimental_rerun()
        except sr.UnknownValueError:
            st.write("Could not understand audio")
        except sr.RequestError as e:
            st.write(f"Could not request results; {e}")

# Journal Page Layout
def journal_page():
    st.markdown("""
        <style>
        body {
            background-color: #EDE7D7;
        }
        .stButton > button {
            width: 100%;
            height: 3em;
            margin-top: 1em;
        }
        </style>
        """, unsafe_allow_html=True)
    
    st.title("ZEPHYR Journal")
    
    if 'journal_entry' not in st.session_state:
        st.session_state.journal_entry = ""

    journal_entry = st.text_area("Journal Entry", value=st.session_state.journal_entry, height=300, key="journal_entry")
    
    # Create columns for buttons
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("Start Speech-to-Text", on_click=perform_speech_to_text):
            pass

    with col2:
        st.button("Save Entry", on_click=save_entry)

    with col3:
        st.button("Back to Login", on_click=lambda: switch_page("app"), key="back_button")

    with col4:
        if st.button("Chat with Zephyr"):
            switch_page("chat")

    # Display the current journal entry
    st.subheader("Current Journal Entry:")
    st.write(st.session_state.journal_entry)

    # JavaScript for continuous speech recognition
    st.components.v1.html("""
    <div id="speech-to-text-container"></div>
    <script>
    let recognition;
    let isListening = false;

    if ('webkitSpeechRecognition' in window) {
        recognition = new webkitSpeechRecognition();
        recognition.continuous = true;
        recognition.interimResults = true;

        recognition.onresult = function(event) {
            const textArea = document.querySelector('textarea[aria-label="Journal Entry"]');
            if (textArea) {
                let finalTranscript = '';
                for (let i = event.resultIndex; i < event.results.length; ++i) {
                    if (event.results[i].isFinal) {
                        finalTranscript += event.results[i][0].transcript + ' ';
                    }
                }
                textArea.value += finalTranscript;
                textArea.dispatchEvent(new Event('input', { bubbles: true }));
                textArea.dispatchEvent(new Event('change', { bubbles: true }));
                
                // Send update to Streamlit
                fetch('/_stcore/stream', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        'journal_entry': textArea.value,
                        'hash': '${st.session_state.journal_entry_hash}'
                    })
                });
            }
        };
    }

    function toggleSpeechRecognition(icon) {
        if (!recognition) {
            alert('Speech recognition is not supported in this browser.');
            return;
        }

        if (isListening) {
            recognition.stop();
            isListening = false;
            icon.textContent = '🎙️';
            icon.classList.remove('active');
        } else {
            recognition.start();
            isListening = true;
            icon.textContent = '🛑';
            icon.classList.add('active');
        }
    }

    function initializeSpeechToText() {
        const textArea = document.querySelector('textarea[aria-label="Journal Entry"]');
        if (textArea) {
            const icon = document.createElement('span');
            icon.textContent = '🎙️';
            icon.className = 'speech-to-text-icon';
            icon.style.position = 'absolute';
            icon.style.right = '10px';
            icon.style.bottom = '10px';
            icon.style.cursor = 'pointer';
            icon.style.fontSize = '24px';
            icon.onclick = function() { toggleSpeechRecognition(this); };
            textArea.parentNode.style.position = 'relative';
            textArea.parentNode.appendChild(icon);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initializeSpeechToText);
    } else {
        initializeSpeechToText();
    }
    </script>
    """, height=0)

    # Use session state to update the journal entry
    if st.session_state.journal_entry != journal_entry:
        st.session_state.journal_entry = journal_entry

# Main Function to call journal page
def main():
    if 'journal_entry_hash' not in st.session_state:
        st.session_state.journal_entry_hash = hashlib.md5(str(id(st.session_state)).encode()).hexdigest()
    journal_page()

if __name__ == "__main__":
    main()
