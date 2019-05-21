from flask import Flask, request, redirect, render_template
import model
import json

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('createpost.html')

@app.route('/getpost/<username>')
def retrievePosts(username):
    return json.dumps(model.getPosts(username))

@app.route('/createpost', methods=['POST', 'GET'])
def createPost():
    if request.method == 'POST':
        post = request.form['pst']
        username = request.form['username']
        model.createPost(post, username)
        return "Success"
    return "Only Post method is allowed"



# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)



