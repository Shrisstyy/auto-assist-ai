import streamlit as st
import requests

st.set_page_config(page_title="AI Support Assistant", layout="centered")

st.title("AI Customer Support Assistant 💬")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Callback function (IMPORTANT)
def send_message():
    user_input = st.session_state.input_box

    if user_input.strip() == "":
        return

    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        with st.spinner("Thinking..."):
            res = requests.post(
                "http://127.0.0.1:8000/chat",
                json={"message": user_input},
                timeout=30
            )

            data = res.json()

            if data.get("status") == "Escalated":
                bot_reply = data.get("message", "Escalated")
            else:
                bot_reply = data.get("response", "No response")

            # Add bot message
            st.session_state.messages.append({
                "role": "bot",
                "content": bot_reply
            })

    except Exception as e:
        st.error(f"Error: {str(e)}")

    # ✅ Clear input safely
    st.session_state.input_box = ""


# Display chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"🧑 **You:** {msg['content']}")
    else:
        st.markdown(f"🤖 **Bot:** {msg['content']}")

# Input box
st.text_input("Type your message...", key="input_box")

# Send button with callback
st.button("Send", on_click=send_message)