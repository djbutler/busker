#!/usr/bin/env python
import subprocess, os
from subprocess import PIPE
from math import log
from os.path import expanduser

# to talk to music players like Spotify
def osascript(s):
    return subprocess.Popen("/usr/bin/osascript -e '%s'" % s, shell=True, stdout=PIPE).stdout.read().strip()

PLAYER_STATE = 'tell application "Spotify" to player state'
PLAYER_POSITION = 'tell application "Spotify" to player position'
ARTWORK = 'tell application "Spotify" to artwork of current track'
PLAY_COUNT = 'tell application "Spotify" to played count of current track'
ARTIST = 'tell application "Spotify" to artist of current track'
TRACK = 'tell application "Spotify" to name of current track' 
ALBUM = 'tell application "Spotify" to album of current track'

LOGFILE = '/Users/djbutler/Dropbox/projects/busker/donations.log'
NOTIFIER = '/Applications/terminal-notifier.app/Contents/MacOS/terminal-notifier'
GIFT_AMOUNT = 1

# to create OSX notifications
def notify(title, subtitle, message, image, url, execute):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    c = '-contentImage {!r}'.format(image)
    u = '-open {!r}'.format(url)
    e = '-execute %s' % execute
    cmd = NOTIFIER + ' {}'.format(' '.join([m, t, s, c, u, e]))
    print(cmd)
    os.system(cmd)

def create_notification(track, artist, play_count):
    track, artist, play_count = osascript(TRACK), osascript(ARTIST), osascript(PLAY_COUNT)
    os.system("echo \'%s | %s | %s plays | asked $%d\' >> %s" % (artist, track, play_count, GIFT_AMOUNT, LOGFILE))
    on_donate_cmd = "\"echo \'%s | %s | %s plays | gave \\$%d\' >> %s\"" % (artist, track, play_count, GIFT_AMOUNT, LOGFILE)
    notify(title    = '%s | %s' % (track, artist),
           subtitle = 'You\'ve listened %s times' % play_count,
           message  = 'Click to send $%d to %s' % (GIFT_AMOUNT, artist),
           image = '/Users/djbutler/Desktop/robyn.png',
           url = 'https://venmo.com/?txn=pay&recipients=raffi.jaffe@gmail.com&amount=5&note=A+donation+from+Busker&audience=private',
           execute = on_donate_cmd)

IS_PLAYING_CMD = \
"""tell application \"System Events\"
  set myList to (name of every process)
end tell
myList contains \"%s\""""
def is_playing(app):
    return osascript(IS_PLAYING_CMD % app)

MIN_PLAYS = 2
if __name__ == "__main__":
    if bool(is_playing("Spotify")) and osascript(PLAYER_STATE) == 'playing':
        play_count = int(osascript(PLAY_COUNT))
        for line in open(expanduser(LOGFILE)):
            pass
        if play_count >= MIN_PLAYS and log(play_count,2) % 1 == 0.0:
            track, artist = osascript(TRACK), osascript(ARTIST)
            if len(line) < len(artist) or line[0:len(artist)] != artist:
                create_notification(track, artist, play_count)
            
