# Text Summarization Web App

**Concise AI** – A web application that generates concise summaries from long text using state-of-the-art NLP models.

---

## 🚀 Features

- Summarizes articles, documents, or any long text.
- Built with **Flask** for the backend.
- Uses **Hugging Face Transformers** (`sshleifer/distilbart-cnn-12-6`) for summarization.
- Responsive UI designed with **Tailwind CSS**.
- Handles minimum text length checks for better summaries.

---

## 🛠 Installation

1. **Clone the repository**
```bash
git clone https://github.com/Bhakti-Ruparel/Text-Summarization.git
cd Text-Summarization
Create a virtual environment

bash
Copy code
python -m venv .nlp
Activate the environment

Windows:

bash
Copy code
.\.nlp\Scripts\activate
Mac/Linux:

bash
Copy code
source .nlp/bin/activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
⚡ Usage
Run the Flask app:

bash
Copy code
python app.py
Open your browser and go to:

cpp
Copy code
http://127.0.0.1:5000
Paste a long text and click Generate Summary.

💻 Technology Stack
Python

Flask – Backend web framework

Hugging Face Transformers – NLP summarization models

Tailwind CSS – Frontend styling

JavaScript (Fetch API) – Frontend interactions

📂 Project Structure
pgsql
Copy code
Text-Summarization/
├── app.py
├── templates/
│   └── index.html
├── static/  (if any CSS/JS files)
├── requirements.txt
└── README.md
📄 License
This project is open-source and free to use.

yaml
Copy code
