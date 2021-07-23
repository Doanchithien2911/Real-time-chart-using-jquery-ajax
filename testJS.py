from flask import Flask,render_template,url_for,request,jsonify,make_response
import random
from random import random
import json
from datetime import datetime
app = Flask(__name__,template_folder="template")


@app.route('/', methods=["GET"])
def main():
    return render_template('index.html')


@app.route('/data', methods=["GET","POST"])
def data():
    temperature=random()*100;
    humidity=random()*100;

    x = datetime.now()
    time=x.strftime("%X")
    data=[time,temperature,humidity]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return (response,200)



if __name__ == "__main__":
    app.run(debug=True)