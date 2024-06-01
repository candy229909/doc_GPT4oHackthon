from flask import Flask, request, jsonify
import requests
from prompt import apply_modifications

app = Flask(__name__)

# 这里假设你有OpenAI API的密钥
OPENAI_API_KEY = 'your_openai_api_key'

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
    prompt = request.json.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    # 从OpenAI获取响应
    openai_response = get_openai_response(prompt)
    openai_text = openai_response['choices'][0]['text']

    return jsonify({'openai_response': openai_text})

@app.route('/api/enter', methods=['POST'])
def enter():
    data = request.get_json()
    modified_article = apply_modifications(data)

    # 从OpenAI获取响应
    openai_response = get_openai_response(modified_article)
    openai_text = openai_response['choices'][0]['text']

    return jsonify({'openai_response': openai_text})

@app.route('/api/get', methods=['POST'])
def api_get():
    prompt = request.json.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    # 从OpenAI获取响应
    openai_response = get_openai_response(prompt)
    openai_text = openai_response['choices'][0]['text']

    return jsonify({'openai_response': openai_text})

if __name__ == '__main__':
    app.run(debug=True)
