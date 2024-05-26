import os
import json

from flask import jsonify, request

from config import app

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


if __name__ == "__main__":
    app.run(debug=True)
