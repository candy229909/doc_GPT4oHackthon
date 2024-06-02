from flask import Flask, request, jsonify, send_file
import os
import requests
import uuid
from prompt import apply_modifications

app = Flask(__name__)

# 这里假设你有OpenAI API的密钥
OPENAI_API_KEY = 'your_openai_api_key'

# 设置上传文件保存的目录
UPLOAD_FOLDER = 'uploads'
MODIFIED_FOLDER = 'modified'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(MODIFIED_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MODIFIED_FOLDER'] = MODIFIED_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  

def get_openai_response(prompt):
    url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'prompt': prompt,
        'max_tokens': 1500,  # 根据需要调整
        'n': 1,
        'stop': None,
        'temperature': 0.2
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@app.route('/api/generate', methods=['POST'])
def generate():
    """
    Correct sentence postback based on selected work.
    Expected JSON format: { "work": ["structure", "child"], "content": "article" }
    Returns JSON: { "openai_response": "modified_article" }
    """
    data = request.get_json()
    modified_article = apply_modifications(data)

    # 从OpenAI获取响应
    openai_response = get_openai_response(modified_article)
    openai_text = openai_response['choices'][0]['text']

    return jsonify({'openai_response': openai_text})

@app.route('/api/enter', methods=['POST'])
def enter():
    """
    Revise format after enter with choose format.
    Expected JSON format: { format:format_name, sentence: upto 1500 words (with above sentence is better) }
    Returns JSON: { "openai_response": "modified_article" }
    """
    data = request.get_json()
    modified_article = apply_modifications(data)

    # 从OpenAI获取响应
    openai_response = get_openai_response(modified_article)
    openai_text = openai_response['choices'][0]['text']

    return jsonify({'openai_response': openai_text})

@app.route('/api/get', methods=['POST'])
def api_get():
    """
    Get format name.
    Expected: upload file, format name
    Returns JSON: { "openai_response": "modified_article" }
    """
    # 读取文件
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected for uploading"}), 400

    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()

    # 获取prompt
    prompt = request.form.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    # 从OpenAI获取响应
    openai_response = get_openai_response(file_content + "\n\n" + prompt)
    openai_text = openai_response['choices'][0]['text']

    return jsonify({'openai_response': openai_text})

if __name__ == '__main__':
    app.run(debug=True)
