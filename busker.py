#!/usr/bin/env python
import subprocess, os
from subprocess import PIPE

# to talk to music players like Spotify
def osascript(s):
    return subprocess.Popen("osascript -e '%s'" % s, shell=True, stdout=PIPE).stdout.read().strip()

PLAYER_POSITION = 'tell application "Spotify" to player position'
ARTWORK = 'tell application "Spotify" to artwork of current track'
PLAY_COUNT = 'tell application "Spotify" to played count of current track'
ARTIST = 'tell application "Spotify" to artist of current track'
TRACK = 'tell application "Spotify" to name of current track' 
ALBUM = 'tell application "Spotify" to album of current track'

# to create OSX notifications
def notify(title, subtitle, message, image, url):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    c = '-contentImage {!r}'.format(image)
    u = '-open {!r}'.format(url)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s, c, u])))

notify(title    = '%s | %s' % (osascript(TRACK), osascript(ARTIST)),
       subtitle = 'You\'ve listened %s times' % osascript(PLAY_COUNT),
       message  = 'Click to send $1 to %s' % osascript(ARTIST),
       image = '/Users/djbutler/Desktop/robyn.png',
       url = 'https://venmo.com/?txn=pay&recipients=raffi.jaffe@gmail.com&amount=5&note=A+donation+from+Busker&audience=private')

# print("track: %s" % osascript(TRACK))
# print("play count: %s" % osascript(PLAY_COUNT))
# print("artist: %s" % osascript(ARTIST))
# print("album: %s" % osascript(ALBUM))
