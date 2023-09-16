from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/") 
@app.route("/index")
def start():
    return redirect("/menu", code=302)
@app.route("/lab1")
def lab1():
        return """
<!doctype html>
<html>
    <head>
        <title>Ларионов Даниил Сергеевич, Лаб1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная 1
        </header>

        <h1>Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности</h1>
        <a href="/menu">Меню</a>


        <footer>
            &copy; Даниил Ларионов, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
"""
@app.route("/menu")
def menu():
      return """
<!doctype html>
<html>
    <head>
        <title>Ларионов Даниил Сергеевич, Лаб1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <h1><a href="http://127.0.0.1:5000/lab1">Первая лабораторная</a></h1>

        <footer>
            &copy; Даниил Ларионов, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
"""
@app.route('/lab1/oak')
def oak():
      return '''
<!doctype html>
<html>
    <body>
        <h1>Дуб</h1>
        <img src="''' +url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''
@app.route("/lab1/student")
def student():
      return f'''
<!doctype html>
<html>
    <head>
        <title>Ларионов Даниил Сергеевич, Лаб1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная 1
        </header>

        <h1>НГТУ</h1>
        <img src="{url_for('static', filename='NSTU.jpg')}">

        <footer>
            &copy; Даниил Ларионов, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
'''
@app.route("/lab1/python")
def python():
    return '''
<!doctype html>
<html>
    <head>
        <title>Ларионов Даниил Сергеевич ПИТООООООН, Лаб1</title>
    </head>
    <body>
        <header>
            Python — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью, ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ.
        </header>
        <h1>НГТУ</h1>
    </body>
</html>
'''
@app.route("/lab1/page1")
def studenttt():
      return f'''
<!doctype html>
<html>
    <head>
        <title>Ларионов Даниил Сергеевич Страничка, Лаб1</title>
    </head>
    <body>
    <header>
            В апреле 1992 года Новосибирский электротехнический институт успешно прошел государственную аттестацию и решением Министерства науки, высшей школы и технической политики Российской Федерации был переименован в Новосибирский государственный технический университет (НГТУ).
        </header>
        <img src="{url_for('static', filename='NSTU.jpg')}">
        <footer>
            &copy; Даниил Ларионов, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
'''
@app.route("/lab2/example")
def example():
      name = 'Даниил Ларионов'
      return render_template('example.html', name=name)
