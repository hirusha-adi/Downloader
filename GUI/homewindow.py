__title__ = "Downloader"
__author__ = "ZeaCeR#5641"
__version__ = "v1.2"

# #########################
# Made by ZeaCeR#5641
# (Hirusha Adikari)
# For any issue, please contact me!
# #########################

import os
import platform
import sys
import tkinter.ttk as ttk
from threading import Thread
from tkinter import *
from tkinter import messagebox
import webbrowser

import clipboard
import requests
from pytube import *
from youtubesearchpython import VideosSearch

import images

# Multi OS Support
if platform.system().lower().startswith('win'):
    UNIX = False
    CLEAR = "cls"
    BSP = "\\"
else:
    UNIX = True
    CLEAR = "clear"
    BSP = "/"

allDownloaded = []
allConverted = []

# ARGS when running the program
try:
    if str(sys.argv[1]).lower().startswith('n'):
        show_text = False
    else:
        show_text = True
except:
    show_text = True

# Creating Images
# --------------------
try:
    if "background2.png" in os.listdir(f"{os.getcwd()}{BSP}assets") and "background.png" in os.listdir(f"{os.getcwd()}{BSP}assets"):
        pass
    else:
        images.CREATE_ALL_IMAGES()
except Exception as e:
    # print(e)
    images.CREATE_ALL_IMAGES()


# Tkinter window
# --------------------
# root = Tk()
window = Tk()
window.resizable(False, False)
window.geometry("786x518")
window.configure(bg="#e3ffdc")
window.title("Downloader")


if show_text:
    print("""
 __   __                  __        __   ___  __  
|  \ /  \ |  | |\ | |    /  \  /\  |  \ |__  |__) 
|__/ \__/ |/\| | \| |___ \__/ /~~\ |__/ |___ |  \ 
                                                  
""")

# Functions
# --------------------
def exit_program():
    try:
        exit()
    except:
        quit()


def clear_yt_url():
    entry0.delete(0, "end")


def paste_yt_url():
    clipboarddata_yturl = clipboard.paste()
    entry0.delete(0, "end")
    entry0.insert(0, clipboarddata_yturl)


# Download Type
vidut = IntVar()
vidut.set("2")

# Download Format / Quality
vidrf = IntVar()
vidrf.set("2")

# Download Video Information
dlvidinfo = IntVar()

# Download Video Information
dlsubs = IntVar()

def to_mp3():
    global allDownloaded, allConverted
    for filename in allDownloaded:
        os.system(f"""ffmpeg "{filename}" "{'.'.join(filename.split('.')[:-1])}.mp3" """)
    allConverted.append(f"""{'.'.join(allDownloaded.split('.')[:-1])}.mp3""")

def to_mp4():
    global allDownloaded, allConverted
    for filename in allDownloaded:
        os.system(f"""ffmpeg "{filename}" "{'.'.join(allDownloaded.split('.')[:-1])}.mp4" """)
    allConverted.append(f"""{'.'.join(allDownloaded.split('.')[:-1])}.mp4""")

def to_mp3_nvenc():
    global allDownloaded, allConverted
    for filename in allDownloaded:
        os.system(f"""ffmpeg -hwaccel_device 0 -hwaccel cuda -i "{"'".join(filename.split('"'))}" -c:v h264_nvenc -preset slow "{''.join("'".join(filename.split('"')).split('.')[:-1])}.mp3" """)
    allConverted.append(f"""{''.join("'".join(filename.split('"')).split('.')[:-1])}.mp3""")

def to_mp4_nvenc():
    global allDownloaded, allConverted
    for filename in allDownloaded:
        os.system(f"""ffmpeg -hwaccel_device 0 -hwaccel cuda -i "{"'".join(filename.split('"'))}" -c:v h264_nvenc -preset slow "{''.join("'".join(filename.split('"')).split('.')[:-1])}.mp4" """)
    allConverted.append(f"""{''.join("'".join(filename.split('"')).split('.')[:-1])}.mp4""")

def select_dl_quality(selectquality):
    # These are the numbers i used for the radio buttons (tk.IntVar)
    # 1080p -> 1
    # 720p -> 2
    # 480p -> 3
    # 360p -> 4
    # 240p -> 5
    # 144p -> 6
    # 32kbps  -> 7
    # 64kbps  -> 8
    # 1440p -> 9
    # 2160p -> 10
    # 128kbps -> 11
    # 160kbps -> 12
    # 192kbps -> 13
    # 256kbps -> 14
    # 320kbps -> 15
    if selectquality == 10:
        return "2160p"
    elif selectquality == 9:
        return "1440p"
    elif selectquality == 1:
        return "1080p"
    elif selectquality == 2:
        return "720p"
    elif selectquality == 3:
        return "480p"
    elif selectquality == 4:
        return "360p"
    elif selectquality == 5:
        return "240p"
    elif selectquality == 6:
        return "144p"
    elif selectquality == 7:
        return "32kbps"
    elif selectquality == 8:
        return "64kbps"
    elif selectquality == 11:
        return "128kbps"
    elif selectquality == 12:
        return "160kbps"
    elif selectquality == 13:
        return "192kbps"
    elif selectquality == 14:
        return "256kbps"
    elif selectquality == 15:
        return "320kbps"
    else:
        if show_text:
            print(
                "[*] Selected default - Something is wrong! Please report to a developer")
        return "480p"


def select_dl_type(fuckingshit=2):
    if fuckingshit == 1:
        return "playlist"
    elif fuckingshit == 2:
        return "video"
    elif fuckingshit == 3:
        return "channel"
    else:
        if show_text:
            print(
                "[*] Selecting Default value: Video - Something is wrong, please report to a developer")
        return "video"


def selected_val():
    rsvrb = vidrf.get()
    return rsvrb


def selected_download_type():
    rsvub = vidut.get()
    return rsvub


def others_source_code():
    webbrowser.open("https://github.com/hirusha-adi/Downloader/")


def others_privacy_policy():
    webbrowser.open(
        "https://github.com/hirusha-adi/Downloader/blob/main/privacy-policy.md")


def others_help():
    webbrowser.open(
        "https://github.com/hirusha-adi/Downloader/blob/main/help.md")


def download_very_first_level():
    thr_dlfunc = Thread(target=download_first_level)
    thr_dlfunc.start()
    # download_first_level()


def download_first_level():
    videoquality = selected_val()
    whattypeofdl = selected_download_type()
    qualityintexttp = select_dl_quality(videoquality)
    downloadtypeintexttp = select_dl_type(whattypeofdl)
    fuckingurlmf = entry0.get()

    # if the link is a YouTube link
    # -----------------------
    ytlistfuck = ("www.youtube.com", "youtube.com", "youtube", "youtu.be")
    if fuckingurlmf.split("/")[:3][-1] in ytlistfuck:
        if show_text:
            print(
                "-------------------------\nFOUND A YOUTUBE LINK - DOWNLOADING\n-------------------------")
        if downloadtypeintexttp == "video":
            FUCKING_DOWNLOAD_ONE_VIDEO(
                qualityvid=qualityintexttp, urlvid=fuckingurlmf)

        elif downloadtypeintexttp == "playlist":
            pl = Playlist(f'{fuckingurlmf}')
            for url in pl.video_urls:
                FUCKING_DOWNLOAD_ONE_VIDEO(
                    qualityvid=qualityintexttp, urlvid=url)

        elif downloadtypeintexttp == "channel":
            cl = Channel(f'{fuckingurlmf}')
            for url in cl.video_urls:
                FUCKING_DOWNLOAD_ONE_VIDEO(
                    qualityvid=qualityintexttp, urlvid=url)

        else:
            if downloadtypeintexttp == "video":
                FUCKING_DOWNLOAD_ONE_VIDEO(
                    qualityvid=qualityintexttp, vidurl=fuckingurlmf)

    elif fuckingurlmf.lower() == "help":
        if show_text:
            print(
                "-------------------------\nOPENING HELP IN WEB BROWSER\n-------------------------")
        others_help()

    elif fuckingurlmf.lower() == "pp":
        if show_text:
            print(
                "-------------------------\nOPENING PRIVACY POLICY IN WEB BROWSER\n-------------------------")
        others_privacy_policy()

    else:
        if fuckingurlmf.lower().startswith('http') or fuckingurlmf.lower().startswith('https'):
            if show_text:
                print(
                    "-------------------------\nFOUND A NON YOUTUBE LINK\n-------------------------")
            try:
                try:
                    filename = fuckingurlmf.split("/")[-1]
                    if filename == "":
                        filename = fuckingurlmf.split("/")[-2]
                    else:
                        if show_text:
                            print(
                                f"""[+] Using filename: {filename.replace('|', 'x').replace('?', 'x').replace('>', 'x').replace('<', 'x').replace(':', 'x').replace(';', 'x').replace('"', "x").replace("'", "x")}""")
                except:
                    try:
                        filename = fuckingurlmf.split(".")[-2:]
                        if show_text:
                            print(
                                f"""[+] Using filename: {filename.replace('|', 'x').replace('?', 'x').replace('>', 'x').replace('<', 'x').replace(':', 'x').replace(';', 'x').replace('"', "x").replace("'", "x")}""")
                    except:
                        filename = "unable_to_get_file_name"
                        if show_text:
                            print(f"[!] Using filename: unable_to_get_file_name")
                try:
                    r = requests.get(f"{fuckingurlmf}").content
                except:
                    if show_text:
                        print("\n[-] Unable to Download the file!")
                    return

                try:
                    with open(f"{filename}", "wb") as filergetnoyt:
                        filergetnoyt.write(r)
                    if show_text:
                        print(f"[+] Created file {filename} successfully!")
                except:
                    if show_text:
                        print("\n[-] Unable to create a file!")
                    return
            except:
                if show_text:
                    print("\n[-] Unable to Download the file!")

        else:
            if show_text:
                print(
                    "-------------------------\nSEARCHING VIDEO NAME IN YOUTUBE\n-------------------------")
            videosSearch = VideosSearch(f'{fuckingurlmf}', limit=1)
            mainresult = videosSearch.result()["result"]
            video_index = mainresult[0]

            video_link = video_index["link"]
            download_type = video_index["type"]

            if show_text:
                try:
                    print(f"""
[+] Selected: {video_index["title"]}
[+] Type: {download_type}
[+] Publisehd Time: {video_index["publishedTime"]}
[+] Duration: {video_index["duration"]}
[+] View Count: {video_index["viewCount"]["text"]}
[+] Video Thumbnail: {video_index["thumbnails"][0]["url"]}
[+] Uploaded channel name: {video_index["channel"]["name"]}
[+] Video Link: {video_link}
    """)
                except:
                    print(f"[+] Selected video: Title: {video_index['title']}")

            if download_type == "video":
                if show_text:
                    print(
                        "-------------------------\nDOWNLOADING VIDEO\n-------------------------")
                FUCKING_DOWNLOAD_ONE_VIDEO(
                    qualityvid=qualityintexttp, urlvid=video_link)

            elif download_type == "channel":
                cl = Channel(f'{video_link}')
                if show_text:
                    print(
                        "-------------------------\nFOUND A YOUTUBE CHANNEL\n-------------------------")
                for url in cl.video_urls:
                    FUCKING_DOWNLOAD_ONE_VIDEO(
                        qualityvid=qualityintexttp, urlvid=url)

            else:
                pl = Playlist(f'{video_link}')
                if show_text:
                    print(
                        "-------------------------\nFOUND A YOUTUBE PLAYLIST\n-------------------------")
                for url in pl.video_urls:
                    FUCKING_DOWNLOAD_ONE_VIDEO(
                        qualityvid=qualityintexttp, urlvid=url)


def FUCKING_DOWNLOAD_ONE_VIDEO(qualityvid, urlvid):

    global allDownloaded

    download_subtitles = int(dlsubs.get())
    download_information = int(dlvidinfo.get())

    if show_text:
        print(f"[*] Recieved a download quality of {qualityvid} to {urlvid}")

        if download_subtitles:
            print(f"[*] Downloading subtitles")

        if download_information:
            print(f"[*] Downloading information")

    try:
        yt = YouTube(urlvid)
    # except VideoUnavailable:
    #     print("[!!] VIDEO UNAVAILABLE!")
    #     return
    except Exception as e:
        print("Error:", e)
        return

    if show_text:
        print("[+] Video Initiated")

    print("[+] Starting to download:", f"{yt.title}")

    if download_information:
        if show_text:
            print(f"\nExtracting Information: \n[+]Title: {yt.title} \n[+]Thumnail URL: {yt.thumbnail_url} \n[+]Author: {yt.author} \n[+]Channel ID: {yt.channel_id} \n[+]Channel URL: {yt.channel_url} \n[+]Video Length: {yt.length} \n[+]Published Date:{yt.publish_date} \n[+]Age Restricted: {yt.age_restricted} \n[+]Video URL: {urlvid} \n[+]Video Description: {yt.description}")
        try:
            with open(f"{yt.title} - Information.txt", "w", encoding="utf8") as fileinfotxt:
                fileinfotxt.write(f"[+]Title: {yt.title} \n[+]Thumnail URL: {yt.thumbnail_url} \n[+]Author: {yt.author} \n[+]Channel ID: {yt.channel_id} \n[+]Channel URL: {yt.channel_url} \n[+]Video Length: {yt.length} \n[+]Published Date:{yt.publish_date} \n[+]Age Restricted: {yt.age_restricted} \n[+]Video URL: {urlvid} \n[+]Video Description: {yt.description}")
        except:
            with open(f"""{yt.title.replace('|', 'x').replace('?', 'x').replace('>', 'x').replace('<', 'x').replace(':', 'x').replace(';', 'x').replace('"', "x").replace("'", "x")} - Information.txt""", "w", encoding="utf8") as fileinfotxt:
                fileinfotxt.write(f"[+]Title: {yt.title} \n[+]Thumnail URL: {yt.thumbnail_url} \n[+]Author: {yt.author} \n[+]Channel ID: {yt.channel_id} \n[+]Channel URL: {yt.channel_url} \n[+]Video Length: {yt.length} \n[+]Published Date:{yt.publish_date} \n[+]Age Restricted: {yt.age_restricted} \n[+]Video URL: {urlvid} \n[+]Video Description: {yt.description}")
        if show_text:
            print(f"[+] Wrote Information to {yt.title} - Information.txt")

    if download_subtitles:
        if show_text:
            print("\n[*] Trying to download subtitles/captions")
        try:
            caption = yt.captions.get_by_language_code('en')
            if show_text:
                print("[+] Successfully loaded subtitles/captions")
            try:
                try:
                    with open(f"{yt.title}.srt", "w", encoding="utf8") as filesrt:
                        filesrt.write(caption.generate_srt_captions())
                except:
                    try:
                        caption.generate_srt_captions()
                    except:
                        pass
            except OSError:
                try:
                    with open(f"""{yt.title.replace('|', 'x').replace('?', 'x').replace('>', 'x').replace('<', 'x').replace(':', 'x').replace(';', 'x').replace('"', "x").replace("'", "x")}.srt""", "w", encoding="utf8") as filesrt:
                        filesrt.write(caption.generate_srt_captions())
                except:
                    try:
                        caption.generate_srt_captions()
                    except:
                        pass
            if show_text:
                print("[+] Created a .srt file!")
        except:
            if show_text:
                print("[-] Unable to download subtitles")

    all_audio_qualities_tup = ("32kbps", "64kbps", "128kbps",
                               "160kbps", "192kbps", "240kbps", "256kbps", "320kbps")

    if qualityvid in all_audio_qualities_tup:
        if show_text:
            print("\n[*] Trying to downlod the audio")
        try:
            video = yt.streams.filter(only_audio=True).filter(
                abr=f"{qualityvid}").first().download()
            if show_text:
                print(f"[+] File downloaded successfully!\n{video}")
        except:
            if show_text:
                print(
                    "[*] Trying to download with the highest available quality for the audio")
            try:
                video = yt.streams.filter(only_audio=True).last().download()
                if show_text:
                    print(f"[+] File downloaded successfully!\n{video}")
            except:
                if show_text:
                    print(
                        "[*] Trying to download with the lowest available quality for the audio")
                try:
                    video = yt.streams.filter(
                        only_audio=True).first().download()
                    if show_text:
                        print(f"[+] File downloaded successfully!\n{video}")
                except:
                    if show_text:
                        print("[!!] FAILED")

    else:
        if show_text:
            print("\n[*] Trying to downlod the video")
        try:
            video = yt.streams.filter(res=f"{qualityvid}").filter(
                progressive=True).first().download()
            if show_text:
                print(f"[+] File downloaded successfully!\n{video}")
        except:
            if show_text:
                print(
                    "[*] Trying to download with the highest available quality for the video")
            try:
                video = yt.streams.filter(
                    progressive=True).get_highest_resolution().download()
                if show_text:
                    print(f"[+] File downloaded successfully!\n{video}")
            except:
                if show_text:
                    print(
                        "[*] Trying to download with the lowest available quality for the video")
                try:
                    video = yt.streams.filter(
                        progressive=True).get_highest_resolution()
                    if show_text:
                        print(f"[+] File downloaded successfully!\n{video}")
                except:
                    if show_text:
                        print("[!!] FAILED")
    
    allDownloaded.append(video)


# Canvas
# --------------------
canvas = Canvas(window, bg="#e3ffdc", height=518, width=786,
                bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"assets{BSP}background.png")
background = canvas.create_image(324.5, 272.5, image=background_img)


# Entry
# --------------------
entry0_img = PhotoImage(file=f"assets{BSP}img_textBox0.png")
entry0_bg = canvas.create_image(326.5, 172.5, image=entry0_img)

entry0 = Entry(bd=0, bg="#c4c4c4", highlightthickness=0)

entry0.place(x=122.0, y=146, width=409.0, height=51)

# Button - Download
# --------------------
img0 = PhotoImage(file=f"assets{BSP}img0.png")
b0 = Button(image=img0, borderwidth=0, highlightthickness=0,
            command=download_very_first_level, relief="flat", bg="#e3ffdc", activebackground="#e3ffdc")

b0.place(x=230, y=424, width=343, height=73)


# Button - Paste
# --------------------
img1 = PhotoImage(file=f"assets{BSP}img1.png")
b1 = Button(image=img1, borderwidth=0, highlightthickness=0,
            command=paste_yt_url, relief="flat", bg="#e3ffdc", activebackground="#e3ffdc")

b1.place(x=564, y=146, width=123, height=53)


# Button - Clear
# --------------------
img2 = PhotoImage(file=f"assets{BSP}img2.png")
b2 = Button(image=img2, borderwidth=0, highlightthickness=0,
            command=clear_yt_url, relief="flat", bg="#e3ffdc", activebackground="#e3ffdc")

b2.place(x=697, y=146, width=53, height=53)


# MunBar
# --------------------
menubar = Menu(window)
window.configure(menu=menubar)

sub_menu = Menu(window, tearoff=0)
menubar.add_cascade(menu=sub_menu, label="Main")
sub_menu.add_command(label="Download", command=download_very_first_level)
sub_menu.add_command(label="Paste URL", command=paste_yt_url)
sub_menu.add_command(label="Clear URL", command=clear_yt_url)
sub_menu.add_command(label="Exit", command=exit_program)

sub_menu_three = Menu(window, tearoff=0)
menubar.add_cascade(menu=sub_menu_three, label="Convert")
sub_menu_three.add_command(label="to MP3", command=to_mp3)
sub_menu_three.add_command(label="to MP4", command=to_mp4)
sub_menu_three.add_command(label="to MP3 - NVENC", command=to_mp3_nvenc)
sub_menu_three.add_command(label="to MP4 - NVENC", command=to_mp4_nvenc)

sub_menu_two = Menu(window, tearoff=0)
menubar.add_cascade(menu=sub_menu_two, label="Others")
# sub_menu_two.add_command(label="Support Us", command=lambda: webbrowser.open(
#     "https://www.youtube.com/c/HirushaAdikari?sub_confirmation=1"))
sub_menu_two.add_command(label="Privacy Policy", command=others_privacy_policy)
sub_menu_two.add_command(label="Source Code", command=others_source_code)
sub_menu_two.add_command(label="Help", command=others_help)


# Radio Buttons - Download Type
# --------------------
p1080_1_1_1 = Radiobutton(canvas, text="Playlist",
                          bg="#e3ffdc", activebackground="#e3ffdc")
p1080_1_1_1.configure(variable=vidut, value=1)
p1080_1_1_1.place(x=195, y=220)

p1080_1_1_1_1 = Radiobutton(
    canvas, text="Video", bg="#e3ffdc", activebackground="#e3ffdc")
p1080_1_1_1_1.configure(variable=vidut, value=2)
p1080_1_1_1_1.place(x=365, y=220)

p1080_1_1_1_1_1 = Radiobutton(
    canvas, text="Channel", bg="#e3ffdc", activebackground="#e3ffdc")
p1080_1_1_1_1_1.configure(variable=vidut, value=3)
p1080_1_1_1_1_1.place(x=535, y=220)


# Radio Buttons - Download Format/Quality
# --------------------
# Video
p1080_1_1 = Radiobutton(canvas, text="2160p",
                        bg="#e3ffdc", activebackground="#e3ffdc")
p1080_1_1.configure(variable=vidrf, value=10)
p1080_1_1.place(x=145, y=260)

p1080_1 = Radiobutton(canvas, text="1440p", bg="#e3ffdc",
                      activebackground="#e3ffdc")
p1080_1.configure(variable=vidrf, value=9)
p1080_1.place(x=230, y=260)

p1080 = Radiobutton(canvas, text="1080p", bg="#e3ffdc",
                    activebackground="#e3ffdc")
p1080.configure(variable=vidrf, value=1)
p1080.place(x=315, y=260)

p720 = Radiobutton(canvas, text="720p", bg="#e3ffdc",
                   activebackground="#e3ffdc")
p720.configure(variable=vidrf, value=2)
p720.place(x=145, y=290)

p480 = Radiobutton(canvas, text="480p", bg="#e3ffdc",
                   activebackground="#e3ffdc")
p480.configure(variable=vidrf, value=3)
p480.place(x=230, y=290)

p360 = Radiobutton(canvas, text="360p", bg="#e3ffdc",
                   activebackground="#e3ffdc")
p360.configure(variable=vidrf, value=4)
p360.place(x=315, y=290)

p240 = Radiobutton(canvas, text="240p", bg="#e3ffdc",
                   activebackground="#e3ffdc")
p240.configure(variable=vidrf, value=5)
p240.place(x=195, y=320)

p144 = Radiobutton(canvas, text="144p", bg="#e3ffdc",
                   activebackground="#e3ffdc")
p144.configure(variable=vidrf, value=6)
p144.place(x=275, y=320)

# Seperator
Seperator1 = ttk.Separator(canvas, orient="vertical")
Seperator1.place(x=390, y=265, height=90)

# Audio
f32kbps = Radiobutton(canvas, text="32kbps", bg="#e3ffdc",
                      activebackground="#e3ffdc")
f32kbps.configure(variable=vidrf, value=7)
f32kbps.place(x=410, y=260)

f64kbps = Radiobutton(canvas, text="64kbps", bg="#e3ffdc",
                      activebackground="#e3ffdc")
f64kbps.configure(variable=vidrf, value=8)
f64kbps.place(x=497, y=260)

f128kbps = Radiobutton(canvas, text="128kbps",
                       bg="#e3ffdc", activebackground="#e3ffdc")
f128kbps.configure(variable=vidrf, value=11)
f128kbps.place(x=575, y=260)

f160kbps = Radiobutton(canvas, text="160kbps",
                       bg="#e3ffdc", activebackground="#e3ffdc")
f160kbps.configure(variable=vidrf, value=12)
f160kbps.place(x=410, y=290)

f192kbps = Radiobutton(canvas, text="192kbps",
                       bg="#e3ffdc", activebackground="#e3ffdc")
f192kbps.configure(variable=vidrf, value=13)
f192kbps.place(x=497, y=290)

f256kbps = Radiobutton(canvas, text="256kbps",
                       bg="#e3ffdc", activebackground="#e3ffdc")
f256kbps.configure(variable=vidrf, value=14)
f256kbps.place(x=575, y=290)

f320kbps = Radiobutton(canvas, text="320kbps",
                       bg="#e3ffdc", activebackground="#e3ffdc")
f320kbps.configure(variable=vidrf, value=15)
f320kbps.place(x=497, y=320)

dl_subs = Checkbutton(canvas, text="Subtitles",
                      bg="#e3ffdc", activebackground="#e3ffdc")
dl_subs.configure(variable=dlsubs)
dl_subs.place(x=290, y=375)

dl_info = Checkbutton(canvas, text="Information",
                      bg="#e3ffdc", activebackground="#e3ffdc")
dl_info.configure(variable=dlvidinfo)
dl_info.place(x=434, y=375)




if __name__ == "__main__":
    try:
        window.mainloop()
    finally:
        images.DELETE_ALL()
