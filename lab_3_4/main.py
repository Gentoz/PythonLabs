from flask import Flask, render_template, request

app = Flask(__name__)

# Список вопросов
questions = [
    'Как вас зовут?',
    'Сколько вам лет?',
    'Какой у вас любимый цвет?'
]


# Обработчик главной страницы
@app.route('/')
def index():
    return render_template('index.html', questions=questions)


# Обработчик страницы с результатами
@app.route('/submit', methods=['POST'])
def submit():
    answers = []
    for question in questions:
        answer = request.form.get(question)
        answers.append(answer)
    with open('answers.txt', 'a', encoding="utf-8") as f:
        f.write(','.join(answers) + 'n')
    return render_template('submit.html', answers=answers)


if __name__ == '__main__':
    app.run(debug=True)
