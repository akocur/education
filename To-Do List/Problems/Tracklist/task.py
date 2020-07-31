def tracklist(**kwargs):
    for artist in kwargs:
        print(artist)
        for album in kwargs[artist]:
            print('ALBUM:', album, 'TRACK:', kwargs[artist][album])
