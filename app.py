from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/") 
@app.route("/index")
def start():
    return redirect("/menu", code=302)
@app.route("/lab2/example")
def example():
      num = '2'
      name = 'Даниил Ларионов'
      groupe = 'ФБИ-12'
      kurs = '3'
      return render_template('example.html', num=num, name=name, groupe=groupe, kurs=kurs )
