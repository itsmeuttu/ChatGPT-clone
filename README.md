# ChatGPT clone using Ollama

This Streamlit application allows users to interact with various local language models using a chat interface locally. The selected language model is used to process user prompts and provide responses. 

![alt text](<Images/Pasted image.png>)

## Features

- **Model Selection**: Choose from locally available language models.
- **Chat Interface**: Interact with the selected model using a chat-like interface.
- **Localhost**: Use it without internet connection
## Requirements

- Streamlit
- Ollama Python library

## Installation
Download the  ollama : https://ollama.com/download
Download any LLM: https://ollama.com/library

### Step 1: Clone the Repository

```sh
git clone https://github.com/itsmeuttu/ChatGPT-clone.git
cd ChatGPT-clone
```
### Create a Virtual Environment and Activate It

```python3 -m venv venv
source venv/bin/activate  
# On Windows use `venv\Scripts\activate`
```


### Step 3: Install the Required Packages 

``` pip install -r requirements.txt```

## Usage

### Step 1: Run the Streamlit App

```streamlit run main.py```

### Step 3: Interact with the Chat Interface
- Select a model from the sidebar.
- Enter a prompt in the chat input box.
- View the model's response.



