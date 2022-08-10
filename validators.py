from pytube.extract import playlist_id

def validate_url(url):
    try:
        return playlist_id(url) in url
    except KeyError:
        return False