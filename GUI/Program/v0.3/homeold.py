# #########################
# Made by ZeaCeR#5641
# a.k.a Hirusha Adikari
# #########################

# Imports - Main
# -----------------------
import sys, platform, os

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from tkinter import messagebox, filedialog

try:
        import clipboard
except ImportError:
        if platform.system().lower().startswith('win'):
                os.system("pip install clipboard")
        else:
                os.system("pip3 install clipboard")
        import clipboard

import webbrowser

try:
        from pytube import *
except ImportError:
        if platform.system().lower().startswith('win'):
                os.system("pip install pytube")
        else:
                os.system("pip3 install pytube")
        from pytube import *

# Import - Support
# -----------------------
import home_support
import importantstuff

# import fkingshit

# Import - Other Windows
# -----------------------
# import whyfree
import credits


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    home_support.set_Tk_var()
    top = Toplevel1 (root)
    home_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    home_support.set_Tk_var()
    top = Toplevel1 (w)
    home_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x370+786+240")
        top.minsize(117, 1)
        top.maxsize(4644, 1274)
        top.resizable(False,  False)
        top.title("YouTube Video Downloader by ZeaCeR")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        # PASE BUTTONS
        # Get a string from what is in your clipboard, clear the entry and insert it
        # -----------------------
        def paste_yt_url():
                self.clipboarddata_yturl = clipboard.paste() 
                self.urlhere.delete(0,"end")
                self.urlhere.insert(0, self.clipboarddata_yturl)

        # CLEAR BUTTONS
        # -----------------------
        def clear_yt_url():
                self.urlhere.delete(0, "end")
        
        def clear_filepath():
                self.pathhere.delete(0, "end")
                
        # Radio Button Variable for Video Quality / Format
        # -----------------------
        self.vidrf = tk.IntVar()
        self.vidrf.set("2")
        # 2160p -> 10
        # 1440p -> 9
        # 1080p -> 1
        # 720p -> 2
        # 480p -> 3
        # 360p -> 4
        # 240p -> 5
        # 144p -> 6 

        # 32kbps -> 7
        # 64kbps -> 8
        # 128kbps -> 11
        # 160kbps -> 12
        # 192kbps -> 13
        # 256kbps -> 14
        # 320kbps -> 15


        # Radio Button Variable for Usage Type
        # -----------------------
        self.vidut = tk.IntVar()
        self.vidut.set("2")
        # Playlist -> 1
        # a Video -> 2
        # Channel -> 3

        # FUCKING QUALITY
        # -----------------------
        def select_dl_quality(selectquality):
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
                        print("[*] Selected default - Something is wrong! Please report to a developer")
                        return "480p"
        
        def select_dl_type(fuckingshit=2):
                if fuckingshit == 1:
                        return "playlist"
                elif fuckingshit == 2:
                        return "video"
                elif fuckingshit == 3:
                        return "channel"
                else:   
                        print("[*] Selecting Default value: Video - Something is wrong, please report to a developer")
                        return "video"




        # Get the value of the selected Radio Button
        # -----------------------
        def selected_val():
                rsvrb = self.vidrf.get()
                return rsvrb
        
        # What type of download?
        # -----------------------
        def selected_download_type():
                rsvub = self.vidut.get()
                return rsvub



        # Menu Bar commands - Files Cascade
        # -----------------------
        # Paset URL
        def menubar_paste_yt_url():
                paste_yt_url()

        # Exit
        def quitapp_whole():
                exit()
        
        # Menu Bar commands - Others Cascade
        # -----------------------

        # Credits
        def others_credits():
                top.destroy()
                credits.vp_start_gui()
        
        # Contributers
        # I thought of not adding an seperate windows for this
        # Instead, this will open the github repo links contributers part
        # Its the same for Privacy Policy and Help

        def others_privacy_policy():
                webbrowser.open(importantstuff.privacy_policy)
        
        def others_help():
                webbrowser.open(importantstuff.helplink)
        

        # ###############################################################
        # This is most likely where i fuck up


        # DOWNLOAD FUNCTIONS
        # Level 1
        def download_first_level():
                videoquality = selected_val()
                whattypeofdl = selected_download_type()

                qualityintexttp = select_dl_quality(videoquality)
                downloadtypeintexttp = select_dl_type(whattypeofdl)

                fuckingurlmf = self.urlhere.get()

                if downloadtypeintexttp == "video":
                        # fkingshit.FUCKING_DOWNLOAD_ONE_VIDEO(qualityvid=qualityintexttp, vidurl=fuckingurlmf)
                        FUCKING_DOWNLOAD_ONE_VIDEO(qualityvid=qualityintexttp, urlvid=fuckingurlmf)

                elif downloadtypeintexttp == "playlist":
                        pl = Playlist(f'{fuckingurlmf}')
                        for url in pl.video_urls:
                                FUCKING_DOWNLOAD_ONE_VIDEO(qualityvid=qualityintexttp, urlvid=url)
                
                elif downloadtypeintexttp == "channel":
                        cl = Channel(f'{fuckingurlmf}')
                        for url in cl.video_urls:
                                FUCKING_DOWNLOAD_ONE_VIDEO(qualityvid=qualityintexttp, urlvid=url)
                
                else:
                        if downloadtypeintexttp == "video":
                                # fkingshit.FUCKING_DOWNLOAD_ONE_VIDEO(qualityvid=qualityintexttp, vidurl=fuckingurlmf)
                                FUCKING_DOWNLOAD_ONE_VIDEO(qualityvid=qualityintexttp, vidurl=fuckingurlmf)




        # Level 2 - The main download function
        def FUCKING_DOWNLOAD_ONE_VIDEO(qualityvid, urlvid):
                print(f"[*] Recieved a download quality of {qualityvid} to {urlvid}")
                try:
                        yt = YouTube(urlvid)
                except VideoUnavailable:
                        print("[!!] VIDEO UNAVAILABLE!")
                        return
                except Exception as e:
                        print("Error", e)
                        return
                print("[+] Object Initiated")
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
                all_audio_qualities_tup = ("32kbps", "64kbps", "128kbps", "160kbps", "192kbps", "240kbps", "256kbps", "320kbps")
                
                if qualityvid in all_audio_qualities_tup:
                        print("\n[*] Trying to downlod the audio")
                        try:
                                video = yt.streams.filter(only_audio=True).filter(abr=f"{qualityvid}").first().download()
                                print(f"[+] File downloaded successfully!\n{video}")
                        except:
                                print("[-] An Error has occured!")
                                print("[*] Trying to download with the highest available quality for the audio")
                                try:
                                        video = yt.streams.filter(only_audio=True).last().download()
                                        print(f"[+] File downloaded successfully!\n{video}")
                                except:
                                        print("[-] Failed!")
                                        print("[*] Trying to download with the lowest available quality for the audio")
                                        try:    
                                                video = yt.streams.filter(only_audio=True).first().download()
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






        self.Topic = tk.Label(top)
        self.Topic.place(relx=-0.017, rely=0.0, height=50, width=614)
        self.Topic.configure(activebackground="#ffffff")
        self.Topic.configure(activeforeground="#fd0006")
        self.Topic.configure(background="#ffffff")
        self.Topic.configure(disabledforeground="#a3a3a3")
        self.Topic.configure(font="-family {Showcard Gothic} -size 22")
        self.Topic.configure(foreground="#ff2227")
        self.Topic.configure(highlightbackground="#d9d9d9")
        self.Topic.configure(highlightcolor="black")
        self.Topic.configure(text='''YouTube Video Downloader''')

        self.urlhere = tk.Entry(top)
        self.urlhere.place(relx=0.033, rely=0.257, height=60, relwidth=0.573)
        self.urlhere.configure(background="#eeeeee")
        self.urlhere.configure(disabledforeground="#a3a3a3")
        self.urlhere.configure(font="-family {Courier New} -size 17")
        self.urlhere.configure(foreground="#000000")
        self.urlhere.configure(highlightbackground="#d9d9d9")
        self.urlhere.configure(highlightcolor="black")
        self.urlhere.configure(insertbackground="black")
        self.urlhere.configure(selectbackground="blue")
        self.urlhere.configure(selectforeground="white")

        self.btnpaste = tk.Button(top)
        self.btnpaste.place(relx=0.633, rely=0.243, height=54, width=147)
        self.btnpaste.configure(activebackground="#ececec")
        self.btnpaste.configure(activeforeground="#000000")
        self.btnpaste.configure(background="#1abe07")
        self.btnpaste.configure(disabledforeground="#4646ff")
        self.btnpaste.configure(font="-family {Showcard Gothic} -size 16")
        self.btnpaste.configure(foreground="#ffffff")
        self.btnpaste.configure(highlightbackground="#d2dcdf")
        self.btnpaste.configure(highlightcolor="#000000")
        self.btnpaste.configure(pady="0")
        self.btnpaste.configure(text='''+ Paste''')
        self.btnpaste.configure(command=paste_yt_url)

        self.btndownload = tk.Button(top)
        self.btndownload.place(relx=0.033, rely=0.595, height=84, width=337)
        self.btndownload.configure(activebackground="#ececec")
        self.btndownload.configure(activeforeground="#000000")
        self.btndownload.configure(background="#1681c0")
        self.btndownload.configure(disabledforeground="#a3a3a3")
        self.btndownload.configure(font="-family {Showcard Gothic} -size 18")
        self.btndownload.configure(foreground="#ffffff")
        self.btndownload.configure(highlightbackground="#d9d9d9")
        self.btndownload.configure(highlightcolor="black")
        self.btndownload.configure(pady="0")
        self.btndownload.configure(text='''⬇ Download''')
        self.btndownload.configure(command=download_first_level)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.883, rely=0.243, height=54, width=57)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ff5155")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Showcard Gothic} -size 17")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''X''')
        self.Button1.configure(command=clear_yt_url)

        self.Topic_1 = tk.Label(top)
        self.Topic_1.place(relx=0.05, rely=0.157, height=26, width=164)
        self.Topic_1.configure(activebackground="#ffffff")
        self.Topic_1.configure(activeforeground="#fd0006")
        self.Topic_1.configure(background="#ffffff")
        self.Topic_1.configure(disabledforeground="#a3a3a3")
        self.Topic_1.configure(font="-family {Showcard Gothic} -size 17")
        self.Topic_1.configure(foreground="#ff2227")
        self.Topic_1.configure(highlightbackground="#d9d9d9")
        self.Topic_1.configure(highlightcolor="black")
        self.Topic_1.configure(text='''YouTube Link''')

        self.p1080 = tk.Radiobutton(top)
        self.p1080.place(relx=0.633, rely=0.589, relheight=0.057, relwidth=0.18)
        self.p1080.configure(activebackground="#ececec")
        self.p1080.configure(activeforeground="#000000")
        self.p1080.configure(background="#ffffff")
        self.p1080.configure(disabledforeground="#a3a3a3")
        self.p1080.configure(font="-family {Showcard Gothic} -size 9")
        self.p1080.configure(foreground="#000000")
        self.p1080.configure(highlightbackground="#d9d9d9")
        self.p1080.configure(highlightcolor="black")
        self.p1080.configure(justify='left')
        self.p1080.configure(text='''1080p''')
        self.p1080.configure(variable=home_support.selectedButton)
        self.p1080.configure(variable=self.vidrf)
        self.p1080.configure(value=1)

        self.p720 = tk.Radiobutton(top)
        self.p720.place(relx=0.633, rely=0.668, relheight=0.057, relwidth=0.18)
        self.p720.configure(activebackground="#ececec")
        self.p720.configure(activeforeground="#000000")
        self.p720.configure(background="white")
        self.p720.configure(disabledforeground="#a3a3a3")
        self.p720.configure(font="-family {Showcard Gothic} -size 9")
        self.p720.configure(foreground="#000000")
        self.p720.configure(highlightbackground="#d9d9d9")
        self.p720.configure(highlightcolor="black")
        self.p720.configure(justify='left')
        self.p720.configure(text='''720p''')
        self.p720.configure(variable=home_support.selectedButton)
        self.p720.configure(variable=self.vidrf)
        self.p720.configure(value=2)

        self.p480 = tk.Radiobutton(top)
        self.p480.place(relx=0.633, rely=0.732, relheight=0.057, relwidth=0.18)
        self.p480.configure(activebackground="#ececec")
        self.p480.configure(activeforeground="#000000")
        self.p480.configure(background="white")
        self.p480.configure(disabledforeground="#a3a3a3")
        self.p480.configure(font="-family {Showcard Gothic} -size 9")
        self.p480.configure(foreground="#000000")
        self.p480.configure(highlightbackground="#d9d9d9")
        self.p480.configure(highlightcolor="black")
        self.p480.configure(justify='left')
        self.p480.configure(text='''480p''')
        self.p480.configure(variable=home_support.selectedButton)

        self.p360 = tk.Radiobutton(top)
        self.p360.place(relx=0.633, rely=0.8, relheight=0.057, relwidth=0.18)
        self.p360.configure(activebackground="#ececec")
        self.p360.configure(activeforeground="#000000")
        self.p360.configure(background="white")
        self.p360.configure(disabledforeground="#a3a3a3")
        self.p360.configure(font="-family {Showcard Gothic} -size 9")
        self.p360.configure(foreground="#000000")
        self.p360.configure(highlightbackground="#d9d9d9")
        self.p360.configure(highlightcolor="black")
        self.p360.configure(justify='left')
        self.p360.configure(text='''360p''')
        self.p360.configure(variable=home_support.selectedButton)
        self.p360.configure(variable=self.vidrf)
        self.p360.configure(value=4)

        self.p240 = tk.Radiobutton(top)
        self.p240.place(relx=0.633, rely=0.873, relheight=0.054, relwidth=0.18)
        self.p240.configure(activebackground="#ececec")
        self.p240.configure(activeforeground="#000000")
        self.p240.configure(background="white")
        self.p240.configure(disabledforeground="#a3a3a3")
        self.p240.configure(font="-family {Showcard Gothic} -size 9")
        self.p240.configure(foreground="#000000")
        self.p240.configure(highlightbackground="#d9d9d9")
        self.p240.configure(highlightcolor="black")
        self.p240.configure(justify='left')
        self.p240.configure(text='''240p''')
        self.p240.configure(variable=home_support.selectedButton)
        self.p240.configure(variable=self.vidrf)
        self.p240.configure(value=5)

        self.p144 = tk.Radiobutton(top)
        self.p144.place(relx=0.633, rely=0.932, relheight=0.057, relwidth=0.18)
        self.p144.configure(activebackground="#ececec")
        self.p144.configure(activeforeground="#000000")
        self.p144.configure(background="white")
        self.p144.configure(disabledforeground="#a3a3a3")
        self.p144.configure(font="-family {Showcard Gothic} -size 9")
        self.p144.configure(foreground="#000000")
        self.p144.configure(highlightbackground="#d9d9d9")
        self.p144.configure(highlightcolor="black")
        self.p144.configure(justify='left')
        self.p144.configure(text='''144p''')
        self.p144.configure(variable=home_support.selectedButton)
        self.p144.configure(variable=self.vidrf)
        self.p144.configure(value=6)

        self.f32kbps = tk.Radiobutton(top)
        self.f32kbps.place(relx=0.833, rely=0.924, relheight=0.054
                , relwidth=0.147)
        self.f32kbps.configure(activebackground="#ececec")
        self.f32kbps.configure(activeforeground="#000000")
        self.f32kbps.configure(background="#ffffff")
        self.f32kbps.configure(disabledforeground="#a3a3a3")
        self.f32kbps.configure(font="-family {Showcard Gothic} -size 9")
        self.f32kbps.configure(foreground="#000000")
        self.f32kbps.configure(highlightbackground="#d9d9d9")
        self.f32kbps.configure(highlightcolor="black")
        self.f32kbps.configure(justify='left')
        self.f32kbps.configure(text='''32kbps''')
        self.f32kbps.configure(variable=home_support.selectedButton)
        self.f32kbps.configure(variable=self.vidrf)
        self.f32kbps.configure(value=7)

        self.f64kbps = tk.Radiobutton(top)
        self.f64kbps.place(relx=0.833, rely=0.846, relheight=0.057
                , relwidth=0.147)
        self.f64kbps.configure(activebackground="#ececec")
        self.f64kbps.configure(activeforeground="#000000")
        self.f64kbps.configure(background="#ffffff")
        self.f64kbps.configure(disabledforeground="#a3a3a3")
        self.f64kbps.configure(font="-family {Showcard Gothic} -size 9")
        self.f64kbps.configure(foreground="#000000")
        self.f64kbps.configure(highlightbackground="#d9d9d9")
        self.f64kbps.configure(highlightcolor="black")
        self.f64kbps.configure(justify='left')
        self.f64kbps.configure(text='''64kbps''')
        self.f64kbps.configure(variable=home_support.selectedButton)
        self.f64kbps.configure(variable=self.vidrf)
        self.f64kbps.configure(value=8)

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.817, rely=0.441,  relheight=0.538)
        self.TSeparator1.configure(orient="vertical")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                label="File")
        self.sub_menu.add_command(
                label="Paste URL",
                command=menubar_paste_yt_url)
        # self.sub_menu.add_command(
        #         label="Paste Save Path")
        self.sub_menu.add_command(
                label="Exit", 
                command=quitapp_whole)

        self.menubar.add_separator()

        self.sub_menu1 = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu1,
                label="Others")
        self.sub_menu1.add_command(
                label="Credits", command=others_credits)
        self.sub_menu1.add_command(
                label="Privacy Policy", command=others_privacy_policy)
        self.sub_menu1.add_command(
                label="Help", command=others_help)

        self.TSeparator1_1 = ttk.Separator(top)
        self.TSeparator1_1.place(relx=0.625, rely=0.438,  relheight=0.535)
        self.TSeparator1_1.configure(orient="vertical")

        self.Lcreditsbottom = tk.Label(top)
        self.Lcreditsbottom.place(relx=0.05, rely=0.892, height=34, width=304)
        self.Lcreditsbottom.configure(activebackground="#f9f9f9")
        self.Lcreditsbottom.configure(activeforeground="black")
        self.Lcreditsbottom.configure(background="#ffffff")
        self.Lcreditsbottom.configure(disabledforeground="#a3a3a3")
        self.Lcreditsbottom.configure(foreground="#000000")
        self.Lcreditsbottom.configure(highlightbackground="#d9d9d9")
        self.Lcreditsbottom.configure(highlightcolor="black")
        self.Lcreditsbottom.configure(text='''YouTube Video Downloader by ZeaCeR#5641 - v0.2''')

        self.p1080_1 = tk.Radiobutton(top)
        self.p1080_1.place(relx=0.633, rely=0.514, relheight=0.057
                , relwidth=0.18)
        self.p1080_1.configure(activebackground="#ececec")
        self.p1080_1.configure(activeforeground="#000000")
        self.p1080_1.configure(background="#ffffff")
        self.p1080_1.configure(disabledforeground="#a3a3a3")
        self.p1080_1.configure(font="-family {Showcard Gothic} -size 9")
        self.p1080_1.configure(foreground="#000000")
        self.p1080_1.configure(highlightbackground="#d9d9d9")
        self.p1080_1.configure(highlightcolor="black")
        self.p1080_1.configure(justify='left')
        self.p1080_1.configure(text='''1440p''')
        self.p1080_1.configure(variable=home_support.selectedButton)
        self.p1080_1.configure(variable=self.vidrf)
        self.p1080_1.configure(value=9)

        self.p1080_1_1 = tk.Radiobutton(top)
        self.p1080_1_1.place(relx=0.633, rely=0.432, relheight=0.057
                , relwidth=0.18)
        self.p1080_1_1.configure(activebackground="#ececec")
        self.p1080_1_1.configure(activeforeground="#000000")
        self.p1080_1_1.configure(background="#ffffff")
        self.p1080_1_1.configure(disabledforeground="#a3a3a3")
        self.p1080_1_1.configure(font="-family {Showcard Gothic} -size 9")
        self.p1080_1_1.configure(foreground="#000000")
        self.p1080_1_1.configure(highlightbackground="#d9d9d9")
        self.p1080_1_1.configure(highlightcolor="black")
        self.p1080_1_1.configure(justify='left')
        self.p1080_1_1.configure(text='''2160p''')
        self.p1080_1_1.configure(variable=home_support.selectedButton)
        self.p1080_1_1.configure(variable=self.vidrf)
        self.p1080_1_1.configure(value=10)

        self.f128kbps = tk.Radiobutton(top)
        self.f128kbps.place(relx=0.833, rely=0.77, relheight=0.054
                , relwidth=0.147)
        self.f128kbps.configure(activebackground="#ececec")
        self.f128kbps.configure(activeforeground="#000000")
        self.f128kbps.configure(background="#ffffff")
        self.f128kbps.configure(disabledforeground="#a3a3a3")
        self.f128kbps.configure(font="-family {Showcard Gothic} -size 9")
        self.f128kbps.configure(foreground="#000000")
        self.f128kbps.configure(highlightbackground="#d9d9d9")
        self.f128kbps.configure(highlightcolor="black")
        self.f128kbps.configure(justify='left')
        self.f128kbps.configure(text='''128kbps''')
        self.f128kbps.configure(variable=home_support.selectedButton)
        self.f128kbps.configure(variable=self.vidrf)
        self.f128kbps.configure(value=11)

        self.f160kbps = tk.Radiobutton(top)
        self.f160kbps.place(relx=0.833, rely=0.692, relheight=0.057
                , relwidth=0.147)
        self.f160kbps.configure(activebackground="#ececec")
        self.f160kbps.configure(activeforeground="#000000")
        self.f160kbps.configure(background="#ffffff")
        self.f160kbps.configure(disabledforeground="#a3a3a3")
        self.f160kbps.configure(font="-family {Showcard Gothic} -size 9")
        self.f160kbps.configure(foreground="#000000")
        self.f160kbps.configure(highlightbackground="#d9d9d9")
        self.f160kbps.configure(highlightcolor="black")
        self.f160kbps.configure(justify='left')
        self.f160kbps.configure(text='''160kbps''')
        self.f160kbps.configure(variable=home_support.selectedButton)
        self.f160kbps.configure(variable=self.vidrf)
        self.f160kbps.configure(value=12)

        self.f192kbps = tk.Radiobutton(top)
        self.f192kbps.place(relx=0.833, rely=0.616, relheight=0.054
                , relwidth=0.147)
        self.f192kbps.configure(activebackground="#ececec")
        self.f192kbps.configure(activeforeground="#000000")
        self.f192kbps.configure(background="#ffffff")
        self.f192kbps.configure(disabledforeground="#a3a3a3")
        self.f192kbps.configure(font="-family {Showcard Gothic} -size 9")
        self.f192kbps.configure(foreground="#000000")
        self.f192kbps.configure(highlightbackground="#d9d9d9")
        self.f192kbps.configure(highlightcolor="black")
        self.f192kbps.configure(justify='left')
        self.f192kbps.configure(text='''192kbps''')
        self.f192kbps.configure(variable=home_support.selectedButton)
        self.f192kbps.configure(variable=self.vidrf)
        self.f192kbps.configure(value=13)

        self.f256kbps = tk.Radiobutton(top)
        self.f256kbps.place(relx=0.833, rely=0.541, relheight=0.057
                , relwidth=0.147)
        self.f256kbps.configure(activebackground="#ececec")
        self.f256kbps.configure(activeforeground="#000000")
        self.f256kbps.configure(background="#ffffff")
        self.f256kbps.configure(disabledforeground="#a3a3a3")
        self.f256kbps.configure(font="-family {Showcard Gothic} -size 9")
        self.f256kbps.configure(foreground="#000000")
        self.f256kbps.configure(highlightbackground="#d9d9d9")
        self.f256kbps.configure(highlightcolor="black")
        self.f256kbps.configure(justify='left')
        self.f256kbps.configure(text='''256kbps''')
        self.f256kbps.configure(variable=home_support.selectedButton)
        self.f256kbps.configure(variable=self.vidrf)
        self.f256kbps.configure(value=14)

        self.f320kbps = tk.Radiobutton(top)
        self.f320kbps.place(relx=0.833, rely=0.459, relheight=0.057
                , relwidth=0.147)
        self.f320kbps.configure(activebackground="#ececec")
        self.f320kbps.configure(activeforeground="#000000")
        self.f320kbps.configure(background="#ffffff")
        self.f320kbps.configure(disabledforeground="#a3a3a3")
        self.f320kbps.configure(font="-family {Showcard Gothic} -size 9")
        self.f320kbps.configure(foreground="#000000")
        self.f320kbps.configure(highlightbackground="#d9d9d9")
        self.f320kbps.configure(highlightcolor="black")
        self.f320kbps.configure(justify='left')
        self.f320kbps.configure(text='''320kbps''')
        self.f320kbps.configure(variable=home_support.selectedButton)
        self.f320kbps.configure(variable=self.vidrf)
        self.f320kbps.configure(value=15)

        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=0.617, rely=0.432,  relwidth=0.4)

        self.p1080_1_1_1 = tk.Radiobutton(top)
        self.p1080_1_1_1.place(relx=0.033, rely=0.459, relheight=0.057
                , relwidth=0.18)
        self.p1080_1_1_1.configure(activebackground="#ececec")
        self.p1080_1_1_1.configure(activeforeground="#000000")
        self.p1080_1_1_1.configure(background="#ffffff")
        self.p1080_1_1_1.configure(disabledforeground="#a3a3a3")
        self.p1080_1_1_1.configure(font="-family {Showcard Gothic} -size 9")
        self.p1080_1_1_1.configure(foreground="#000000")
        self.p1080_1_1_1.configure(highlightbackground="#d9d9d9")
        self.p1080_1_1_1.configure(highlightcolor="black")
        self.p1080_1_1_1.configure(justify='left')
        self.p1080_1_1_1.configure(text='''Playlist''')
        self.p1080_1_1_1.configure(variable=home_support.selectedButton)
        self.p1080_1_1_1.configure(variable=self.vidut)
        self.p1080_1_1_1.configure(value=1)

        self.p1080_1_1_1_1 = tk.Radiobutton(top)
        self.p1080_1_1_1_1.place(relx=0.217, rely=0.459, relheight=0.057
                , relwidth=0.18)
        self.p1080_1_1_1_1.configure(activebackground="#ececec")
        self.p1080_1_1_1_1.configure(activeforeground="#000000")
        self.p1080_1_1_1_1.configure(background="#ffffff")
        self.p1080_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.p1080_1_1_1_1.configure(font="-family {Showcard Gothic} -size 9")
        self.p1080_1_1_1_1.configure(foreground="#000000")
        self.p1080_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.p1080_1_1_1_1.configure(highlightcolor="black")
        self.p1080_1_1_1_1.configure(justify='left')
        self.p1080_1_1_1_1.configure(text='''Video''')
        self.p1080_1_1_1_1.configure(variable=home_support.selectedButton)
        self.p1080_1_1_1_1.configure(variable=self.vidut)
        self.p1080_1_1_1_1.configure(value=2)

        self.p1080_1_1_1_1_1 = tk.Radiobutton(top)
        self.p1080_1_1_1_1_1.place(relx=0.417, rely=0.459, relheight=0.057
                , relwidth=0.18)
        self.p1080_1_1_1_1_1.configure(activebackground="#ececec")
        self.p1080_1_1_1_1_1.configure(activeforeground="#000000")
        self.p1080_1_1_1_1_1.configure(background="#ffffff")
        self.p1080_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.p1080_1_1_1_1_1.configure(font="-family {Showcard Gothic} -size 9")
        self.p1080_1_1_1_1_1.configure(foreground="#000000")
        self.p1080_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.p1080_1_1_1_1_1.configure(highlightcolor="black")
        self.p1080_1_1_1_1_1.configure(justify='left')
        self.p1080_1_1_1_1_1.configure(text='''Channel''')
        self.p1080_1_1_1_1_1.configure(variable=home_support.selectedButton)
        self.p1080_1_1_1_1_1.configure(value=3)






# if __name__ == '__main__':
#     vp_start_gui()





