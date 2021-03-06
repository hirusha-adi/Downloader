import os
import webbrowser
import requests
from pytube import *
from youtubesearchpython import VideosSearch


class Info:
    VERSION = "0.9"
    CREATOR = "ZeaCeR#5641"


all_audio_qualities_tup = ("32kbps", "64kbps", "128kbps",
                           "160kbps", "192kbps", "240kbps", "256kbps", "320kbps")


def START_PROGRAM():
    ENTIRE_PROGRAM()


def show_logo():
    print("""       
                 ██████╗ ██╗     
                 ██╔══██╗██║     
                 ██║  ██║██║     
                 ██║  ██║██║     
                 ██████╔╝███████╗
                 ╚═════╝ ╚══════╝

                   Downloader
               CLI for Downloader
                      v0.5
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
    5) Privacy Policy
    6) Help
7) Download Others
8) Search and download
88) Update
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
        17) MP3
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
    elif selectquality == 17:
        return "mp3"
    else:
        return "720p"


def DOWNLOAD_VIDEO(qualityvid: str, urlvid: str, subs: bool = False, videoinformationyn: bool = False):
    try:
        yt = YouTube(urlvid)
    # except VideoUnavailable:
    #         print("[!!] VIDEO UNAVAILABLE!")
    #         return
    except Exception as e:
        print("Error", e)
        return

    if videoinformationyn:
        print(f"""\nExtracting Information: \n[+]Title: {yt.title} \n[+]Thumnail URL: {yt.thumbnail_url} \n[+]Author: {yt.author} \n[+]Channel ID: {yt.channel_id} \n[+]Channel URL: {yt.channel_url} \n[+]Video Length: {yt.length} \n[+]Published Date:{yt.publish_date} \n[+]Age Restricted: {yt.age_restricted} \n[+]Video URL: {urlvid} \n[+]Video Description: {yt.description}""")
        try:
            with open(f"""{yt.title} - Information.txt""", "w", encoding="utf8") as fileinfotxt:
                fileinfotxt.write(f"""[+]Title: {yt.title} \n[+]Thumnail URL: {yt.thumbnail_url} \n[+]Author: {yt.author} \n[+]Channel ID: {yt.channel_id} \n[+]Channel URL: {yt.channel_url} \n[+]Video Length: {yt.length} \n[+]Published Date:{yt.publish_date} \n[+]Age Restricted: {yt.age_restricted} \n[+]Video URL: {urlvid} \n[+]Video Description: {yt.description}""")
        except:
            with open(f"""{yt.title.replace('|', 'x').replace('?', 'x').replace('>', 'x').replace('<', 'x').replace(':', 'x').replace(';', 'x')} - Information.txt", "w""", encoding="utf8") as fileinfotxt:
                fileinfotxt.write(f"""[+]Title: {yt.title} \n[+]Thumnail URL: {yt.thumbnail_url} \n[+]Author: {yt.author} \n[+]Channel ID: {yt.channel_id} \n[+]Channel URL: {yt.channel_url} \n[+]Video Length: {yt.length} \n[+]Published Date:{yt.publish_date} \n[+]Age Restricted: {yt.age_restricted} \n[+]Video URL: {urlvid} \n[+]Video Description: {yt.description}""")

        print(f"[+] Wrote Information to {yt.title} - Information.txt")

    if subs:
        print("\n[*] Trying to download subtitles/captions")
        try:
            caption = yt.captions.get_by_language_code('en')
            print("[+] Successfully loaded subtitles/captions")
            try:
                with open(f"""{yt.title}.srt", "w", encoding="utf8""") as filesrt:
                    filesrt.write(caption.generate_srt_captions())
            except OSError:
                with open(f"""{yt.title.replace('|', 'x').replace('?', 'x').replace('>', 'x').replace('<', 'x').replace(':', 'x').replace(';', 'x')}.srt""", "w", encoding="utf8") as filesrt:
                    filesrt.write(caption.generate_srt_captions())
            print("[+] Created a .srt file!")
        except:
            print("[-] Unable to download subtitles")

    if qualityvid in all_audio_qualities_tup:
        print("\n[*] Trying to downlod the audio")
        try:
            video = yt.streams.filter(only_audio=True).filter(
                abr=f"{qualityvid}").first().download()
            print(f"[+] File downloaded successfully!\n{video}")
        except:
            print("[-] An Error has occured!")
            print(
                "[*] Trying to download with the highest available quality for the audio")
            try:
                video = yt.streams.filter(only_audio=True).first().download()
                print(f"[+] File downloaded successfully!\n{video}")
            except:
                print("[-] Failed!")
                print(
                    "[*] Trying to download with the lowest available quality for the audio")
                try:
                    video = yt.streams.filter(
                        only_audio=True).last().download()
                    print(f"[+] File downloaded successfully!\n{video}")
                except:
                    print("[!!] FAILED")
    # elif qualityvid == "mp3":
    else:
        print("\n[*] Trying to downlod the video")
        try:
            video = yt.streams.filter(res=f"{qualityvid}").filter(
                progressive=True).first().download()
            print(f"[+] File downloaded successfully!\n{video}")
        except:
            print("[-] An Error has occured!")
            print(
                "[*] Trying to download with the highest available quality for the video")
            try:
                video = yt.streams.filter(
                    progressive=True).get_highest_resolution().download()
                print(f"[+] File downloaded successfully!\n{video}")
            except:
                print("[-] Failed!")
                print(
                    "[*] Trying to download with the lowest available quality for the video")
                try:
                    video = yt.streams.filter(
                        progressive=True).get_highest_resolution()
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

        yes_list = ("y", "yes", "yeah")
        dl_subs = input("[?] Do you want to download subtitles(BETA)?: ")
        dl_vid_info = input("[?] Do you want to download video info?: ")
        if dl_subs in yes_list:
            psubs = True
        else:
            psubs = False
        if dl_vid_info in yes_list:
            pvideoinformationyn = True
        else:
            pvideoinformationyn = False

        downloadlink = input("[?] Enter the video link: ")

        DOWNLOAD_VIDEO(qualityvid=selectquality, urlvid=downloadlink,
                       subs=psubs, videoinformationyn=pvideoinformationyn)

        return

    if mmo == "2":
        os.system("cls")
        show_logo()
        show_all_qualities()

        selectquality = select_dl_quality()

        yes_list = ("y", "yes", "yeah")
        dl_subs = input("[?] Do you want to download subtitles(BETA)?: ")
        dl_vid_info = input("[?] Do you want to download video info?: ")
        if dl_subs in yes_list:
            psubs = True
        else:
            psubs = False
        if dl_vid_info in yes_list:
            pvideoinformationyn = True
        else:
            pvideoinformationyn = False

        downloadlink = input("[?] Enter the playlist link: ")
        allorsome = input(
            "[?] Do you want to download all videos in the playlist: ")

        no_wl = ["n", "no", "nope", "dont"]

        if allorsome.lower() in no_wl:
            pl = Playlist(f'{downloadlink}')
            whatno2dl = int(
                input("[?] How many videos do you want to download: "))
            # whatno2dl -= 1
            for url in pl.video_urls[:whatno2dl]:
                DOWNLOAD_VIDEO(qualityvid=selectquality, urlvid=url,
                               subs=psubs, videoinformationyn=pvideoinformationyn)

        else:
            pl = Playlist(f'{downloadlink}')
            for url in pl.video_urls:
                DOWNLOAD_VIDEO(qualityvid=selectquality, urlvid=url,
                               subs=psubs, videoinformationyn=pvideoinformationyn)

        return

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

    elif mmo == "5":
        webbrowser.open(
            "https://github.com/hirusha-adi/YouTube-Video-Downloader/blob/main/privacy-policy")
        ENTIRE_PROGRAM()

    elif mmo == "6":
        webbrowser.open(
            "https://github.com/hirusha-adi/YouTube-Video-Downloader/blob/main/help.md")
        ENTIRE_PROGRAM()

    elif mmo == "3":
        os.system("cls")
        show_logo()
        show_all_qualities()

        selectquality = select_dl_quality()

        yes_list = ("y", "yes", "yeah")
        dl_subs = input("[?] Do you want to download subtitles(BETA)?: ")
        dl_vid_info = input("[?] Do you want to download video info?: ")
        if dl_subs in yes_list:
            psubs = True
        else:
            psubs = False
        if dl_vid_info in yes_list:
            pvideoinformationyn = True
        else:
            pvideoinformationyn = False

        downloadlink = input("[?] Enter the channel link: ")
        allorsome = input(
            "[?] Do you want to download all videos in the channel: ")

        no_wl = ["n", "no", "nope", "dont"]

        if allorsome.lower() in no_wl:
            cl = Channel(f'{downloadlink}')
            whatno2dl = int(
                input("[?] How many videos do you want to download: "))
            # whatno2dl -= 1
            for url in cl.video_urls[:whatno2dl]:
                DOWNLOAD_VIDEO(qualityvid=selectquality, urlvid=url,
                               subs=psubs, videoinformationyn=pvideoinformationyn)

        else:
            cl = Channel(f'{downloadlink}')
            for url in cl.video_urls:
                DOWNLOAD_VIDEO(qualityvid=selectquality, urlvid=url,
                               subs=psubs, videoinformationyn=pvideoinformationyn)
        return

    elif mmo == "7":
        link = input("[?] Please enter the link: ")
        try:
            try:
                filename = link.split("/")[-1]
                if filename == "":
                    filename = link.split("/")[-2]
                else:
                    print(
                        f"""[+] Using filename: {filename.replace('|', 'x').replace('?', 'x').replace('>', 'x').replace('<', 'x').replace(':', 'x').replace(';', 'x')}""")

            except:
                try:
                    filename = link.split(".")[-2:]
                    print(
                        f"""[+] Using filename: {filename.replace('|', 'x').replace('?', 'x').replace('>', 'x').replace('<', 'x').replace(':', 'x').replace(';', 'x')}""")
                except:
                    filename = "unable_to_get_file_name"
                    print(f"[!] Using filename: unable_to_get_file_name")
            try:
                r = requests.get(f"{link}").content
            except:
                print("\n[-] Unable to Download the file!")
                return

            try:
                with open(f"{filename}", "wb", encoding="utf8") as filergetnoyt:
                    filergetnoyt.write(r)
                print(f"[+] Created file {filename} successfully!")
            except:
                print("\n[-] Unable to create a file!")
                return
        except:
            print("\n[-] Unable to Download the file!")
        print()

    elif mmo == "8":
        os.system("cls")
        show_logo()
        show_all_qualities()

        selectquality = select_dl_quality()

        yes_list = ("y", "yes", "yeah")
        dl_subs = input("[?] Do you want to download subtitles(BETA)?: ")
        dl_vid_info = input("[?] Do you want to download video info?: ")
        if dl_subs in yes_list:
            psubs = True
        else:
            psubs = False
        if dl_vid_info in yes_list:
            pvideoinformationyn = True
        else:
            pvideoinformationyn = False

        whattosearch = input("[?] Please enter what to search for: ")
        # add a open in webbroser feature to the GUI with a checkbox to enable and disable it
        videosSearch = VideosSearch(f'{whattosearch}', limit=1)
        mainresult = videosSearch.result()["result"]
        video_index = mainresult[0]

        video_link = video_index["link"]
        download_type = video_index["type"]

        try:
            print(f"""
+ Selected {video_index["title"]}
Type: {download_type}
Publisehd Time: {video_index["publishedTime"]}
Duration: {video_index["duration"]}
View Count: {video_index["viewCount"]["text"]}
Video Thumbnail: {video_index["thumbnails"][0]["url"]}
Uploaded channel name: {video_index["channel"]["name"]}
Video Link: {video_link}
                        """)
        except:
            print("[+] Selected video: Title: {video_index['title']}")

        if download_type == "video":
            DOWNLOAD_VIDEO(qualityvid=selectquality, urlvid=video_link,
                           subs=psubs, videoinformationyn=pvideoinformationyn)

        elif download_type == "channel":
            allorsome = input(
                "[?] Do you want to download all videos in the channel: ")

            no_wl = ["n", "no", "nope", "dont"]

            if allorsome.lower() in no_wl:
                cl = Channel(f'{video_link}')
                whatno2dl = int(
                    input("[?] How many videos do you want to download: "))
                # whatno2dl -= 1
                for url in cl.video_urls[:whatno2dl]:
                    DOWNLOAD_VIDEO(qualityvid=selectquality, urlvid=url,
                                   subs=psubs, videoinformationyn=pvideoinformationyn)

            else:
                cl = Channel(f'{video_link}')
                for url in cl.video_urls:
                    DOWNLOAD_VIDEO(qualityvid=selectquality, urlvid=url,
                                   subs=psubs, videoinformationyn=pvideoinformationyn)
            return

        else:
            allorsome = input(
                "[?] Do you want to download all videos in the playlist: ")

            no_wl = ["n", "no", "nope", "dont"]

            if allorsome.lower() in no_wl:
                pl = Playlist(f'{video_link}')
                whatno2dl = int(
                    input("[?] How many videos do you want to download: "))
                # whatno2dl -= 1
                for url in pl.video_urls[:whatno2dl]:
                    DOWNLOAD_VIDEO(qualityvid=selectquality, urlvid=url,
                                   subs=psubs, videoinformationyn=pvideoinformationyn)

            else:
                pl = Playlist(f'{video_link}')
                for url in pl.video_urls:
                    DOWNLOAD_VIDEO(qualityvid=selectquality, urlvid=url,
                                   subs=psubs, videoinformationyn=pvideoinformationyn)

            return

    elif mmo == "88":
        os.system("cls")
        print(f"[+] Current Version: {Info.VERSION}")
        latest_version = requests.get(
            "https://raw.githubusercontent.com/hirusha-adi/Downloader/main/update/vcli.txt").text
        if str(latest_version) == Info.VERSION:
            print("[+]No updates available\n[+] Downloader - CLI - is upto date!")
            return
        else:
            print("[+] Update available")
            print("[+] Starting to update")
            new_version_dl_link = requests.get(
                "https://raw.githubusercontent.com/hirusha-adi/Downloader/main/update/cli.txt").text
            print(f"[+] Recieved download link:", new_version_dl_link)
            print("[+] Downloading file...")
            new_version_data = requests.get(new_version_dl_link).content
            print("[+] Download complete!")
            with open(f"Downloader_{latest_version}.exe") as updated_version_file:
                updated_version_file.write(new_version_data)
            print(f"Created file: Downloader_{latest_version}.exe")

    elif mmo == "99":
        exit()

    else:
        ENTIRE_PROGRAM()


if __name__ == "__main__":
    START_PROGRAM()
