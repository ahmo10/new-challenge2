from flask import Flask,jsonify, request
from flask_restplus import reqparse
from models import Entry, content
app = Flask(__name__)

@app.route('/api/v1/entries', methods=['GET'])
def get_entries():
    return jsonify({'Entries':content})

#route post
@app.route('/api/v1/entries', methods=['POST'])
def create_entries():
   post =  request.get_json()
   title = post["Title"]
   date = post["Date"]
   descr = post["Description"]
   entry = Entry(date, title,descr)
   if entry.create_diary():
        return jsonify({"message" : "successful", "entry": entry.create_diary() }) , 201      
   return jsonify({"message" : "naah"})
@app.route('/api/v1/entries/<string:title>', methods=['DELETE'])
def delete_entries(title):
    entry = [entry for entry in content if entry['Title'] == title ]
    content.remove(entry[0])
    return jsonify({'result': "Entry successfully deleted"})

@app.route('/api/v1/entries/<int:id>',methods=["GET"])
def get_each_entry(id):
     entry = [entry for entry in content if entry['id'] == id]
     return jsonify({'results': entry})

if __name__ == '__main__':
    app.run(debug=True)