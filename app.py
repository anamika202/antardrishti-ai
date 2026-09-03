import os
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API key from environment/secret
API_KEY = os.environ.get("GEMINI_API_KEY", "")
if API_KEY:
    genai.configure(api_key=API_KEY)

@app.route("/")
def home():
    try:
        with open("index.html", "r") as f:
            return f.read()
    except Exception as e:
        return f"Antardrishti AI Service Active. Status: Healthy ({str(e)})"

@app.route("/api/reflect", methods=["POST"])
def reflect():
    data = request.get_json() or {}
    journal_text = data.get("text", "")
    
    if not journal_text:
        return jsonify({"error": "No journal entry provided"}), 400

    if not API_KEY:
        return jsonify({
            "reflection": f"[Reflective Mode] Thank you for expressing: '{journal_text[:40]}...'. Notice how putting words to thought brings clarity."
        })

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = (
            "You are Antardrishti AI, an empathetic, non-judgmental mindfulness and emotional reflection companion. "
            "Analyze this user reflection and respond with 2-3 grounding, warm, and supportive sentences: "
            + journal_text
        )
        response = model.generate_content(prompt)
        return jsonify({"reflection": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
