from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import json
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)
CORS(app)

model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
conversation_history = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    data = request.get_data(as_text=True)
    data = json.loads(data)
    input_text = data['prompt']
    
    # Add user input to conversation history
    conversation_history.append(input_text)
    
    # If conversation history is empty, respond with a default message
    if len(conversation_history) == 0:
        response_text = "Hello! How can I assist you today?"
    else:
        # Create conversation history string
        history = "\n".join(conversation_history)

        # Tokenize the input text and history
        inputs = tokenizer.encode_plus(history, input_text, return_tensors="pt")

        # Generate the response from the model
        outputs = model.generate(**inputs)

        # Decode the response
        response_text = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

        # Add response to conversation history
        conversation_history.append(response_text)

    # Return the response in a more human-readable format
    return response_text

if __name__ == '__main__':
    app.run()
