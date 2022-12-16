import lyricsgenius

token = 'YOUR_TOKEN'

genius = lyricsgenius.Genius(token)


def getLyrics(artistName: str, songName: str):
    artist = genius.search_artist(artistName, max_songs=0)
    if artist != None:
        song = genius.search_song(songName, artist.name)
        if song != None:
            return song.lyrics
        else:
            return None
    else:
        return None