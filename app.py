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
   title = post["title"]
   date = post["date"]
   description = post["description"]
   entry = Entry(date, title,description)
   new_entry = entry.create_diary()
   if new_entry:
        return jsonify({"message" : "successful", "entry": new_entry }) , 201      
   return jsonify({"message" : "naah"})
@app.route('/api/v1/entries/<int:id>', methods=['DELETE'])
def delete_entries(id):
    entry = [entry for entry in content if entry['id'] == id ]
    content.remove(entry[0])
    return jsonify({'result': "Entry successfully deleted"})

@app.route('/api/v1/entries/<int:id>',methods=["GET"])
def get_each_entry(id):
     entry = [entry for entry in content if entry['id'] == id]
     return jsonify({'results': entry})

@app.route('/api/v1/entries/<int:id>', methods=['PUT'])
def put_entry(id):
    entry = [entry for entry in content if entry['id'] == id][0]
    titleResults = request.get_json()['title']
    descriptionResults=request.get_json()["description"]
    entry['title'] = titleResults
    entry["description"]=descriptionResults
    return jsonify({ "message" : "entry modified successfully" }), 200

if __name__ == '__main__':
    app.run(debug=True)