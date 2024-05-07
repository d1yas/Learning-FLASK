from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Test"

@app.route('/admin')
def admin_page():
    return "ADMIN SITE"


if __name__ == "__main__":
    app.run(debug=True)
