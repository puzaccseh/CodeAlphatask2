from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load predefined intents/responses
with open("responses.json", "r") as file:
    chatbot_data = json.load(file)

def get_response(user_input):
    user_input = user_input.lower()
    for intent in chatbot_data["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input:
                return intent["response"]
    return "I'm sorry, I didn't understand that. Can you rephrase?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_msg = request.form["msg"]
    bot_response = get_response(user_msg)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
