from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main_page.html')


@app.route('/arcana')
def arcana():
    return render_template('arcana.html')


if __name__ == '__main__':
    app.run(debug=True)