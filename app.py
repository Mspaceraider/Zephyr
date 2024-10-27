import streamlit as st
import streamlit.components.v1 as components

def chatbot_html():
    return """
    <div id="chat-container" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:1000;">
        <div style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); width:80%; max-width:600px; height:80%; background:white; border-radius:10px; overflow:hidden;">
            <button onclick="document.getElementById('chat-container').style.display='none'" style="position:absolute; top:10px; right:10px; z-index:1001;">Close</button>
            <div id="chat-widget" style="width:100%; height:100%;"></div>
        </div>
    </div>
    <script defer src="https://unpkg.com/@nlxai/chat-widget/lib/index.umd.js"></script>
    <script>
      window.addEventListener("DOMContentLoaded", () => {
        const widget = nlxai.chatWidget.create({
          config: {
            botUrl: "https://bots.dev.studio.nlx.ai/c/rRoRAYuJapx3oJHBQmGEF/ZGCrQb8-hlxCiGdsyLKdt",
            headers: {
              "nlx-api-key": "lDUZ8LmOrNsf/E5=zd=smoQrw9zS7_=x"
            },
            languageCode: "en-US"
          },
          titleBar: {
            "title": "Support",
            "withCollapseButton": true,
            "withCloseButton": true
          },
          onExpand: (conversationHandler) => {
            const checkMessages = (messages) => {
              if (messages.length === 0) {
                conversationHandler.sendWelcomeIntent();
              }
              conversationHandler.unsubscribe(checkMessages);
            };
            conversationHandler.subscribe(checkMessages);
          },
          theme: {
            "primaryColor": "#2663da",
            "darkMessageColor": "#2663da",
            "lightMessageColor": "#EFEFEF",
            "white": "#FFFFFF",
            "fontFamily": "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen-Sans, Ubuntu, Cantarell, \"Helvetica Neue\", sans-serif",
            "spacing": 12,
            "borderRadius": 8,
            "chatWindowMaxHeight": 640
          },
          containerEl: document.getElementById("chat-widget")
        });
      });

      function openChat() {
        document.getElementById('chat-container').style.display = 'block';
      }
    </script>
    """

def main_page():
    st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #2b0e3a 0%, #1f1147 100%);
            color: white;
            font-family: 'Poppins', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .content {
            text-align: center;
        }
        h1 {
            color: #ff69b4;
            font-size: 5rem;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        .button {
            background-color: #ff69b4;
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 50px;
            transition: all 0.3s ease;
        }
        .button:hover {
            background-color: #ff1493;
            transform: translateY(-2px);
        }
    </style>
    <div class="content">
        <h1>ZEPHRY</h1>
        <button class="button" onclick="openChat()">Chat with Zephry</button>
    </div>
    """, unsafe_allow_html=True)
    
    components.html(chatbot_html(), height=0)
    
    if st.button("Wanna journal?"):
        st.session_state.page = "journal"
        st.rerun()

def journal_page():
    st.markdown("""
    <style>
        body {
            background-color: #f0f0f0;
            color: #333;
            font-family: 'Poppins', sans-serif;
        }
        .content {
            width: 90%;
            max-width: 800px;
            margin: 2rem auto;
            padding: 2rem;
            position: relative;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #2b0e3a;
            margin-bottom: 2rem;
            font-size: 2.5rem;
        }
        .journal-area {
            width: 100%;
            height: 500px;
            padding: 1rem;
            border: none;
            background-image: 
                linear-gradient(#e5e5e5 1px, transparent 1px),
                linear-gradient(90deg, #e5e5e5 1px, transparent 1px);
            background-size: 20px 20px;
            background-color: white;
            border-radius: 5px;
            font-size: 1rem;
            line-height: 20px;
            resize: none;
        }
        .gradient-bar {
            position: fixed;
            top: 0;
            right: 0;
            width: 15px;
            height: 100%;
            background: linear-gradient(to bottom, #ff69b4, #1f1147);
        }
        .button {
            background-color: #ff69b4;
            border: none;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 25px;
            transition: all 0.3s ease;
        }
        .button:hover {
            background-color: #ff1493;
            transform: translateY(-2px);
        }
        .button-container {
            display: flex;
            justify-content: space-between;
            margin-top: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='content'>", unsafe_allow_html=True)
    st.markdown("<h1>ZEPHRY</h1>", unsafe_allow_html=True)
    st.text_area("", placeholder="Start your journal entry here...", height=500, key="journal_entry")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("Save Entry", on_click=lambda: st.success("Journal entry saved!"))
    with col2:
        st.button("Back to Main Page", on_click=lambda: st.session_state.update(page="main"))

    st.markdown("<div class='gradient-bar'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Embed the NLX chatbot directly on the screen
    chat_html = """
    <div id="chat-widget" style="width:100%; height:500px;"></div>
    <script defer src="https://unpkg.com/@nlxai/chat-widget/lib/index.umd.js"></script>
    <script>
      window.addEventListener("DOMContentLoaded", () => {
        const widget = nlxai.chatWidget.create({
          config: {
            botUrl: "https://bots.dev.studio.nlx.ai/c/rRoRAYuJapx3oJHBQmGEF/ZGCrQb8-hlxCiGdsyLKdt",
            headers: {
              "nlx-api-key": "lDUZ8LmOrNsf/E5=zd=smoQrw9zS7_=x"
            },
            languageCode: "en-US"
          },
          titleBar: {
            "title": "Support",
            "withCollapseButton": true,
            "withCloseButton": true
          },
          onExpand: (conversationHandler) => {
            const checkMessages = (messages) => {
              if (messages.length === 0) {
                conversationHandler.sendWelcomeIntent();
              }
              conversationHandler.unsubscribe(checkMessages);
            };
            conversationHandler.subscribe(checkMessages);
          },
          theme: {
            "primaryColor": "#2663da",
            "darkMessageColor": "#2663da",
            "lightMessageColor": "#EFEFEF",
            "white": "#FFFFFF",
            "fontFamily": "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Oxygen-Sans, Ubuntu, Cantarell, \"Helvetica Neue\", sans-serif",
            "spacing": 12,
            "borderRadius": 8,
            "chatWindowMaxHeight": 640
          },
          containerEl: document.getElementById("chat-widget")
        });
      });
    </script>
    """
    
    components.html(chat_html, height=500)

def main():
    st.set_page_config(page_title="ZEPHRY", layout="wide", initial_sidebar_state="collapsed")

    if 'page' not in st.session_state:
        st.session_state.page = "main"
    
    if st.session_state.page == "main":
        main_page()
    elif st.session_state.page == "journal":
        journal_page()

if __name__ == "__main__":
    main()
