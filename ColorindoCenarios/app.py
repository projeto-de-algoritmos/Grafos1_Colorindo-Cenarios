from flask import Flask, render_template
from matrix import matrix

app = Flask(__name__)

@app.route('/')
def single_page_app():
    return render_template('index.html', matrix=matrix())

if __name__ == "__main__":
    app.run(debug=True)