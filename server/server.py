from datetime import datetime
from flask import *

app = Flask(__name__)
msg = []
with open('messages.json', 'r') as f:
    msg = json.load(f)
@app.route('/getUsers')
def getUsers():
    return {"status": "ok", "message":"Server is working."}
@app.route('/getMessages')
def getMessages():
    return json.jsonify(msg)
@app.route('/getMessages', methods=['POST'])
def sendMessage():
    message_author = request.form['author']
    message_content = request.form['message']
    if message_content == "":
        return { "status": "no", "message":"Empty message"}
    if message_author == "":
        return { "status": "no", "message": "Empty name"}
    msg.append({
        'author': message_author,
        'message': message_content,
        'time': datetime.now()
    })
    with open('messages.json', 'w') as f:
        json.dump(msg, f)
    return { "status": "ok", "message":"Message sent!"}
app.run(debug=True, port=8300)