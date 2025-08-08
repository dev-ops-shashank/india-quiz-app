from flask import Flask, render_template, request, redirect, url_for, session
import secrets
from datetime import timedelta

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.permanent_session_lifetime = timedelta(minutes=30)

# Quiz questions about India
quiz_questions = [
    {
        'id': 1,
        'question': 'What is the capital of India?',
        'options': ['Mumbai', 'New Delhi', 'Kolkata', 'Chennai'],
        'answer': 'New Delhi'
    },
    {
        'id': 2,
        'question': 'Which is the national bird of India?',
        'options': ['Peacock', 'Parrot', 'Eagle', 'Sparrow'],
        'answer': 'Peacock'
    },
    {
        'id': 3,
        'question': 'Who is known as the Father of the Nation in India?',
        'options': ['Jawaharlal Nehru', 'Sardar Patel', 'Mahatma Gandhi', 'Subhas Chandra Bose'],
        'answer': 'Mahatma Gandhi'
    },
    {
        'id': 4,
        'question': 'Which is the longest river in India?',
        'options': ['Yamuna', 'Brahmaputra', 'Godavari', 'Ganga'],
        'answer': 'Ganga'
    },
    {
        'id': 5,
        'question': 'How many states are there in India?',
        'options': ['28', '29', '30', '27'],
        'answer': '28'
    },
    {
        'id': 6,
        'question': 'Which is the national flower of India?',
        'options': ['Rose', 'Lotus', 'Jasmine', 'Sunflower'],
        'answer': 'Lotus'
    },
    {
        'id': 7,
        'question': 'In which year did India gain independence?',
        'options': ['1945', '1946', '1947', '1948'],
        'answer': '1947'
    },
    {
        'id': 8,
        'question': 'Which is the smallest state in India by area?',
        'options': ['Goa', 'Sikkim', 'Tripura', 'Delhi'],
        'answer': 'Goa'
    },
    {
        'id': 9,
        'question': 'Who wrote the Indian National Anthem?',
        'options': ['Bankim Chandra', 'Rabindranath Tagore', 'Sarojini Naidu', 'Subramanya Bharathi'],
        'answer': 'Rabindranath Tagore'
    },
    {
        'id': 10,
        'question': 'Which is the highest mountain peak in India?',
        'options': ['K2', 'Nanda Devi', 'Kangchenjunga', 'Mount Everest'],
        'answer': 'Kangchenjunga'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_quiz():
    name = request.form.get('name')
    email = request.form.get('email')
    
    if not name or not email:
        return redirect(url_for('index'))
    
    session.permanent = True
    session['user_name'] = name
    session['user_email'] = email
    session['current_question'] = 0
    session['score'] = 0
    session['answers'] = []
    
    return redirect(url_for('quiz'))

@app.route('/quiz')
def quiz():
    if 'user_name' not in session:
        return redirect(url_for('index'))
    
    current_q = session.get('current_question', 0)
    
    if current_q >= len(quiz_questions):
        return redirect(url_for('result'))
    
    question = quiz_questions[current_q]
    return render_template('quiz.html', 
                         question=question, 
                         question_number=current_q + 1,
                         total_questions=len(quiz_questions),
                         user_name=session['user_name'])

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    if 'user_name' not in session:
        return redirect(url_for('index'))
    
    answer = request.form.get('answer')
    current_q = session.get('current_question', 0)
    
    if current_q < len(quiz_questions):
        correct_answer = quiz_questions[current_q]['answer']
        if answer == correct_answer:
            session['score'] = session.get('score', 0) + 1
        
        session['answers'].append({
            'question': quiz_questions[current_q]['question'],
            'user_answer': answer,
            'correct_answer': correct_answer,
            'is_correct': answer == correct_answer
        })
        
        session['current_question'] = current_q + 1
    
    return redirect(url_for('quiz'))

@app.route('/result')
def result():
    if 'user_name' not in session:
        return redirect(url_for('index'))
    
    score = session.get('score', 0)
    total = len(quiz_questions)
    percentage = (score / total) * 100
    
    return render_template('result.html',
                         user_name=session['user_name'],
                         score=score,
                         total=total,
                         percentage=percentage,
                         answers=session.get('answers', []))

@app.route('/restart')
def restart():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)