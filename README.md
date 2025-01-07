# sts_bot 
 
### To Download Requirement 
```
pip install -r requirements.txt
```
### Features

- **Speech Recognition**: Converts user speech to text using Google Speech Recognition API.
- **Generative AI Integration**: Processes user input with Google's Gemini LLM API for generating responses.
- **Text-to-Speech (TTS)**: Converts AI-generated responses back into speech using `pyttsx3`.
- **Streamlit Interface**: Provides an interactive web-based UI.
- **Session Management**: Maintains conversation history during a session.

  
### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/shivam1750/tensorgo_sts_bot.git
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv env
    env\Scripts\activate
    ```

3. Set up the `.env` file with your Gemini API key:
    ```env
    GEMINI_API_KEY=your_api_key_here
    ```

### Usage : 
Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

### Configuration

The application uses the following configuration for the LLM:

- **Temperature**: 1
- **Top-p**: 0.95     #above >9
- **Top-k**: 64
- **Max Output Tokens**: 8192
