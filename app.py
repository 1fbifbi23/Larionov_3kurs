from flask import Flask, redirect
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