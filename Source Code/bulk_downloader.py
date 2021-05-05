
_author__ = "moiSentinel"
__license__ = "Apache License 2.0"
__version__ = "1.1.1"
__maintainer__ = "moiSentinel"
__status__ = "In Progress"

from pytube import *
import os

print("\nmoiSentineL's Youtube Bulk Video Downloader\nStable 1.1.1 / YDT 2.1.1")
print("This program will download video in bulk from Youtube.\n")

def download():
    try:   
        filepathinput = input("\nEnter path for the .txt file with the links (e.g. E:\Files\links.txt):\n>> ")

        link= open(filepathinput,'r')
        line_count = 0

        for line in link:
            if line != "\n":
                line_count += 1
        choosefileformat = int(input("\nChoose File Format:\n1 for .mp4 (video).\n2 for .mp3 (audio).\n>> "))
    
        if choosefileformat == 1:
            choosequality = int(input("\nChoose Video Quality:\n1 for 720p.\n2 for 480p.\n3 for 360p\n>> "))
            if choosequality == 1:
                destinationinput = input("\nEnter path for the file to save (e.g. E:\Movies), press enter for default directory:\n>> ")
                if destinationinput == '':
                    if not os.path.exists('downloads'):
                        os.makedirs('downloads')

                    currentdirectory = os.getcwd()
                    destination = currentdirectory +'\downloads'
                else:
                    destination = destinationinput
                    
                print(line_count, 'file(s) added to download.')
                proceed = input('Proceed? (y/n)\n>> ').lower()
                if proceed == 'y':
                    link.seek(0)
                    for i in link:
                        try:	
                            yt = YouTube(i)  
                            video = yt.streams.filter(res='720p').first() 
                            video.download(destination)
                            filesize = format(int(video.filesize)/1000000, ".2f") + " MB"
                            print(yt.title + " has been successfully downloaded with the size of ", filesize)
                        except Exception as e:
                            print('Something went wrong\n')
                            print("Error: ", e.args)
                else:
                    restart = input("Restart Program? (y/n)\n>> ").lower()
                    if restart == 'y':
                        redo = download()
                    else:
                        exit()
            elif choosequality == 2:
                destinationinput = input("\nEnter path for the file to save (e.g. E:\Movies), press enter for default directory:\n>> ")
                if destinationinput == '':
                    if not os.path.exists('downloads'):
                        os.makedirs('downloads')

                    currentdirectory = os.getcwd()
                    destination = currentdirectory +'\downloads'
                else:
                    destination = destinationinput
                    
                print(line_count, 'file(s) added to download.')
                proceed = input('Proceed? (y/n)\n>> ').lower()
                if proceed == 'y':
                    link.seek(0)
                    for i in link:
                        try:	
                            yt = YouTube(i)  
                            video = yt.streams.filter(res='480p').first() 
                            video.download(destination)
                            filesize = format(int(video.filesize)/1000000, ".2f") + " MB"
                            print(yt.title + " has been successfully downloaded with the size of ", filesize)
                        except Exception as e:
                            print('Something went wrong\n')
                            print("Error: ", e.args)
                else:
                    restart = input("Restart Program? (y/n)\n>> ").lower()
                    if restart == 'y':
                        redo = download()
                    else:
                        exit()
            elif choosequality == 3:
                destinationinput = input("\nEnter path for the file to save (e.g. E:\Movies), press enter for default directory:\n>> ")
                if destinationinput == '':
                    if not os.path.exists('downloads'):
                        os.makedirs('downloads')

                    currentdirectory = os.getcwd()
                    destination = currentdirectory +'\downloads'
                else:
                    destination = destinationinput
                
                print(line_count, 'file(s) added to download.')
                proceed = input('Proceed? (y/n)\n>> ').lower()
                if proceed == 'y':
                    link.seek(0)
                    for i in link:
                        try:	
                            yt = YouTube(i)  
                            video = yt.streams.filter(res='360p').first() 
                            video.download(destination)
                            filesize = format(int(video.filesize)/1000000, ".2f") + " MB"
                            print(yt.title + " has been successfully downloaded with the size of ", filesize)
                        except Exception as e:
                            print('Something went wrong\n')
                            print("Error: ", e.args)
                else:
                    restart = input("Restart Program? (y/n)\n>> ").lower()
                    if restart == 'y':
                        redo = download()
                    else:
                        exit()
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
                    
                print(line_count, 'file(s) added to download.')
                proceed = input('Proceed? (y/n)\n>> ').lower()
                if proceed == 'y':
                    link.seek(0)
                    for i in link:
                        try:	
                            yt = YouTube(i)
                            video = yt.streams.filter(only_audio=True).first()
                            filesize = format(int(video.filesize)/1000000, ".2f") + " MB"
                            out_file = video.download(output_path=destination)
                            base, ext = os.path.splitext(out_file)
                            new_file = base + '.mp3'
                            os.rename(out_file, new_file)
                            print(yt.title + " has been successfully downloaded with the size of " , filesize)

                        except:
                            print('\nSomething Went Wrong\nLogging Now.\n')

                            f = open('failed url log.txt', 'a')
                            failed_url = yt.title + ': ' + i
                            f.write(failed_url)
                            f.close() 
                else:
                    restart = input("Restart Program? (y/n)\n>> ").lower()
                    if restart == 'y':
                        redo = download()
                    else:
                        exit()
            except Exception as e:
                print('Something went wrong\n')
                print(e.args)

        print('\nTask Completed!')
    except Exception as e:
        print('Something went wrong\n')
        print(e.args)
download()
k = input('Press <Enter> key to exit.')