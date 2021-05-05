
_author__ = "moiSentinel"
__license__ = "Apache License 2.0"
__version__ = "1.0.1"
__maintainer__ = "moiSentinel"
__status__ = "In Progress"

from pytube import *
import os

print("\nmoiSentineL's Youtube Bulk Video Downloader\nStable 1.0.1 / YDT 2.1.1")
print("This program will download playlists from Youtube.\n")

def download():
    try:  
        userinputlink = input("Enter Youtube Playlist Link:\n>> ")
        p= Playlist(userinputlink)

        choosefileformat = int(input("\nChoose File Format:\n1 for .mp4 (video).\n2 for .mp3 (audio).\n>> "))
        if choosefileformat == 1:
            choosequality = int(input("\nChoose Video Quality:\n1 for 720p.\n2 for 480p.\n3 for 360p\n>> "))     
            if choosequality == 1:
                try:
                    destinationinput = input("\nEnter path for the file to save (e.g. E:\Movies), press enter for default directory:\n>> ")
                    if destinationinput == '':
                        if not os.path.exists('downloads'):
                            os.makedirs('downloads')

                        currentdirectory = os.getcwd()
                        destination = currentdirectory +'\downloads'
                    else:
                        destination = destinationinput
                    
                    print ('Playlist found.\nName: ', p.title)
                    proceed = input('Proceed? (y/n)\n>> ').lower()  
                    if proceed == 'y':
                        for video in p.videos:
                            filesize = format(int(video.filesize)/1000000, ".2f") + " MB"
                            video.streams.filter(res='720p').first().download(destination) 
                            print(video.title + " has been successfully downloaded with the size of " , filesize)
                    else:
                        pass
                except Exception as e:
                    print('Something went wrong\n')
                    print(e.args)
            elif choosequality == 2:
                try:
                    destinationinput = input("\nEnter path for the file to save (e.g. E:\Movies), press enter for default directory:\n>> ")
                    if destinationinput == '':
                        if not os.path.exists('downloads'):
                            os.makedirs('downloads')

                        currentdirectory = os.getcwd()
                        destination = currentdirectory +'\downloads'
                    else:
                        destination = destinationinput
                    
                    print ('Playlist found.\nName: ', p.title)
                    proceed = input('Proceed? (y/n)\n>> ').lower()  
                    if proceed == 'y':
                        for video in p.videos:
                            filesize = format(int(video.filesize)/1000000, ".2f") + " MB"
                            video.streams.filter(res='480p').first().download(destination) 
                            print(video.title + " has been successfully downloaded with the size of " , filesize)
                    else:
                        pass
                except Exception as e:
                    print('Something went wrong\n')
                    print(e.args)
            else:
                try:
                    destinationinput = input("\nEnter path for the file to save (e.g. E:\Movies), press enter for default directory:\n>> ")
                    if destinationinput == '':
                        if not os.path.exists('downloads'):
                            os.makedirs('downloads')

                        currentdirectory = os.getcwd()
                        destination = currentdirectory +'\downloads'
                    else:
                        destination = destinationinput
                    
                    print ('Playlist found.\nName: ', p.title)
                    proceed = input('Proceed? (y/n)\n>> ').lower()  
                    if proceed == 'y':
                        for video in p.videos:
                            filesize = format(int(video.filesize)/1000000, ".2f") + " MB"
                            video.streams.filter(res='480p').first().download(destination) 
                            print(video.title + " has been successfully downloaded with the size of " , filesize)
                    else:
                        pass
                except Exception as e:
                    print('Something went wrong\n')
                    print(e.args)
        else:
            try:
                destinationinput = input("\nEnter path for the file to save (e.g. E:\Movies), press enter for default directory:\n>> ")
                if destinationinput == '':
                    if not os.path.exists('downloads'):
                        os.makedirs('downloads')

                    currentdirectory = os.getcwd()
                    destination = currentdirectory +'\downloads'
                else:
                    destination = destinationinput
                
                print ('Playlist found.\nName: ', p.title)
                proceed = input('Proceed? (y/n)\n>> ').lower()  
                if proceed == 'y':  
                    for video in p.videos:
                        videos = video.streams.filter(only_audio=True).first()
                        filesize = format(int(videos.filesize)/1000000, ".2f") + " MB"
                        out_file = videos.download(output_path=destination)
                        base, ext = os.path.splitext(out_file)
                        new_file = base + '.mp3'
                        os.rename(out_file, new_file)
                        print(videos.title + " has been successfully downloaded with the size of " , filesize)
            except Exception as e:
                print('Something went wrong\n')
                print(e.args)          
        print('\nTask Completed!')
    except Exception as e:
        print('Something went wrong\n')
        print(e.args)

download()
k = input('Press <Enter> key to exit.')

