from flask import Flask, url_for, abort, redirect, url_for, session

from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    return 'welcome'

#passing variables recieved from url to functions
@app.route('/helloworld/<username>')
def helloworld(username):
    return 'Hello World, %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/')
def index():
    return 'Index Page'

@app.route('/home')
def home():
    return redirect(url_for('welcome'))



with app.test_request_context():
    print(url_for('index'))
    print(url_for('welcome'))
    print(url_for('helloworld', username='Swaroop'))


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('pagenotfound.html'), 404

# In order to use sessions you have to set a secret key. Here is how sessions work
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = '1234  '

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('welcome'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)