import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.LLMS.ollamallm import OllamaLLMWrapper
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.

    """

    ##Load UI
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input: #This is the user input from the UI if no user input is found then error is shown
        st.error("Error: Failed to load user input from the UI.")
        return
    
    user_message = st.chat_input("Enter your message:") #This is the user message from the UI       

    if user_message:
        try:
            print(user_input)
            ## Configure The LLM's
            if user_input["selected_llm"] == "Groq":
                obj_llm_config=GroqLLM(user_contols_input=user_input) #calling the GroqLLM class and passing the user input to the class
                model=obj_llm_config.get_llm_model() #Returns the LLM model
            elif user_input["selected_llm"] == "Ollama":
                obj_llm_config=OllamaLLMWrapper(user_controls_input=user_input) # Use the wrapper class
                model=obj_llm_config.get_llm_model() #Returns the LLM model
            print("Hello")
            print(model)
            print("Hi")
            if not model:
                st.error("Error: LLM model could not be initialized")
                return
            
            # Initialize and set up the graph based on use case
            usecase=user_input.get("selected_usecase")

            if not usecase:
                    st.error("Error: No use case selected.")
                    return
            
            ## Graph Builder

            graph_builder=GraphBuilder(model)
            try:
                 graph=graph_builder.setup_graph(usecase) #Returns the graph type from the graph builder class based on the user input
                 DisplayResultStreamlit(usecase,graph,user_message,user_input.get("selected_llm")).display_result_on_ui()
            except Exception as e:
                 st.error(f"Error: Graph set up failed- {e}")
                 return

        except Exception as e:
             st.error(f"Error: Graph set up failed- {e}")
             return   
