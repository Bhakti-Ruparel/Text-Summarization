import os
from flask import Flask, render_template, request, jsonify
from transformers import pipeline

# 1. Initialize Flask Application
# We don't need to specify the template folder path as 'templates' is the default
app = Flask(__name__)

# 2. Load the Hugging Face Summarization Pipeline
# It's crucial to load the model only once when the app starts.
# Recommended model for speed and good performance: sshleifer/distilbart-cnn-12-6
print("Loading model... This may take a moment on first run.")
try:
    # Use the pipeline abstraction for easy summarization
    summarizer = pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6",
        # Use device=0 for GPU if available, or -1 for CPU (default)
        device=-1 
    )
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    # In a real app, you might want to handle this more gracefully
    summarizer = None


# --- Flask Routes ---

@app.route('/', methods=['GET'])
def index():
    """Renders the main HTML page."""
    # Flask looks for index.html inside the 'templates' folder
    return render_template('index.html')


@app.route('/summarize', methods=['POST'])
def summarize_text():
    """Handles the text summarization API request."""
    if not summarizer:
        return jsonify({"error": "Summarization model failed to load."}), 500

    # Get the JSON data sent from the frontend
    data = request.get_json()
    text = data.get('text', '')
    
    if not text or len(text.split()) < 20:
        # Simple check for minimum text length before running the model
        return jsonify({"summary": "Please provide a longer text (at least 20 words) to summarize."})

    try:
        # Define generation parameters for abstractive summarization
        # You can adjust min_length and max_length based on your needs
        summary_params = {
            "max_length": min(150, len(text.split())), # Max summary length
            "min_length": min(40, len(text.split()) // 4), # Min summary length (at least 1/4 of input or 40)
            "do_sample": False, # Use greedy decoding (or beam search if num_beams > 1)
            "num_beams": 4 # Using beam search often produces better summaries
        }

        # Run the summarization pipeline
        result = summarizer(text, **summary_params)
        
        # The result is typically a list of dicts: [{'summary_text': '...'}]
        summary = result[0]['summary_text']
        
        return jsonify({"summary": summary})

    except Exception as e:
        print(f"Error during summarization: {e}")
        return jsonify({"error": "An error occurred during summarization."}), 500


# 3. Run the application
if __name__ == '__main__':
    # Use environment variable for port, default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Setting debug=True is useful during development
    app.run(debug=True, host='0.0.0.0', port=port)