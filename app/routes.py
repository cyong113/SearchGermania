from flask import Blueprint, render_template, request
from .utilities.text_utils import load_text, find_sentences_containing_word

# Create a Blueprint for the main routes
main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    word = request.args.get('word', '')
    sentences = []
    if word:
        text = load_text('Germania.txt')
        sentences = find_sentences_containing_word(text, word)
    return render_template('index.html', sentences=sentences, word=word)

@main.route('/tribes')
def tribes():
    return render_template('tribes.html')
