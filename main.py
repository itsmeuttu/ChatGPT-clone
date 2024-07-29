import streamlit as st
import logging
import ollama
from typing import List, Dict, Tuple, Any

# Streamlit page configuration
st.set_page_config(
    page_title="Sigma AI",
    page_icon="∮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

@st.cache_resource(show_spinner=True)
def extract_model_names(models_info: Dict[str, List[Dict[str, Any]]]) -> Tuple[str, ...]:
    """
    Extract model names from the provided models information.
    """
    logger.info("Extracting model names from models_info")
    model_names = tuple(model["name"] for model in models_info["models"])
    logger.info(f"Extracted model names: {model_names}")
    return model_names

def process_question(question: str, selected_model: str) -> str:
    """
    Process a user question using the selected language model.
    """
    logger.info(f"Processing question: {question} using model: {selected_model}")
    response = ollama.chat(model=selected_model, messages=[{'role': 'user', 'content': question}])
    response_content = response['message']['content']
    logger.info("Question processed and response generated")
    return response_content

def main() -> None:
    """
    Main function to run the Streamlit application.
    """
    st.sidebar.subheader("Model Selection")

    models_info = ollama.list()
    available_models = extract_model_names(models_info)

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    if available_models:
        selected_model = st.sidebar.selectbox(
            "Pick a model available locally on your system ↓", available_models
        )

    st.subheader("Sigma AI")

    message_container = st.container()

    for message in st.session_state["messages"]:
        avatar = "🤖" if message["role"] == "assistant" else "☃️"
        with message_container.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter a prompt here..."):
        try:
            st.session_state["messages"].append({"role": "user", "content": prompt})
            message_container.chat_message("user", avatar="☃️").markdown(prompt)

            with message_container.chat_message("assistant", avatar="🤖"):
                with st.spinner(":green[processing...]"):
                    response = process_question(prompt, selected_model)
                    st.markdown(response)

            st.session_state["messages"].append(
                {"role": "assistant", "content": response}
            )

        except Exception as e:
            st.error(e, icon="⛔️")
            logger.error(f"Error processing prompt: {e}")


   

if __name__ == "__main__":
    main()


        
 