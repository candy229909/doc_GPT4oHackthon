from flask import Flask, request, jsonify
import os
import requests
from prompt import apply_modifications
app = Flask(__name__)

# Set up the OpenAI API key
OPENAI_API_KEY = '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'

# Set up directories for uploaded and modified files
UPLOAD_FOLDER = 'uploads'
MODIFIED_FOLDER = 'modified'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(MODIFIED_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MODIFIED_FOLDER'] = MODIFIED_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB upload file size limit

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx'}

def get_openai_response(prompt):
    baseURL: 'https://integrate.api.nvidia.com/v1',
    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'prompt': prompt,
        'max_tokens': 1500,
        'n': 1,
        'stop': None,
        'temperature': 0.2
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api', methods=['POST'])
def api():
    return 'API running'

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()
    modified_article = apply_modifications(data)

    # Get response from OpenAI
    openai_response = get_openai_response(modified_article)
    openai_text = openai_response['choices'][0]['text']

    return jsonify({'openai_response': openai_text})

@app.route('/api/get', methods=['POST'])
def api_get():
    if 'file' not in request.files or 'format_name' not in request.form:
        return jsonify({"error": "Missing file or format name"}), 400

    file = request.files['file']
    format_name = request.form['format_name']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        with open(file_path, 'r') as f:
            file_content = f.read()

        prompt = f"Format the following text using the '{format_name}' format:\n{file_content}"
        openai_response = get_openai_response(prompt)
        modified_article = openai_response.get('choices', [{}])[0].get('text', '')

        os.remove(file_path)

        return jsonify({"openai_response": modified_article})

    return jsonify({"error": "Invalid file type"}), 400

@app.route('/api/enter', methods=['POST'])
def enter():
    data = request.get_json()

    if not data or 'format' not in data or 'sentence' not in data:
        return jsonify({"error": "Missing format or sentence"}), 400

    format_name = data['format']
    sentence = data['sentence']

    if len(sentence.split()) > 1500:
        return jsonify({"error": "Sentence exceeds 1500 words"}), 400

    prompt = f"Revise the following sentence using the '{format_name}' format:\n{sentence}"
    openai_response = get_openai_response(prompt)
    modified_article = openai_response.get('choices', [{}])[0].get('text', '')

    return jsonify({"openai_response": modified_article})

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
