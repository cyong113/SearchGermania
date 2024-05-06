import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

def load_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return None

def find_sentences_containing_word(text, word):
    sentences = sent_tokenize(text, language='english')
    return [sentence for sentence in sentences if word.lower() in sentence.lower()]
