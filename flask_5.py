from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdgfgdgfdhghgshgdgdhg7424dhsdjkh'

menu = [{"name":"Установка", "url":"install-flask"},
        {"name":"Первое приложение", "url":"first-app"},
        {"name":"Обратная связь", "url":"contact"}]

@app.route("/")
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)

@app.route("/about")
def about():
    print( url_for('about'))
    return render_template('about.html', title="О сайте", menu=menu)

@app.route("/contact", methods=["POST", "GET"]) # Обработчик данных поступивших из формы
def contact():

    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')
        print(request.form)

    return render_template('contact.html', title="Обратная связь", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)