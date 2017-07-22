from sys import argv
from time import sleep
from plexapi.server import PlexServer

print('arvg', argv)
url = argv[1]
token = argv[2]
section_title = argv[3]
playlist_title = argv[4]
item_title = argv[5]

print('url', url)
print('token', token)
print('section_title', section_title)
print('playlist_title', playlist_title)
print('item_title', item_title)


def cb(data):
    if 'StatusNotification' and data['size'] == 1:
        status = data[u'StatusNotification'][0]
        if 'title' in status and status['title'] == 'Library scan complete':
            print('finished refresing')
            notifier.stop()


server = PlexServer(url, token)
library = server.library
section = library.section(section_title)
notifier = server.startAlertListener(callback=cb)

if section.refreshing:
    print('already refrehsing')
else:
    print('start refrehsing')
    section.update()

while notifier.isAlive():
    sleep(0.1)

print('addig item to playlist')
items = section.searchTracks(title=item_title, sort='addedAt:desc', maxresults=1)
print('items', items)
if items:
    playlist = server.playlist(playlist_title)
    print('playlist', playlist)
    playlist.addItems(items)
    print('item added to playlist')
else:
    print('no items found')
