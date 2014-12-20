#!/usr/bin/env python
import os

# The notifier function
def notify(title, subtitle, message, image, url):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    c = '-contentImage {!r}'.format(image)
    u = '-open {!r}'.format(url)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s, c, u])))

# Calling the function
notify(title    = 'support this artist',
       subtitle = 'Robyn',
       message  = 'send $1 now',
       image = '/Users/djbutler/Desktop/robyn.png',
       url = 'https://venmo.com/?txn=pay&recipients=raffi.jaffe@gmail.com&amount=5&note=A+donation+from+Busker&audience=private')
