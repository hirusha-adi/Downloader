import os, time, platform, webbrowser
import importshandler
from pytube import *

class Info:
        VERSION = "0.1"
        CREATOR = "ZeaCeR#5641"
        


def START_PROGRAM():
        importshandler.ALL()
        ENTIRE_PROGRAM()

def show_logo():
    print("""       
 _     _  _______  _____   ______ 
(_)   (_)(__ _ __)(_____) (______)
 (_)_(_)    (_)   (_)  (_)(_)__   
   (_)      (_)   (_)  (_)(____)  
   (_)      (_)   (_)__(_)(_)     
   (_)      (_)   (_____) (_)     
                                 
                                  """)

def show_menu_items():
    os.system("cls")
    show_logo()
    print("""
1) Download a Single Video
2) Download a Playlist
Others:
    3) Why Free?
    4) Credits
    5) Contributors
    6) Privacy Policy
    7) Help
99) Exit
    """)

def show_all_qualities():
        print("""
Video:
        1) 1080p
        2) 720p
        3) 480p
        4) 360p
        5) 240p
        6) 144p
Audio:
        7) MP3
        """)

def DOWNLOAD_VIDEO(qualityvid, urlvid):
        try:
                yt = YouTube(urlvid)
        except VideoUnavailable:
                print("[!!] VIDEO UNAVAILABLE!")
                return
        except Exception as e:
                print("Error", e)
                return

        print(f"\nExtracting Information: \n[+] Title: {yt.title} \n[+]Thumnail URL: {yt.thumbnail_url} \n[+]Video Description: {yt.description} \n[+]Author: {yt.author} \n[+]Channel ID: {yt.channel_id} \n[+]Channel URL: {yt.channel_url} \n[+]Video Length: {yt.length} \n[+]Published Date:{yt.publish_date} \n[+]Age Restricted: {yt.age_restricted} \n[+]Video URL: {downloadlink}\n")
        
        try:
                with open(f"{yt.title} - Information.txt", "w") as fileinfotxt:
                        fileinfotxt.write(f"[+] Title: {yt.title} \n[+]Thumnail URL: {yt.thumbnail_url} \n[+]Author: {yt.author} \n[+]Channel ID: {yt.channel_id} \n[+]Channel URL: {yt.channel_url} \n[+]Video Length: {yt.length} \n[+]Published Date:{yt.publish_date} \n[+]Age Restricted: {yt.age_restricted} \n[+]Video URL: {downloadlink} \n[+]Video Description: {yt.description}")
        except:
                with open(f"{yt.title.replace('|', 'x').replace('?', 'x').replace('>', 'x').replace('<', 'x').replace(':', 'x').replace(';', 'x')} - Information.txt", "w") as fileinfotxt:
                        fileinfotxt.write(f"[+] Title: {yt.title} \n[+]Thumnail URL: {yt.thumbnail_url} \n[+]Author: {yt.author} \n[+]Channel ID: {yt.channel_id} \n[+]Channel URL: {yt.channel_url} \n[+]Video Length: {yt.length} \n[+]Published Date:{yt.publish_date} \n[+]Age Restricted: {yt.age_restricted} \n[+]Video URL: {downloadlink} \n[+]Video Description: {yt.description}")
        
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

        mmo = input("[?] Please select an option: ")

        if mmo == "1":
                os.system("cls")
                show_logo()
                show_all_qualities()

                selectquality = input("[?} Please select a quality: ")
                if selectquality == 1:
                        downloadquality = "1080p"
                elif selectquality == 2:
                        downloadquality = "720p"
                elif selectquality == 3:
                        downloadquality = "480p"
                elif selectquality == 4:
                        downloadquality = "360p"
                elif selectquality == 5:
                        downloadquality = "240p"
                elif selectquality == 6:
                        downloadquality = "144p"
                elif selectquality == 7:
                        downloadquality = "MP3"
                else:
                        downloadquality = "720p"
                
                downloadlink = input("[?] Enter the video link: ")
                DOWNLOAD_VIDEO(qualityvid=downloadquality, urlvid=downloadlink)


        if mmo == "2":
                os.system("cls")
                show_logo()
                show_all_qualities()

                selectquality = input("[?} Please select a quality: ")
                if selectquality == 1:
                        downloadquality = "1080p"
                elif selectquality == 2:
                        downloadquality = "720p"
                elif selectquality == 3:
                        downloadquality = "480p"
                elif selectquality == 4:
                        downloadquality = "360p"
                elif selectquality == 5:
                        downloadquality = "240p"
                elif selectquality == 6:
                        downloadquality = "144p"
                elif selectquality == 7:
                        downloadquality = "MP3"
                else:
                        downloadquality = "720p"
                
                downloadlink = input("[?] Enter the playlist link: ")
                allorsome = input("[?] Do you want to download all videos in the playlist: ")
                
                yes_wl = ["y", "yes", "ok", "k"]
                
                if allorsome.lower() in yes_wl:
                        pl = Playlist(f'{downloadlink}')
                        whatno2dl = int(input("[?] How many videos do you want to download: "))
                        whatno2dl -= 1
                        for url in pl.video_urls[:whatno2dl]:
                                DOWNLOAD_VIDEO(qualityvid=downloadquality, urlvid=downloadlink)

                else:
                        pl = Playlist(f'{downloadlink}')
                        for url in pl.video_urls:
                                DOWNLOAD_VIDEO(qualityvid=downloadquality, urlvid=downloadlink)

        if mmo == "3":
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
                """)

        if mmo == "4":
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

        if mmo == "5":
                webbrowser.open("")


if __name__ == "__main__":
        START_PROGRAM()
