#!flask/bin/python
from flask import Flask, jsonify, request, Response, abort
import transmissionrpc, json
tc = transmissionrpc.Client('localhost', port=9091)

app = Flask(__name__)

@app.route('/')
def index():
    return "Active"

@app.route('/get_torrents', methods=['GET'])
def get_torrents():
    torrents = tc.get_torrents()

    tors = []
    for t in torrents:
        tors.append({
            'id': t.id,
            'name': t.name,
            'hashString': t.hashString,
            'status': t.status,
            'comment': t.comment,
            'torrent': 'http://10.0.1.77/' + t.name
            })

    if len(torrents) == 0:
        return jsonify({'torrents': 0})
    else:
        return Response(json.dumps(tors), mimetype='application/json')

@app.route('/torrent/add', methods=['POST'])
def add_torrent():
    if not request.json or not 'torrent' in request.json:
        abort(400)
    # torrent = torrent urlj
    tor = tc.add_torrent(request.json['torrent'])
    return jsonify(tor), 201

@app.route('/torrent/remove', methods=['POST'])
def remove_torrent():
    if not request.json or not 'torrent' in request.json:
        abort(400)
    # torrent = torrent ID or hash
    tc.stop_torrent(request.json['torrent'])
    tor = tc.remove_torrent(request.json['torrent'])
    request.json(tor), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
