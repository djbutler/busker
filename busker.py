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

LOGFILE = '~/Dropbox/projects/busker/donations.log'
GIFT_AMOUNT = 1

# to create OSX notifications
def notify(title, subtitle, message, image, url, execute):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    c = '-contentImage {!r}'.format(image)
    u = '-open {!r}'.format(url)
    e = '-execute %s' % execute
    cmd = 'terminal-notifier {}'.format(' '.join([m, t, s, c, u, e]))
    print(cmd)
    os.system(cmd)

track, artist, play_count = osascript(TRACK), osascript(ARTIST), osascript(PLAY_COUNT)

os.system("echo \'%s | %s | %s plays | asked $%d\' >> %s" % (artist, track, play_count, GIFT_AMOUNT, LOGFILE))
on_donate_cmd = "\"echo \'%s | %s | %s plays | gave \\$%d\' >> %s\"" % (artist, track, play_count, GIFT_AMOUNT, LOGFILE)
notify(title    = '%s | %s' % (track, artist),
       subtitle = 'You\'ve listened %s times' % play_count,
       message  = 'Click to send $%d to %s' % (GIFT_AMOUNT, artist),
       image = '/Users/djbutler/Desktop/robyn.png',
       url = 'https://venmo.com/?txn=pay&recipients=raffi.jaffe@gmail.com&amount=5&note=A+donation+from+Busker&audience=private',
       execute = on_donate_cmd)

# print("track: %s" % osascript(TRACK))
# print("play count: %s" % osascript(PLAY_COUNT))
# print("artist: %s" % osascript(ARTIST))
# print("album: %s" % osascript(ALBUM))
