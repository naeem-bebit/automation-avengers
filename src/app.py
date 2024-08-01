from flask import Flask, render_template_string, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/newpage')
def new_page():
    return render_template("newpage.html")

if __name__ == '__main__':
    app.run()
