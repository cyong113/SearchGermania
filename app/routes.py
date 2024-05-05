from flask import Blueprint, render_template, request
from .utilities.text_utils import load_text, find_sentences_containing_word
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
# Create a Blueprint for the main routes
main = Blueprint('main', __name__)

def load_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return None
text = load_text('Germania.txt')

def find_sentences_containing_word(text, word):
    sentences = sent_tokenize(text, language='english')
    return [sentence for sentence in sentences if word.lower() in sentence.lower()]

@main.route('/tribes')
def tribes():
    return render_template('tribes.html')

@main.route('/search', methods=['GET'])
def search():
    word = request.args.get('word', '') 
    if text and word:
        sentences = find_sentences_containing_word(text, word)
    else:
        sentences = []
    return render_template('index.html', sentences=sentences, word=word)


@main.route('/', methods=['GET', 'POST'])
def home():
    word = ""
    if request.method == 'POST':
        word = request.form.get('word', '')
        if text and word:  
            sentences = find_sentences_containing_word(text, word)
            return render_template('index.html', sentences=sentences, word=word)
    return render_template('index.html', sentences=[], word=word)
