from pytube import *
import os

print("\nmoiSentineL's Youtube Playlist Video URL Finder\nStable v1.0\n")
print('This program will make a .txt file with all the links of the videos from a playlist.\n')

def urlfinder():
    userinputlink = input("Enter Youtube Playlist Link:\n>> ")
    p= Playlist(userinputlink)

    print('\nPlaylist found.')
    proceed = input('Proceed? (y/n)\n>> ').lower()
    if proceed == 'y':
        f = open("links.txt", "a")
        for url in p.video_urls:
            urlappend = url + "\n"
            f.write(urlappend)
        f.close()
    else:
        restart = input("Restart Program? (y/n)\n>> ").lower()
        if restart == 'y':
            redo = urlfinder()
        else:
            exit()

    print('\nTask Completed!')

urlfinder()
k = input('Press any key to exit.')