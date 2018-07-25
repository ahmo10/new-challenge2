from flask import Flask,jsonify, request

app = Flask(__name__)


#Dictionary to temporily store/hold diary entries
Entries = [
		{
		 	"id": 1,
            "date":12/12/2012,
			"title":"one",
			"body":"the world cup final on sunday"
		},
		{
			"id": 2,
            "date":12/12/2012,
			"title":"two",
			"body":"The world cup second runners up"
		},
		{
		 	"id": 3,
			"title":"three",
            "date":12/12/2012,
			"body":"world cup semi final"
		}

	]

#route getting every entries
@app.route('/api/v1/entries', methods=['GET'])
def get_entries():
    return jsonify({'Entries': Entries})

#route post
@app.route('/api/v1/entries', methods=['POST'])
def create_entries():

   date =  request.get_json(["datte"])
   entry = date
   Entries.append(entry)
   print(Entries)
   return jsonify({'Entries': Entries})
@app.route('/api/v1/entries/<int:id>', methods=['DELETE'])
def delete_entries(id):
    entry = [entry for entry in Entries if entry['id'] == id]
    del entry
    return jsonify({'result': "Entry successfully deleted"})

#get each entry
@app.route('/api/v1/entries/<int:id>',methods=["GET"])
def get_each_entry(id):
    entry = [entry for entry in Entries if entry['id'] == id]

    return jsonify({'results': entry})


if __name__ == '__main__':
    app.run(debug=True)