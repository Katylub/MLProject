from flask import Flask, request, render_template,jsonify
from model import prev
import numpy as np

app = Flask(__name__)
def do_something(text1,text2):
   text1 = text1.upper()
   text2 = text2.upper()
   combine = text1 + text2
   return combine
@app.route('/')
def home():
  return app.send_static_file('home.html')
@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = float(request.form['text1'])
    word = request.args.get('text1')
    combine = prev(text1)
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
if __name__ == '__main__':
    app.run(debug=True)