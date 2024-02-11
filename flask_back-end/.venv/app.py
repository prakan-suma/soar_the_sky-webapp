from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello back-end"

# run back-end
if __name__ == '__main__':
    app.run(debug=True)