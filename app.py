from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__)

# Initialize the translator
translator = Translator()

def translate_text(text, target_language='te'):
    translated = translator.translate(text, dest=target_language)
    return translated.text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text_to_translate = request.form['text']
    translated_text = translate_text(text_to_translate)
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)
