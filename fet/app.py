from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    # flask does all the work to turn this string into an appropriate http response
    return 'Hello Flask!'


@app.route('/hello_get')
def hello_get():
    myint = request.args['myint']
    return jsonify({'myint': int(myint)})


@app.route('/hello_post', methods=['POST'])
def hello_post():
    code = int(request.form['code'])
    return jsonify({'code squared': int(code*code)})

