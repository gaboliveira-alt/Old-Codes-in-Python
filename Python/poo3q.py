class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    
    def add_song(self, songs_name):
        self.songs.append(songs_name)
    
    def remove_song(self, songs_name):
        self.songs.remove(songs_name)
    
    def show_playlist(self):
        digits = len(str(len(self.songs)))
        
        for songs_no, songs_name in enumerate(self.songs):
            print('%0*d.%s' % (digits, songs_no + 1, songs_name))


playlist = Playlist('My Musics')

for k in range(15):
    playlist.add_song(f'Musica #{k + 1}')
    
playlist.show_playlist()
        