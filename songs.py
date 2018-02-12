# songs.py

from constants import Const

from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = Const.SONGS_DB

mongo = PyMongo(app)

def get_songs_collection():
    return mongo.db[Const.SONGS_COLLECTION]


def perform_search_songs(filter):
    output = []
    for song in get_songs_collection().find(filter):
      song_id = str(song.pop('_id'))
      song['song_id'] = song_id
      output.append(song)
    return jsonify({'result': output})


@app.route('/songs', methods=['GET'])
def get_all_songs():
    filter = {}
    return perform_search_songs(filter)


@app.route('/songs/search', methods=['GET'])
def search_songs():
    message = request.args.get('message')
    if message is not None:
        filter = {'$or': [
            {'artist': {'$regex': message , '$options': 'i'}},
            {'title': {'$regex': message , '$options': 'i'}}
        ]}
        return perform_search_songs(filter)
    return jsonify({'result': []})


@app.route('/songs/avg/difficulty', methods=['GET'])
def get_avg_difficulty():
    aggregate_expression = []
    level = request.args.get('level')
    if level is not None:
        aggregate_expression.append({'$match': {'level': int(level)}})
    aggregate_expression.append({'$group': {'_id': 'null', 'average': {'$avg': '$difficulty'}}})

    result = list(get_songs_collection().aggregate(aggregate_expression))
    output = {'average_difficulty': result[0]['average'] if len(result) > 0 else -1}
    return jsonify({'result': output})


@app.route('/songs/rating', methods=['POST'])
def add_song_rating():
    return jsonify({'result': 'wip'})


@app.route('/songs/avg/rating/', methods=['GET'])
def get_avg_rating(song_id):
    print(song_id)
    return jsonify({'result': 'wip'})


@app.route('/songs', methods=['PUT'])
def add_song():
    song_id = get_songs_collection().insert(request.json)
    output = {'song_id': str(song_id)}
    return jsonify({'result': output})


if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)
