import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page

def chat_page():
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
    
    # Add this CSS right after the st.set_page_config() call
    st.markdown("""
        <style>
        body {
            background-color: #EDE7D7;
        }
        </style>
        """, unsafe_allow_html=True)
    
    # Modify Content Security Policy
    st.markdown("""
        <meta http-equiv="Content-Security-Policy" 
        content="default-src 'self'; 
        script-src 'self' 'unsafe-inline' 'unsafe-eval' https://unpkg.com https://cdnjs.cloudflare.com; 
        style-src 'self' 'unsafe-inline';
        img-src 'self' data: https:;
        connect-src 'self' https://bots.dev.studio.nlx.ai;
        frame-src 'self' https://www.youtube.com;">
    """, unsafe_allow_html=True)
    
    st.title("Chat with Zephyr")

    # Add a button to go back to the journal page
    if st.button("Back to Journal"):
        switch_page("journal")

    # Chat widget
    chat_html = """
    <div id="chat-widget-container" style="width:100%; height:calc(100vh - 150px);">
        <div id="chat-widget" style="width:100%; height:100%;"></div>
    </div>
    <script defer src="https://unpkg.com/@nlxai/chat-widget/lib/index.umd.js"></script>
    <script defer src="https://cdnjs.cloudflare.com/ajax/libs/htm/3.1.1/htm.js" integrity="sha512-RilD4H0wcNNxG2GvB+L1LRXCntT0zgRvRLnmGu+e9wWaLKGkPifz3Ozb6+WPsyEkTBLw6zWCwwEjs9JLL1KIHg==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script>
      window.addEventListener("DOMContentLoaded", () => {
        // EMBEDDABLE COMPONENT SETUP
        const React = nlxai.chatWidget.React;
        const useConversationHandler = nlxai.chatWidget.useConversationHandler;
        const html = htm.bind(React.createElement);
     
        Video = ({ data }) => {
          console.log("Video component called with data:", data);
          const videoSrc = `https://www.youtube.com/embed/${data.src}`;
          return html`
            <iframe
              width="264"
              height="160"
              src=${videoSrc}
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
            ></iframe>`;
        };

        const widget = nlxai.chatWidget.create({
          config: {
            botUrl: "https://bots.dev.studio.nlx.ai/c/8CkPIDiIOvlWToUYScqtI/df9G1HlryEWmW8QxgTtLx",
            headers: {
              "nlx-api-key": "lDUZ8LmOrNsf/E5=zd=smoQrw9zS7_=x"
            },
            languageCode: "en-US"
          },
          titleBar: {
            "title": "Chat with Zephyr"
          },
          onExpand: (conversationHandler) => {
            const checkMessages = (messages) => {
              console.log("Current messages:", messages);
              if (messages.length === 0) {
                console.log("Sending welcome intent");
                conversationHandler.sendWelcomeIntent();
              }
              conversationHandler.unsubscribe(checkMessages);
            };
            conversationHandler.subscribe(checkMessages);
          },
          customModalities: { Video },
          theme: {
            "primaryColor": "#2663da",
            "darkMessageColor": "#2663da",
            "lightMessageColor": "#EFEFEF",
            "white": "#FFFFFF",
            "fontFamily": "-apple-system, BlinkMacSystemFont, \\"Segoe UI\\", Roboto, Oxygen-Sans, Ubuntu, Cantarell, \\"Helvetica Neue\\", sans-serif",
            "spacing": 12,
            "borderRadius": 8,
            "chatWindowMaxHeight": 640
          }
        });
      });
    </script>
    """
    components.html(chat_html, height=700, scrolling=True)

def main():
    chat_page()

if __name__ == "__main__":
    main()
