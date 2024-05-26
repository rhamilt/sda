# Reed Hamilton 2024
from datetime import datetime
import json
import os

from song import Song


def get_tracks(user: str, limit: bool) -> list[Song]:
    tracks = parse_streaming_history(user)

    tracks = list(filter(lambda x: x.name != "Unknown Track" or
                                   x.artist != "Unknown Artist", tracks))

    if limit:
        tracks = list(filter(lambda x: x.endTime.year == datetime.now().year, tracks))

    return tracks


def parse_streaming_history(user: str) -> list[Song]:
    songs = []
    i = 0
    file = os.path.join("data", user, "StreamingHistory_music_%d.json" % i)
    while os.path.exists(file):
        f = open(file)
        songs += list(map(convert_json_to_song, json.load(f)))
        f.close()

        i += 1
        file = os.path.join("data", user, "StreamingHistory_music_%d.json" % i)

    return songs


def convert_json_to_song(json: dict) -> Song:
    return Song(name=json["trackName"], duration=json["msPlayed"],
                endTime=json["endTime"], artist=json["artistName"])
