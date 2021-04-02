from pytube import *
import os

print("\nmoiSentineL's Youtube Video Downloader\nStable 2.0")
print("This program will download video from Youtube.\n")

def download():
    try:
        linkinput = input('Enter Video link\n>> ')

        try: 
            yt = YouTube(linkinput) 
        except Exception as e: 
            print('Something went wrong\n')
            print("Error: ", e.args)

        choosefileformat = int(input("\nChoose File Format:\n1 for .mp4 (video).\n2 for .mp3 (audio).\n>> "))
            
        if choosefileformat == 1:
            choosequality = int(input("\nChoose Video Quality:\n1 for 720p.\n2 for 480p.\n3 for 360p\n>> "))     
            if choosequality == 1:
                try:
                    video = yt.streams.filter(res='720p').first()           
                    destination = input("\nEnter path for the file to save (e.g. E:\Movies):\n>> ")
                    filesize = format(int(video.filesize)/1000000, ".2f") + " MB"
                    print('Filename: ', video.title)
                    print('Filesize: ', filesize)
                    proceed = input('Proceed? (y/n)\n>> ').lower()
                    if proceed == 'y':
                        video.download(destination)
                        print(yt.title + " has been successfully downloaded.")
                    else:
                        restart = input("Restart Program? (y/n)\n>> ").lower()
                        if restart == 'y':
                            redo = download()
                        else:
                            exit()
                except Exception as e:
                    print('Something went wrong\n')
                    print("Error: ", e.args)
            elif choosequality == 2:
                try:
                    video = yt.streams.filter(res='480p').first()           
                    destination = input("\nEnter path for the file to save (e.g. E:\Movies):\n>> ")
                    filesize = format(int(video.filesize)/1000000, ".2f") + " MB"
                    print('Filename: ', video.title)
                    print('Filesize: ', filesize)
                    proceed = input('Proceed? (y/n)\n>> ').lower()
                    if proceed == 'y':
                        video.download(destination)
                        print(yt.title + " has been successfully downloaded.")
                    else:
                        restart = input("Restart Program? (y/n)\n>> ").lower()
                        if restart == 'y':
                            redo = download()
                        else:
                            exit()
                except Exception as e:
                    print('Something went wrong\n')
                    print("Error: ", e.args)
            elif choosequality == 3:
                try:
                    video = yt.streams.filter(res='360p').first()           
                    destination = input("\nEnter path for the file to save (e.g. E:\Movies):\n>> ")
                    filesize = format(int(video.filesize)/1000000, ".2f") + " MB"
                    print('Filename: ', video.title)
                    print('Filesize: ', filesize)
                    proceed = input('Proceed? (y/n)\n>> ').lower()
                    if proceed == 'y':
                        video.download(destination)
                        print(yt.title + " has been successfully downloaded.")
                    else:
                        restart = input("Restart Program? (y/n)\n>> ").lower()
                        if restart == 'y':
                            redo = download()
                        else:
                            exit()
                except Exception as e:
                    print('Something went wrong\n')
                    print("Error: ", e.args)
        else:
            try:
                video = yt.streams.filter(only_audio=True).first()
                destination = input("\nEnter path for the file to save (e.g. E:\Movies):\n>> ")
                filesize = format(int(video.filesize)/1000000, ".2f") + " MB"
                print('Filename: ', video.title)
                print('Filesize: ', filesize)
                proceed = input('Proceed? (y/n)\n>> ').lower()
                if proceed == 'y':
                    out_file = video.download(output_path=destination)
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '.mp3'
                    os.rename(out_file, new_file)
                    print(yt.title + " has been successfully downloaded.")
                else:
                    restart = input("Restart Program? (y/n)\n>> ").lower()
                    if restart == 'y':
                        redo = download()
                    else:
                        exit()

            except Exception as e:
                print('Something went wrong\n')
                print("Error: ", e.args)

        print('\nTask Completed!')
    except Exception as e:
        print('Something went wrong\n')
        print("Error: ", e.args)

download()
k = input('Press <Enter> key to exit.')