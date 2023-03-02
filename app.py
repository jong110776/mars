from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.inelwg0.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/mars", methods=["POST"])
def mars_post():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']


    doc = {
        'name':name_receive,
        'adress':address_receive,
        'size':size_receive
    }
    db.mars.insert_one(doc)


    return jsonify({'msg':'저장 완료'})


@app.route("/mars", methods=["GET"])
def mars_get():
    return jsonify({'msg':'GET 연결 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)