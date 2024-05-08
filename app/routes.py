from flask import Blueprint, render_template, request, session, redirect, url_for
from .utilities.text_utils import load_text, find_sentences_containing_word

main = Blueprint('main', __name__)

text = load_text('Germania.txt')

quiz_questions = [
    {"question": "Who wrote 'Germania'?", "choices": ["Tacitus", "Pliny", "Caesar"], "answer": "Tacitus"},
    {"question": "What year was 'Germania' written?", "choices": ["98 AD", "150 AD", "200 AD"], "answer": "98 AD"},
    {"question": "What rivers separate Germany from Gaul, Rhoetia, and Pannonia?", "choices": ["Danube and Rhone", "Rhine and Danube", "Elbe and Rhine"], "answer": "Rhine and Danube"},
    {"question": "From which mountains does the Rhine river rise?", "choices": ["Black Forest", "Vosges Mountains", "Rhoetian Alps"], "answer": "Rhoetian Alps"},
    {"question": "What ocean does the Rhine flow into?", "choices": ["Baltic Sea", "Black Sea", "North Sea"], "answer": "North Sea"},
    {"question": "Who are considered the fathers and founders of the German nation according to their ancient ballads?", "choices": ["Tuisto and Mannus", "Odin and Thor", "Romulus and Remus"], "answer": "Tuisto and Mannus"},
    {"question": "Which group of people is said to have expelled the Gauls and initially been called 'Germans'?", "choices": ["Tungrians", "Teutons", "Visigoths"], "answer": "Tungrians"},
    {"question": "What is said to ennoble the Langobards according to the text?", "choices": ["Their large population and wealth", "Their numerous peaceful negotiations with the northern tribes", "The smallness of their number and their prowess in battle"], "answer": "The smallness of their number and their prowess in battle"},
    {"question": "How do the Sarmatians differ from the Germans according to the text?", "choices": ["The Sarmatians use large and flowing vests, unlike the closely girt vests of the Germans", "The Sarmatians are primarily foot soldiers, unlike the mounted Germans", "The Sarmatians use large and flowing vests, unlike the closely girt vests of the Germans"], "answer": "The Sarmatians use large and flowing vests, unlike the closely girt vests of the Germans"},
    {"question": "Which deity is most worshipped by the ancient Germans?", "choices": ["Mercury", "Jupiter", "Mars"], "answer": "Mercury"}
]

leaderboard = []

@main.route('/quiz')
def quiz():
    return render_template('quiz.html', questions=quiz_questions)

@main.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    nickname = request.form['nickname']
    score = 0
    for i in range(1, len(quiz_questions) + 1):
        user_answer = request.form.get(f'answer{i}')
        correct_answer = quiz_questions[i-1]['answer']
        if user_answer == correct_answer:
            score += 1
    # Add score to leaderboard (or use a database to save scores)
    leaderboard.append((nickname, score))
    leaderboard.sort(key=lambda x: x[1], reverse=True)
    # Store score in session or pass directly to template
    session['nickname'] = nickname
    session['score'] = score
    return redirect(url_for('main.quiz_results'))


@main.route('/quiz_results')
def quiz_results():
    # Retrieve score from session if not passing directly
    nickname = session.get('nickname', 'Unknown')
    score = session.get('score', 0)
    return render_template('quiz_results.html', nickname=nickname, score=score, leaderboard=leaderboard)


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
