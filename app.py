import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage , SystemMessage , AIMessage

os.environ['OPENAI_API_KEY'] = "KEY"

st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")

chat_model = ChatOpenAI(temperature=0.7)

if 'flow_message' not in st.session_state:
    st.session_state['flow_message'] = [SystemMessage(content="You are Medcare AI Assistant. who have wide knowledge of medical Science")]

def get_response(input):
    st.session_state['flow_message'].append(HumanMessage(content=input))
    response = chat_model(st.session_state['flow_message'])
    print(response.content)
    st.session_state['flow_message'].append(AIMessage(content=response.content))
    return response.content

input  = st.text_input("Input: " , key="input")

submit = st.button("Ask the Question")

if submit and input:
    response = get_response(input)
    st.subheader("Response: ")
    st.write(response)