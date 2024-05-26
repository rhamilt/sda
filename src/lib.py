from collections import defaultdict

from song import Song

def kSongs(tracks: list[Song], k: int):
    songs = defaultdict(float)
    for track in tracks:
        songs[(track.name, track.artist)] += msToMin(track.duration)

    songs = sorted(songs.items(), key=lambda item: item[1], reverse=True)
    data = defaultdict(list)
    for i in range(0, k):
        data["keys"].append(songs[i][0][0] + "*,*" + songs[i][0][1])
        data["totals"].append(songs[i][1])

    return data


def kArtists(tracks: list[Song], k: int):
    artists = defaultdict(float)
    for track in tracks:
        artists[track.artist] += msToMin(track.duration)

    artists = sorted(artists.items(), key=lambda item: item[1], reverse=True)
    data = defaultdict(list)
    for i in range(0, k):
        data["keys"].append(artists[i][0])
        data["totals"].append(artists[i][1])

    return data


def kHours(tracks: list[Song], k: int):
    hours = defaultdict(float)
    for track in tracks:
        hours[track.endTime.hour] += msToMin(track.duration)

    hours = sorted(hours.items(), key=lambda item: item[1], reverse=True)
    data = defaultdict(list)
    for i in range(0, k):
        data["keys"].append(hours[i][0])
        data["totals"].append(hours[i][1])

    return data


def kMonths(tracks: list[Song], k: int):
    months = defaultdict(float)
    for track in tracks:
        months[track.endTime.month] += msToMin(track.duration)

    months = sorted(months.items(), key=lambda item: item[1], reverse=True)
    data = defaultdict(list)
    for i in range(0, k):
        data["keys"].append(months[i][0])
        data["totals"].append(months[i][1])

    return data


# UTILS
def msToMin(ms: int) -> int:
    return int(ms / 1000 / 60)

