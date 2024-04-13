**Conversational Chatbot with BlenderBot**

This project implements a conversational chatbot using the BlenderBot model from Facebook's AI Research (FAIR). The chatbot is built using Python and Flask framework for the backend, and HTML, CSS, and JavaScript for the frontend.

**Features**

- Allows users to engage in a conversation with a chatbot powered by the BlenderBot model.
- Provides a simple and intuitive user interface for interacting with the chatbot.
- Utilizes Flask as the web server framework for handling user requests and serving responses.
- Integrates the Hugging Face `transformers` library to interact with the BlenderBot model for generating responses.

**Prerequisites**

Before running the application, ensure you have the following installed:

- Python 3.x
- Flask (`pip install Flask`)
- transformers (`pip install transformers`)

**Usage**

1. Clone this repository to your local machine.
2. Run the Flask web server by executing `python app.py` in the project directory.
3. Open a web browser and navigate to `http://localhost:5000` to interact with the chatbot.

**How it Works**

1. Upon launching the application, users are presented with a chat interface where they can type messages to the chatbot.
2. The user's message is sent to the Flask backend via a POST request to the `/chatbot` endpoint.
3. The Flask server processes the user's message, tokenizes it, and feeds it to the BlenderBot model to generate a response.
4. The generated response is sent back to the frontend and displayed in the chat interface.
5. The conversation history is maintained on the server side to provide context for generating subsequent responses.

**Credits**

- This project utilizes the Hugging Face `transformers` library, which provides easy access to pre-trained natural language processing models.

**Acknowledgements**

Special thanks to the developers of the BlenderBot model and the Hugging Face `transformers` library for making this project possible.

Feel free to customize and extend this project according to your needs. If you have any questions or suggestions, please don't hesitate to contact us. We hope you enjoy using our conversational chatbot!
