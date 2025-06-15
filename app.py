import streamlit as st
from chatbot.chatbot import get_rag_chain
from chatbot.utils import ComplaintChatSession
import requests

st.title("🤖 Complaint Chatbot")

qa = get_rag_chain()

if "session" not in st.session_state:
    st.session_state.session = ComplaintChatSession()

user_input = st.text_input("You:", key="user_input")

if user_input:
    if "show" in user_input.lower() and "complaint" in user_input.lower():
        complaint_id = user_input.strip().split()[-1]
        res = requests.get(f"http://127.0.0.1:8000/complaints/{complaint_id}")
        if res.status_code == 200:
            data = res.json()
            st.markdown(f"**Complaint ID:** {data['complaint_id']}")
            st.markdown(f"**Name:** {data['name']}")
            st.markdown(f"**Phone:** {data['phone_number']}")
            st.markdown(f"**Email:** {data['email']}")
            st.markdown(f"**Details:** {data['complaint_details']}")
            st.markdown(f"**Created At:** {data['created_at']}")
        else:
            st.error("Complaint not found.")
    else:
        session = st.session_state.session
        session.update_data(user_input)

        if session.is_complete():
            res = session.submit_complaint()
            st.success(f"✅ Complaint registered. ID: {res['complaint_id']}")
            session.reset()
        else:
            st.write(session.get_next_prompt())
