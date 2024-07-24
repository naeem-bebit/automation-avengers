from flask import Flask, render_template_string
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    Hello, World!
    <form action="/newpage">
        <input type="submit" value="Go to New Page" />
    </form>
    '''

@app.route('/newpage')
def new_page():
    return 'Welcome to the new page!'

if __name__ == '__main__':
    app.run()
