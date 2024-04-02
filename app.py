import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


def get_bot_response(input_text):
    global bot_responded
    llm = CTransformers(model='paste your model path',
                        model_type='llama',
                        config={'max_new_tokens': 256,
                                'temperature': 0.01})
    template = """ {input_text} """
    
    prompt = PromptTemplate(input_variables=["input_text"],template=template)
    
    response = llm(prompt.format(input_text=input_text))
    
    bot_responded = False
    
    return response

st.title("")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message['content'])

prompt = st.chat_input("What is up")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role" : "user" , "content" : prompt})

    response = get_bot_response(prompt) 

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role" : "assistant" , "content" : response})