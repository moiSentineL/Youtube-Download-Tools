from pytube import *
import os

print("\nmoiSentineL's Youtube Video Downloader\nDiscontinued / Stable\n")
print("This program will download video(s) from Youtube as you like.\n")

def download():
    try:
        chooseinput = int(input("Choose Link Input:\n1 for Manual Input (for one video).\n2 for .txt file (for two or more videos).\n>> "))
        if chooseinput == 1:
            linkinput = input('\nEnter Video link\n>> ')

            try: 
                yt = YouTube(linkinput) 
            except Exception as e: 
                print('Something went wrong\n')
                print(e.args)

            choosefileformat = int(input("\nChoose File Format:\n1 for .mp4 (video).\n2 for .mp3 (audio).\n>> "))
                
            if choosefileformat == 1:
                try:
                    video = yt.streams.filter(file_extension='mp4').first()           
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
                    print(e.args)
                
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
                    print(e.args)
                
        elif chooseinput == 2:
            filepathinput = input("\nEnter path for the .txt file with the links (e.g. E:\Files\links.txt):\n>> ")

            link= open(filepathinput,'r')
            line_count = 0

            for line in link:
                if line != "\n":
                    line_count += 1

            choosefileformat = int(input("\nChoose File Format:\n1 for .mp4 (video).\n2 for .mp3 (audio).\n>> "))

            if choosefileformat == 1:
                try:
                    destination = input("\nEnter path for the file to save (e.g. E:\Movies):\n>> ")
                    print(line_count, 'file(s) added to download.')
                    proceed = input('Proceed? (y/n)\n>> ').lower()
                    if proceed == 'y':
                        link.seek(0)
                        for i in link:
                            try:	
                                yt = YouTube(i)  
                                video = yt.streams.filter(file_extension='mp4').first()
                                video.download(destination)
                                filesize = format(int(video.filesize)/1000000, ".2f") + " MB"
                                print(yt.title + " has been successfully downloaded with the size of ", filesize)
                            except Exception as e:
                                print('Something went wrong\n')
                                print(e.args)
                    else:
                        restart = input("Restart Program? (y/n)\n>> ").lower()
                        if restart == 'y':
                            redo = download()
                        else:
                            exit()
                        
                except Exception as e:
                    print('Something went wrong\n')
                    print(e.args)
                
            else:
                try:
                    destination = input("\nEnter path for the file to save (e.g. E:\Movies):\n>> ")
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
k = input('Press any key to exit.')