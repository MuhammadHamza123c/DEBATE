import streamlit as st
import religious
import athiest

# Initialize session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🕌🤖 Atheist vs Religious Bot Conversation")

# Let atheist start the conversation
if st.button("Start Conversation"):
    atheist_msg = "Why there are so much Strictness for Women in Islam but not for Men???"
    st.session_state.messages.append(("Atheist", atheist_msg))

# Show current messages
for speaker, msg in st.session_state.messages:
    if speaker == "Atheist":
        st.markdown(f"<p style='color:red'><b>Atheist:</b> {msg}</p>", unsafe_allow_html=True)
    else:
        st.markdown(f"<p style='color:green'><b>Religious:</b> {msg}</p>", unsafe_allow_html=True)

# Respond when last message is from Atheist
if st.session_state.messages and st.session_state.messages[-1][0] == "Atheist":
    if st.button("Respond from Religious Bot"):
        atheist_msg = st.session_state.messages[-1][1]
        religious_msg = religious.chat_with_Religious(atheist_msg)
        st.session_state.messages.append(("Religious", religious_msg))

# Respond when last message is from Religious
if st.session_state.messages and st.session_state.messages[-1][0] == "Religious":
    if st.button("Respond from Atheist Bot"):
        religious_msg = st.session_state.messages[-1][1]
        atheist_msg = athiest.chat_with_athiest(religious_msg)
        st.session_state.messages.append(("Atheist", atheist_msg))

