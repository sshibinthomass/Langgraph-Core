import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self,user_contols_input): #user_contols_input is the user controls input from the UI passed from Main.py
        self.user_controls_input=user_contols_input

    def get_llm_model(self):
        try:
            groq_api_key=self.user_controls_input["GROQ_API_KEY"]
            selected_groq_model=self.user_controls_input["selected_groq_model"]
            if groq_api_key=='' and os.environ["GROQ_API_KEY"] =='':
                st.error("Please Enter the Groq API KEY")

            llm=ChatGroq(api_key=groq_api_key,model=selected_groq_model)

        except Exception as e:
            raise ValueError(f"Error Ocuured With Exception : {e}")
        return llm

if __name__ == "__main__":
    # Example user_controls_input
    user_controls_input = {
        "GROQ_API_KEY": os.getenv("GROQ_API_KEY", ""),  # Use env var or set your key here
        "selected_groq_model": "llama3-8b-8192"  # Replace with a valid model for your Groq account
    }

    groq_llm = GroqLLM(user_controls_input)
    llm = groq_llm.get_llm_model()
    print(type(llm))
    #if llm:
    ##    prompt = "What is the capital of France?"
    #    try:
    #        response = llm.invoke(prompt)
    #        print("Response:", response)
    #    except Exception as e:
    #        print("Error during invocation:", e)
    #else:
    #    print("LLM could not be initialized.")