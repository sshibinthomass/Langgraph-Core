import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json


class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_message,selected_llm=None):
        self.usecase= usecase
        self.graph = graph
        self.user_message = user_message
        self.selected_llm = selected_llm

    def display_result_on_ui(self):
        usecase= self.usecase
        graph = self.graph
        user_message = self.user_message
        selected_llm = self.selected_llm
        if usecase =="Basic Chatbot":
                for event in graph.stream({'messages':("user",user_message)}):
                    for value in event.values():
                        with st.chat_message("user"):
                            st.write(user_message)
                        with st.chat_message("assistant"):
                            if selected_llm == "Groq":
                                st.write(value["messages"].content)
                            else:
                                st.write(value["messages"])