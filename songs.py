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

@app.route('/songs', methods=['GET'])
def get_songs():
    output = []
    for song in get_songs_collection().find():
      song_id = str(song.pop('_id'))
      song['song_id'] = song_id
      output.append(song)
    return jsonify({'result' : output})

@app.route('/song', methods=['PUT'])
def add_song():
    song_id = get_songs_collection().insert(request.json)
    output = {'song_id' : str(song_id)}
    return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
