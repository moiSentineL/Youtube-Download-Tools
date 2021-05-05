
_author__ = "moiSentinel"
__license__ = "Apache License 2.0"
__version__ = "1.0.1"
__maintainer__ = "moiSentinel"
__status__ = "In Progress"

from pytube import *
import os

print("\nmoiSentineL's Youtube Playlist Video URL Finder\nStable 1.0.1 / YDT 2.1.1")
print('This program will make a .txt file with all the links of the videos from a playlist.\n')

def urlfinder():
    userinputlink = input("Enter Youtube Playlist Link:\n>> ")
    p= Playlist(userinputlink)

    print('\nPlaylist found.')
    proceed = input('Proceed? (y/n)\n>> ').lower()
    if proceed == 'y':
        destinationinput = input("\nEnter path for the file to save (e.g. E:\Movies), press enter for default directory:\n>> ")
        if destinationinput == '':
            destination = os.getcwd()
        else:
            destination = destinationinput
        linkfiledest = destination + "\links.txt"
        f = open(linkfiledest, "a")
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
k = input('Press <Enter> key to exit.')