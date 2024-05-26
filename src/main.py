import json
import os

from flask import jsonify, request

from config import app
import lib
from parse import get_tracks

@app.route("/<user>", methods=["GET"])
def get_user_data(user):
    tracks = []
    i = 0
    file = os.path.join("data", user, "StreamingHistory_music_%d.json" % i)
    print (file)
    while os.path.exists(file):
        f = open(file)
        tracks += json.load(f)
        f.close()

        i += 1
        file = os.path.join("data", user, "StreamingHistory_music_%d.json" % i)

    if i == 0:
        return jsonify({"message": "The user does not exist!"}), 404

    return jsonify({"tracks": tracks}), 404


@app.route("/<user>/topK", methods=["GET"])
def getTopK(user):
    if not os.path.exists(os.path.join("data", user)):
        return jsonify({"message": "The user does not exist!"}), 404

    if request.json:
        k = request.json.get("k")
        t = request.json.get("type")
        limit = request.json.get("limit")
    else:
        return jsonify({"message": "Improper request"}), 400

    tracks = get_tracks(user, limit)

    match t:
        case "songs":
            return jsonify(lib.kSongs(tracks, k)), 200
        case "artists":
            return jsonify(lib.kArtists(tracks, k)), 200
        case "hours":
            return jsonify(lib.kHours(tracks, k)), 200
        case "months":
            return jsonify(lib.kMonths(tracks, k)), 200
        case _:
            return jsonify({"message": "Improper request"}), 400


if __name__ == "__main__":
    app.run(debug=True)
