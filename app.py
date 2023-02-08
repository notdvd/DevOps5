from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/request', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_request():
    r = request.method
    if r == 'GET':
        return 'This is a GET request'
    elif r == 'POST':
        return 'This is a POST request'
    elif r == 'PUT':
        return 'This is a PUT request'
    elif r == 'DELETE':
        return 'This is a DELETE request'
    else:
        return 'This is an UNDEFINED request'

records = {
    1: {
        'name': 'John'
    },
    2: {
        'name': 'Jane'
    }
}

@app.route('/records/all', methods=['GET'])
def getRecords():
    return jsonify(records)

@app.route('/records/id=<id>', methods=['GET'])
def getRecordByID(id):
    id = int(id)
    if id in records:
        return jsonify(records[id])
    else:
        return "GET: Record {} does not exist".format(id)

@app.route('/records/create/name=<name>', methods=['PUT'])
def createRecord(name):
    id = len(records) + 1
    records.update({id: {"name": name}})
    return "Record added"

@app.route('/records/edit/id=<id>+name=<name>', methods=['PATCH'])
def updateRecord(id, name):
    id = int(id)
    if id in records:
        old_name = records[id]['name']
        if name != old_name:
            records[id]['name'] = name
            return "Name updated for record {}".format(id)
        else:
            return "PATCH: Cannot rename {} to the same name".format(id)
    else:
        return "PATCH: Record {} does not exist".format(id)

@app.route('/records/delete/id=<id>', methods=['DELETE'])
def deleteRecord(id):
    id = int(id)
    if id in records:
        del records[id]
        return "Record deleted"
    else:
        return "DELETE: Record {} does not exist".fomrat(id)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)