
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,request

global flag
global question
global answer

flag=False

app=Flask(__name__)

@app.route('/')
def index():
    return "this is my Amelia home page -- 2"

@app.route('/checkStatus')
def checkStatus():
    global flag
    return str(flag)

@app.route('/askQuestion',methods=['GET', 'POST'])
def askQuestion():
    global flag
    global question
    flag=True
    question = request.values.get('query', None)

    return "use answer end point to check answer"

@app.route('/getQuery')
def getQuery():
    global question
    return question

@app.route('/postAnswer',methods=['GET', 'POST'])
def postAnswer():
    global flag
    global question
    global answer
    flag=False
    answer = request.values.get('answer', None)

    return answer

@app.route('/getAnswer')
def getAnswer():
    global answer
    return answer


if __name__ == "__main__":
    app.run(debug=True)

