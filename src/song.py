import datetime
import re

class Song:
    def __init__(self, name, duration, endTime, artist):
        self.name = name
        self.duration = int(duration)
        self.artist = artist

        if s := re.match(r'(\d\d\d\d)-(\d\d)-(\d\d) (\d\d):(\d\d)', endTime):
            self.endTime = datetime.datetime(*map(int, [s.group(i) for i in range(1, 6)]))


    def __str__(self):
        return "Name: %s, Artist: %s, duration %d, end time: %s" % \
            (self.name, self.artist, self.duration, str(self.endTime))
