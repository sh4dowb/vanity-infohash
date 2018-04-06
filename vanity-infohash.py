import bencoder, sys, hashlib, base64

target = sys.argv[1]
with open(target, 'rb') as torrent_file:
    torrent = bencoder.decode(torrent_file.read())

def get_infohash(torrent):
    encoded = bencoder.encode(torrent[b'info'])
    sha1 = hashlib.sha1(encoded).hexdigest()
    return sha1

original_name = torrent[b'info'][b'name'].decode('utf-8')

def save_torrent(torrent, name):
    with open(name, 'wb+') as torrent_file:
        torrent_file.write(bencoder.encode(torrent))

vanity = 0
while True:
    torrent[b'info'][b'vanity'] = str(vanity)
    if get_infohash(torrent).startswith(sys.argv[2]):
        save_torrent(torrent, sys.argv[3])
        print(vanity, get_infohash(torrent))
        break
    vanity += 1

