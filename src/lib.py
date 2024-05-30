from collections import defaultdict

from song import Song

def kSongs(tracks: list[Song], k: int):
    songs = defaultdict(float)
    for track in tracks:
        songs[(track.name, track.artist)] += msToMin(track.duration)

    songs = sorted(songs.items(), key=lambda item: item[1], reverse=True)
    data = []
    for i in range(0, k):
        data.append({"key": (songs[i][0][0] + " by " + songs[i][0][1]), "total": songs[i][1]})

    return data


def kArtists(tracks: list[Song], k: int):
    artists = defaultdict(float)
    for track in tracks:
        artists[track.artist] += msToMin(track.duration)

    artists = sorted(artists.items(), key=lambda item: item[1], reverse=True)
    data = []
    for i in range(0, k):
        data.append({"key": artists[i][0], "total": artists[i][1]})

    return data


def kHours(tracks: list[Song], k: int):
    hours = defaultdict(float)
    for track in tracks:
        hours[track.endTime.hour] += msToMin(track.duration)

    hours = sorted(hours.items(), key=lambda item: item[1], reverse=True)
    data = []
    for i in range(0, k):
        data.append({"key": hours[i][0], "total": hours[i][1]})

    return data


def kMonths(tracks: list[Song], k: int):
    months = defaultdict(float)
    for track in tracks:
        months[track.endTime.month] += msToMin(track.duration)

    months = sorted(months.items(), key=lambda item: item[1], reverse=True)
    data = []
    for i in range(0, k):
        data.append({"key": months[i][0], "total": months[i][1]})

    return data


def streakSong(tracks: list[Song], k: int):
    songs = defaultdict(int)
    i, streak = 0, 1
    while i < len(tracks) - 1:
        while i < len(tracks) - 1 and \
              sameSong(tracks[i], tracks[i + 1]) and \
              not skip(tracks[i]) and \
              not skip(tracks[i + 1]):
            streak += 1
            i += 1

        songTup = (tracks[i].name, tracks[i].artist)
        songs[songTup] = max(streak, songs[songTup])

        streak = 1
        i += 1

    streaks = sorted(songs.items(), key=lambda item: item[1], reverse=True)
    data = []
    for i in range(0, k):
        data.append({"key": (streaks[i][0][0] + " by " + streaks[i][0][1]), "total": streaks[i][1]})

    return data


def streakArtist(tracks: list[Song], k: int):
    artists = defaultdict(int)
    i, streak = 0, 1
    while i < len(tracks) - 1:
        while i < len(tracks) - 1 and \
              tracks[i].artist == tracks[i + 1].artist and \
              not skip(tracks[i]) and \
              not skip(tracks[i + 1]):
            streak += 1
            i += 1

        artists[tracks[i].artist] = max(streak, artists[tracks[i].artist])

        streak = 1
        i += 1

    streaks = sorted(artists.items(), key=lambda item: item[1], reverse=True)
    data = []
    for i in range(0, k):
        data.append({"key": streaks[i][0], "total": streaks[i][1]})

    return data


def skipSong(tracks: list[Song], k: int):   
    songs = defaultdict(int)
    for track in tracks:
        if skip(track):
            songs[(track.name, track.artist)] += 1

    skips = sorted(songs.items(), key=lambda item: item[1], reverse=True)
    data = []
    for i in range(0, k):
        data.append({"key": (skips[i][0][0] + " by " + skips[i][0][1]), "total": skips[i][1]})

    return data


def skipArtist(tracks: list[Song], k: int):   
    artists = defaultdict(int)
    for track in tracks:
        if skip(track):
            artists[track.artist] += 1

    skips = sorted(artists.items(), key=lambda item: item[1], reverse=True)
    data = []
    for i in range(0, k):
        data.append({"key": skips[i][0], "total": skips[i][1]})

    return data


# UTILS
def msToMin(ms: int) -> int:
    return int(ms / 1000 / 60)


def sameSong(s1: Song, s2: Song) -> bool:
    return s1.name == s2.name and s1.artist == s2.artist


def skip(s: Song) -> bool:
    return s.duration <= 10000
