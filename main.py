from flask import Flask, request
from ceasar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
       <form method="post">
       <label for="rotation">Rotate by:</label>
       <input id="rotation_amount" type="text" value=0 name="rot" />
       <textarea rows="4" cols="50" name="text">
       </textarea>
       <input type="submit" value="Submit"/> 
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])

def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    answer = rotate_string (text, rot)
    ret_string = "<h1>" + answer + "</h1>"
    return ret_string

app.run()