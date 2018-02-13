# Songs

## System Specification
1. Ubuntu 16.04
2. Python 3.5.2 (using pymongo and flask_pymongo packages)
3. MongoDB 3.6.2

## File Description
* **constants.py** - contains definitions used by other scripts.
* **populatedb.py** - cleans up MongoDB songs and ratings collections and loads the contents of the sample songs file into the songs collection.
* **songs.py** - exposes the songs REST API interfacing with MongoDB to perform its business.
* **songs.json** - contains sample song entries that get loaded by the populate script.

## REST API Summary
* [GET] **/songs**
  - returns the complete list of songs.
* [GET] **/songs/avg/difficulty<?level=n>**
  - returns the average difficulty for all songs (optionally filtered by level 'n').
* [GET] **/songs/search<?message=m>**
  - returns a list of songs where their artists and/or title match (case insensitive) the optional message 'm'.
* [POST] **/songs/rating?song_id=id&rating=r**
  - adds a rating 'r' to the song with identifier 'id' (rating being an integer between 1 and 5).
* [GET] **/songs/avg/rating/<song_id>**
  - returns the average, the lowest and the highest rating of the song with identifier 'song_id'.

## How To Run It?
1. Assuming MongoDB to be running locally at the default port (otherwise **contants.py** needs to be changed accordingly).
2. Execute **prompt> python populatedb.py** so sample songs are loaded in MongoDB.
3. Execute **prompt> python songs.py** to start up the web server locally on port 5000.
4. Use a REST client like Postman (or even Curl directly in the command line) to perform calls to the exposed API.

## Sample Calls And Results
curl -X GET "http://localhost:5000/songs/avg/difficulty"
```json
{
  "result": {
    "average_difficulty": 10.323636363636364
  }
}
```

curl -X GET "http://localhost:5000/songs/avg/difficulty?level=13"
```json
{
  "result": {
    "average_difficulty": 14.096
  }
}
```

curl -X POST "http://localhost:5000/songs/rating?song_id=5a82d78a962d741740b42bcb&rating=5"
```json
{
  "result": {
    "rating_id": "5a831f87962d742148f7ad43"
  }
}
```

curl -X GET "http://locahost:5000/songs/avg/rating/5a82d78a962d741740b42bcb"
```json
{
    "result": {
        "average_rating": 4.5,
        "max_rating": 5,
        "min_rating": 3
    }
}
```

curl -X GET "http://localhost:5000/songs/search?message=ki"
```json
{
    "result": [
        {
            "artist": "Mr Fastfinger",
            "difficulty": 15,
            "level": 13,
            "released": "2012-05-11",
            "song_id": "5a82d78a962d741740b42bc3",
            "title": "Awaki-Waki"
        },
        {
            "artist": "The Yousicians",
            "difficulty": 14.66,
            "level": 13,
            "released": "2013-04-27",
            "song_id": "5a82d78a962d741740b42bc6",
            "title": "Opa Opa Ta Bouzoukia"
        },
        {
            "artist": "The Yousicians",
            "difficulty": 9,
            "level": 9,
            "released": "2016-05-01",
            "song_id": "5a82d78a962d741740b42bc9",
            "title": "Can't Buy Me Skills"
        }
    ]
}
```

curl -X GET "http://localhost:5000/songs"
```json
{
    "result": [
    {
      "artist": "The Yousicians",
      "difficulty": 14.6,
      "level": 13,
      "released": "2016-10-26",
      "song_id": "5a82d78a962d741740b42bc1",
      "title": "Lycanthropic Metamorphosis"
    },
    {
      "artist": "The Yousicians",
      "difficulty": 9.1,
      "level": 9,
      "released": "2010-02-03",
      "song_id": "5a82d78a962d741740b42bc2",
      "title": "A New Kennel"
    },
    {
      "artist": "Mr Fastfinger",
      "difficulty": 15,
      "level": 13,
      "released": "2012-05-11",
      "song_id": "5a82d78a962d741740b42bc3",
      "title": "Awaki-Waki"
    },
    {
      "artist": "The Yousicians",
      "difficulty": 13.22,
      "level": 13,
      "released": "2014-12-20",
      "song_id": "5a82d78a962d741740b42bc4",
      "title": "You've Got The Power"
    },
    {
      "artist": "The Yousicians",
      "difficulty": 10.98,
      "level": 9,
      "released": "2016-01-01",
      "song_id": "5a82d78a962d741740b42bc5",
      "title": "Wishing In The Night"
    },
    {
      "artist": "The Yousicians",
      "difficulty": 14.66,
      "level": 13,
      "released": "2013-04-27",
      "song_id": "5a82d78a962d741740b42bc6",
      "title": "Opa Opa Ta Bouzoukia"
    },
    {
      "artist": "The Yousicians",
      "difficulty": 2,
      "level": 3,
      "released": "2016-03-01",
      "song_id": "5a82d78a962d741740b42bc7",
      "title": "Greasy Fingers - boss level"
    },
    {
      "artist": "The Yousicians",
      "difficulty": 5,
      "level": 6,
      "released": "2016-04-01",
      "song_id": "5a82d78a962d741740b42bc8",
      "title": "Alabama Sunrise"
    },
    {
      "artist": "The Yousicians",
      "difficulty": 9,
      "level": 9,
      "released": "2016-05-01",
      "song_id": "5a82d78a962d741740b42bc9",
      "title": "Can't Buy Me Skills"
    },
    {
      "artist": "The Yousicians",
      "difficulty": 13,
      "level": 13,
      "released": "2016-06-01",
      "song_id": "5a82d78a962d741740b42bca",
      "title": "Vivaldi Allegro Mashup"
    },
    {
      "artist": "The Yousicians",
      "difficulty": 7,
      "level": 6,
      "released": "2016-07-01",
      "song_id": "5a82d78a962d741740b42bcb",
      "title": "Babysitting"
    }
  ]
}
```
