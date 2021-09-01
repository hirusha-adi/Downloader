import os, time, platform, webbrowser
# import importshandler
from pytube import *

class Info:
        VERSION = "0.1"
        CREATOR = "ZeaCeR#5641"

all_audio_qualities_tup = ("32kbps", "64kbps", "128kbps", "160kbps", "192kbps", "240kbps", "256kbps", "320kbps")

def START_PROGRAM():
        # importshandler.ALL()
        ENTIRE_PROGRAM()

def show_logo():
    print("""       
        ██████╗ ██╗   ██╗████████╗██╗   ██╗
        ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║   ██║
        ██║  ██║ ╚████╔╝    ██║   ██║   ██║
        ██║  ██║  ╚██╔╝     ██║   ╚██╗ ██╔╝
        ██████╔╝   ██║      ██║    ╚████╔╝ 
        ╚═════╝    ╚═╝      ╚═╝     ╚═══╝  
                                        
            Download You Tube Videos
        CLI for YouTube Video Downloader
                        """)

def show_menu_items():
    os.system("cls")
    show_logo()
    print("""
1) Download a Single Video
2) Download a Playlist
3) Download videos of a Channel
Others:
    4) Credits
    5) Contributors
    6) Privacy Policy
    7) Help
99) Exit
    """)


def show_all_qualities():
        print("""
Video:
        1) 2160p
        2) 1440p
        3) 1080p
        4) 720p
        5) 480p
        6) 360p
        7) 240p
        8) 144p
Audio(MP3):
        9) 32kbps
        10) 64kbps
        11) 128kbps
        12) 160kbps
        13) 192kbps
        14) 240kbps
        15) 256kbps
        16) 320kbps
        """)


def select_dl_quality():
        selectquality = int(input("[?] Please select a quality: "))
        if selectquality == 1:
                return "2160p"
        elif selectquality == 2:
                return "1440p"
        elif selectquality == 3:
                return "1080p"
        elif selectquality == 4:
                return "720p"
        elif selectquality == 5:
                return "480p"
        elif selectquality == 6:
                return "360p"
        elif selectquality == 7:
                return "240p"
        elif selectquality == 8:
                return "144p"
        elif selectquality == 9:
                return "32kbps"
        elif selectquality == 10:
                return "64kbps"
        elif selectquality == 11:
                return "128kbps"
        elif selectquality == 12:
                return "160kbps"
        elif selectquality == 13:
                return "192kbps"
        elif selectquality == 14:
                return "240kbps"
        elif selectquality == 15:
                return "256kbps"
        elif selectquality == 16:
                return "320kbps"
        else:
                return "720p"


def DOWNLOAD_VIDEO(qualityvid, urlvid):
        try:
                yt = YouTube(urlvid)
        except VideoUnavailable:
                print("[!!] VIDEO UNAVAILABLE!")
                return
        except Exception as e:
                print("Error", e)
                return

        print(f"\nExtracting Information: \n[+]Title: {yt.title} \n[+]Thumnail URL: {yt.thumbnail_url} \n[+]Author: {yt.author} \n[+]Channel ID: {yt.channel_id} \n[+]Channel URL: {yt.channel_url} \n[+]Video Length: {yt.length} \n[+]Published Date:{yt.publish_date} \n[+]Age Restricted: {yt.age_restricted} \n[+]Video URL: {urlvid} \n[+]Video Description: {yt.description}")
        
        try:
                with open(f"{yt.title} - Information.txt", "w") as fileinfotxt:
                        fileinfotxt.write(f"[+]Title: {yt.title} \n[+]Thumnail URL: {yt.thumbnail_url} \n[+]Author: {yt.author} \n[+]Channel ID: {yt.channel_id} \n[+]Channel URL: {yt.channel_url} \n[+]Video Length: {yt.length} \n[+]Published Date:{yt.publish_date} \n[+]Age Restricted: {yt.age_restricted} \n[+]Video URL: {urlvid} \n[+]Video Description: {yt.description}")
        except:
                with open(f"{yt.title.replace('|', 'x').replace('?', 'x').replace('>', 'x').replace('<', 'x').replace(':', 'x').replace(';', 'x')} - Information.txt", "w") as fileinfotxt:
                        fileinfotxt.write(f"[+]Title: {yt.title} \n[+]Thumnail URL: {yt.thumbnail_url} \n[+]Author: {yt.author} \n[+]Channel ID: {yt.channel_id} \n[+]Channel URL: {yt.channel_url} \n[+]Video Length: {yt.length} \n[+]Published Date:{yt.publish_date} \n[+]Age Restricted: {yt.age_restricted} \n[+]Video URL: {urlvid} \n[+]Video Description: {yt.description}")
        
        print(f"[+] Wrote Information to {yt.title} - Information.txt")
        print("\n[*] Trying to download subtitles/captions")
        try:
                caption = yt.captions.get_by_language_code('en')
                print("[+] Successfully loaded subtitles/captions")
                try:
                        with open(f"{yt.title}.srt", "w") as filesrt:
                                filesrt.write(caption.generate_srt_captions())
                except OSError:
                        with open(f"{yt.title.replace('|', 'x').replace('?', 'x').replace('>', 'x').replace('<', 'x').replace(':', 'x').replace(';', 'x')}.srt", "w") as filesrt:
                                filesrt.write(caption.generate_srt_captions())
                print("[+] Created a .srt file!")
        except:
                print("[-] Unable to download subtitles")
        
        if qualityvid in all_audio_qualities_tup:
                print("\n[*] Trying to downlod the audio")
                try:
                        video = yt.streams.filter(only_audio=True).filter(abr=f"{qualityvid}").first().download()
                        print(f"[+] File downloaded successfully!\n{video}")
                except:
                        print("[-] An Error has occured!")
                        print("[*] Trying to download with the highest available quality for the audio")
                        try:
                                video = yt.streams.filter(only_audio=True).first().download()
                                print(f"[+] File downloaded successfully!\n{video}")
                        except:
                                print("[-] Failed!")
                                print("[*] Trying to download with the lowest available quality for the audio")
                                try:    
                                        video = yt.streams.filter(only_audio=True).last().download()
                                        print(f"[+] File downloaded successfully!\n{video}")
                                except:
                                        print("[!!] FAILED")
        else:
                print("\n[*] Trying to downlod the video")
                try:
                        video = yt.streams.filter(res=f"{qualityvid}").filter(progressive=True).first().download()
                        print(f"[+] File downloaded successfully!\n{video}")
                except:
                        print("[-] An Error has occured!")
                        print("[*] Trying to download with the highest available quality for the video")
                        try:
                                video = yt.streams.filter(progressive=True).get_highest_resolution().download()
                                print(f"[+] File downloaded successfully!\n{video}")
                        except:
                                print("[-] Failed!")
                                print("[*] Trying to download with the lowest available quality for the video")
                                try:    
                                        video = yt.streams.filter(progressive=True).get_highest_resolution()
                                        print(f"[+] File downloaded successfully!\n{video}")
                                except:
                                        print("[!!] FAILED")


def ENTIRE_PROGRAM():
        show_menu_items()

        mmo = input("\n[?] Please select an option: ")

        if mmo == "1":
                os.system("cls")
                show_logo()
                show_all_qualities()

                selectquality = select_dl_quality()
                
                downloadlink = input("[?] Enter the video link: ")
                DOWNLOAD_VIDEO(qualityvid=selectquality, urlvid=downloadlink)

                return


        if mmo == "2":
                os.system("cls")
                show_logo()
                show_all_qualities()

                selectquality = select_dl_quality()
                
                downloadlink = input("[?] Enter the playlist link: ")
                allorsome = input("[?] Do you want to download all videos in the playlist: ")
                
                no_wl = ["n", "no", "nope", "dont"]
                
                if allorsome.lower() in no_wl:
                        pl = Playlist(f'{downloadlink}')
                        whatno2dl = int(input("[?] How many videos do you want to download: "))
                        whatno2dl -= 1
                        for url in pl.video_urls[:whatno2dl]:
                                DOWNLOAD_VIDEO(qualityvid=selectquality, urlvid=url)

                else:
                        pl = Playlist(f'{downloadlink}')
                        for url in pl.video_urls:
                                DOWNLOAD_VIDEO(qualityvid=selectquality, urlvid=url)
                
                return

        if mmo == "4":
                os.system("cls")
                print(f"""
Once, i tried to download a music playlist to listen locally
and i the experience was inferior! The only option i had was
to pay 40 USD to purchause that software to download a single
small playlist, and YES! i didn't do it! I had a great idea
creating a program for that prupose for myself, and distribute
it for free and make it open source... First i tried creating
a GUI and i got it to work but except for the command of the
download button. I realized i am a dumb idiot who can't create
a command properly... then i made this CLI version

Edit: I did it successfully! and today, both of the versions
      will be released

                   made by ZeaCeR#5641
                        1) Home 
                        99) Exit
                """)
                mmo3i = input("[?] Please select an option: ")
                if mmo3i == "1":
                        ENTIRE_PROGRAM()
                elif mmo3i == "99":
                        exit()
                else:
                        ENTIRE_PROGRAM()

        if mmo == "5":
                os.system("cls")
                print(r"""                              
                ,. . ./(//..*////,. .       .               
          .    (/%/(**,*/#((,,,,,,*(//((((//.               
         ..   (/***,,,,,,,,**/////(/**,*//((( .             
     ..*#///////****,,....**/#***((/((/****/(*.             
     ...*/...........,*,(*.,,,,*((*/(((#*/*,*/(/%...        
         ,*,....,**(*.........*((#*#((((((((//,*/(/ .       
   ...     **/((,,,........,.*/((#/####((((##((((**(.     ..
.........   /(/((/,........,,,/((((#(((((((//(#((((/# ......
.......... (,((%(#((**/*...,,*//(/((((((((/////(((((//(/ ...
.......,*(#/(((%(((#*,,&@&%(((///*#/#(###((((/((//(((%(,....
....... /(/###%(((#/,,,..*. */#@@@@@&&&&%##((/((((/.###. ...
.... /  ##(#///(/(/,//(*..#*..*(#%@%@&&&///%(# %#(%%%(%(*...
...... (/ #(/(%(/(.**#*,*.((*&&&#%%%%&#((//(%#.,%/%#&%###...
........(/##(%#/((,...,/,(#/(((##%%%%&(/((&%#%,#%(#/(#(# ...
.........(/(/(((//*.,...,////%/(#(##%&/(/(&&%###(#&,........
..........(((//((,**..,....**///(##%%&#(//(%&@.(%#%.........
.......##(#/##/(,,..*..,......**/(####(/(#(%%&../# ,........
.........# ,#/.,,....,,..........**(/(%#((#((...............
.............*........**,,,,.....,**/#%(%%#.................
...............,*.....,//(/***,,,*/(((#(#/../,.*,. .........
..................,*...,//(((((//(##%%%%&.*,*//......... ...
........................,/*/(////((%#*,,............. ..   .

                    made by ZeaCeR#5641
                         1) Home 
                         99) Exit
                """)
                mmo4i = input("[?] Please select an option: ")
                if mmo4i == "1":
                        ENTIRE_PROGRAM()
                elif mmo4i == "99":
                        exit()
                else:
                        ENTIRE_PROGRAM()

        if mmo == "6":
                webbrowser.open("https://github.com/hirusha-adi/YouTube-Video-Downloader")
                ENTIRE_PROGRAM()

        elif mmo == "7":
                webbrowser.open("https://github.com/hirusha-adi/YouTube-Video-Downloader/blob/main/privacy-policy")
                ENTIRE_PROGRAM()

        elif mmo == "8":
                webbrowser.open("https://github.com/hirusha-adi/YouTube-Video-Downloader/blob/main/help.md")
                ENTIRE_PROGRAM()
        
        if mmo == "9":
                os.system("cls")
                show_logo()
                show_all_qualities()

                selectquality = select_dl_quality()
                
                downloadlink = input("[?] Enter the channel link: ")
                allorsome = input("[?] Do you want to download all videos in the channel: ")
                
                no_wl = ["n", "no", "nope", "dont"]
                
                if allorsome.lower() in no_wl:
                        cl = Channel(f'{downloadlink}')
                        whatno2dl = int(input("[?] How many videos do you want to download: "))
                        whatno2dl -= 1
                        for url in cl.video_urls[:whatno2dl]:
                                DOWNLOAD_VIDEO(qualityvid=selectquality, urlvid=url)

                else:
                        cl = Channel(f'{downloadlink}')
                        for url in cl.video_urls:
                                DOWNLOAD_VIDEO(qualityvid=selectquality, urlvid=url)
                return

        elif mmo == "99":
                exit()
        
        else:
                ENTIRE_PROGRAM()



if __name__ == "__main__":
        START_PROGRAM()
