from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index/index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre/sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato/contato.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)