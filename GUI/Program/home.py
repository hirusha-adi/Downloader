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

# Import - Other Windows
# -----------------------
import whyfree
import credits



# Some more useful functions that support the GUI
# -----------------------
def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    home_support.set_Tk_var()
    top = Toplevel1 (root)
    home_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    global w, w_win, root
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

# The GUI
# -----------------------
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

        top.geometry("600x410+820+199")
        top.minsize(117, 1)
        top.maxsize(4644, 1274)
        top.resizable(False,  False)
        top.title("YouTube Video Downloader by ZeaCeR")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        # Download Functions
        # -----------------------
        def download_video_quality(quality="720p", vidurl="http://youtube.com/watch?v=2lAe1cqCOXo"):
                try:
                        yt = YouTube(vidurl)

                        print(f"+ Obtaining Information of '{yt.title}'")

                        with open(f"{self.download_Directory}\\{yt.title}.txt") as filetxt:
                                try:
                                        filetxt.write(f"Title: {yt.title} \nThumnail URL: {yt.thumbnail_url} \nVideo Description: {yt.description} \nAuthor: {yt.author} \nChannel ID: {yt.channel_id} \nChannel URL: {yt.channel_url} \nVideo Length: {yt.length} \nPublished Date:{yt.publish_date} \nAge Restricted: {yt.age_restricted} \nVideo URL: {vidurl}")
                                except Exception as e:
                                        filetxt.write(f"An error has occured: {e}")
                                print(f"+ Wrote Video information to file: {self.download_Directory}\\{yt.title}.txt")
                        
                        print("* Trying do downlaod subtitles")
                        try:
                                caption = yt.captions.get_by_language_code('en')
                                print("+ Subtitles have been loaded")
                                print("* Generating .srt file")
                                try:
                                        captionssrt = caption.generate_srt_captions()
                                        with open(f"{self.download_Directory}\\{yt.title}.txt") as filecaptxt:
                                                filecaptxt.write(captionssrt)
                                except:
                                        print("- Unable to Generate subtitles")
                        except:
                                print("- Unable to Generate subtitles")

                        print(f"* Trying to downlod video{yt.title}")

                        try:    
                                try:
                                        ytvideo = yt.streams.filter(f"{quality}").first().download()
                                except:
                                        print(f"- Unable to download the file from the given quality: {quality}")
                                        print("* Trying to download from the highest possible quality")
                                        try:
                                                ytvideo = yt.streams.get_highest_resolution.download()
                                        except:
                                                print("- UNABLE TO DOWNLOAD THE FILE!")
                                                return
                                print(f"+ Downloaded {yt.title} Successfully!")
                                try:
                                        print("* Renaming file")
                                        os.rename(ytvideo, f"{yt.title.replace(' ', '_')}.mp4")
                                        print(f"+ Renamed file from {ytvideo} to {yt.title.replace(' ', '_')}.mp4")
                                except:
                                        print("- Unable to rename file")
                        except:
                                print("- Unable to download file")
                                return
                        
                        print("* Moving file from downloaded dir to specified dir")

                        try:
                                os.system(f"mv {yt.title.replace(' ', '_')}.mp4 {self.download_Directory}")
                                print("+ COMPLETED!")
                        except Exception as e:
                                print("- Unable to copy the file to the specified path!")
                                print("Error", e)
                                
                except VideoUnavailable:
                        print(f"{vidurl} if not available!")
                
        
        def download_playlist(vidquality, urlplaylist):
                p = Playlist(urlplaylist)
                for video in p.videos:
                        download_video_quality(vidquality, video)




        # PASE BUTTONS
        # Get a string from what is in your clipboard, clear the entry and insert it
        # -----------------------
        def paste_yt_url():
                self.clipboarddata_yturl = clipboard.paste() 
                self.urlhere.delete(0,"end")
                self.urlhere.insert(0, self.clipboarddata_yturl)

        # Get a string from what is in your clipboard, clear the entry and insert it
        def paste_filepath():
                # OLD CODE
                # self.clipboarddata_yturl = clipboard.paste() 
                # self.pathhere.delete(0,"end")
                # self.pathhere.insert(0, self.clipboarddata_yturl)

                # NEW CODE
                self.download_Directory = filedialog.askdirectory(
                title="Save Video"
                # ,initialdir="C:\\"
                )
                self.pathhere.delete(0,"end")
                self.pathhere.insert(0, self.download_Directory)

        # CLEAR BUTTONS
        # -----------------------
        def clear_yt_url():
                self.urlhere.delete(0, "end")
        
        def clear_filepath():
                self.pathhere.delete(0, "end")
                
        # Radio Button Variable
        # -----------------------
        self.vidrf = tk.IntVar()
        self.vidrf.set("2")
        # 1080p -> 1
        # 720p -> 2
        # 480p -> 3
        # 360p -> 4
        # 240p -> 5
        # 144p -> 6 
        # MP3 -> 7
        # MP3 HQ - 8

        # Get the value of the selected Radio Button
        # -----------------------
        def selected_val():
                rsvrb = self.vidrf.get()
                return rsvrb
        
        # Menu Bar commands - Files Cascade
        # -----------------------
        # Paset URL
        def menubar_paste_yt_url():
                paste_yt_url()
        
        # Paste File Path
        def menubar_paste_filepath():
                paste_filepath()

        # Exit
        def quitapp_whole():
                exit()
        
        # Menu Bar commands - Others Cascade
        # -----------------------

        # Why Free?
        def others_why_free():
                top.destroy()
                whyfree.vp_start_gui()
        
        # Credits
        def others_credits():
                top.destroy()
                credits.vp_start_gui()
        
        # Contributers
        # I thought of not adding an seperate windows for this
        # Instead, this will open the github repo links contributers part
        # Its the same for Privacy Policy and Help
        def others_contributors():
                webbrowser.open(importantstuff.contributors)

        def others_privacy_policy():
                webbrowser.open(importantstuff.privacy_policy)
        
        def others_help():
                webbrowser.open(importantstuff.helplink)

        # DOWNLOAD BUTTON
        # ----------------------
        # This is the main part of the code
        def download_button_function():
                self.playlistyn = messagebox.askyesno(title='Playlist or Video', message='Yes if the is link a playlist. No if its a single video')
                videourlyt = self.urlhere.get() 
                if self.playlistyn:
                        print("Its a playlist")
                        squalityframes = selected_val()

                        if squalityframes == 1:
                                print("1080p")

                        elif squalityframes == 2:
                                print("720p")
                        
                        elif squalityframes == 3:
                                print("480p")
                        
                        elif squalityframes == 4:
                                print("360p")
                                download_video_quality("360p", videourlyt)
                        
                        elif squalityframes == 5:
                                print("240p")
                        
                        elif squalityframes == 6:
                                print("144p")
                        
                        elif squalityframes == 7:
                                print("MP3")
                        
                        elif squalityframes == 8:
                                print("MP3 HQ | MP3 High Quality")
                        
                        else:
                                print("something is wrong")
                        
                        
                else:
                        print("Its a single video")
                        squalityframes = selected_val()

                        if squalityframes == 1:
                                print("1080p")

                        elif squalityframes == 2:
                                print("720p")
                        
                        elif squalityframes == 3:
                                print("480p")
                        
                        elif squalityframes == 4:
                                print("360p")
                        
                        elif squalityframes == 5:
                                print("240p")
                        
                        elif squalityframes == 6:
                                print("144p")
                        
                        elif squalityframes == 7:
                                print("MP3")
                        
                        elif squalityframes == 8:
                                print("MP3 HQ | MP3 High Quality")
                        
                        else:
                                print("something is wrong")
        



        self.Topic = tk.Label(top)
        self.Topic.place(relx=-0.017, rely=0.0, height=55, width=614)
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
        self.urlhere.place(relx=0.067, rely=0.244, height=50, relwidth=0.54)
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
        self.btnpaste.place(relx=0.633, rely=0.244, height=64, width=147)
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
        self.btndownload.place(relx=0.067, rely=0.634, height=84, width=327)
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
        self.btndownload.configure(command=download_button_function)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.883, rely=0.244, height=64, width=57)
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

        self.pathhere = tk.Entry(top)
        self.pathhere.place(relx=0.067, rely=0.466, height=50, relwidth=0.54)
        self.pathhere.configure(background="#eeeeee")
        self.pathhere.configure(disabledforeground="#a3a3a3")
        self.pathhere.configure(font="-family {Courier New} -size 17")
        self.pathhere.configure(foreground="#000000")
        self.pathhere.configure(highlightbackground="#d9d9d9")
        self.pathhere.configure(highlightcolor="black")
        self.pathhere.configure(insertbackground="black")
        self.pathhere.configure(selectbackground="blue")
        self.pathhere.configure(selectforeground="white")

        self.Button1_1 = tk.Button(top)
        self.Button1_1.place(relx=0.883, rely=0.422, height=64, width=57)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#ff5155")
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font="-family {Showcard Gothic} -size 17")
        self.Button1_1.configure(foreground="#ffffff")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''X''')
        self.Button1_1.configure(command=clear_filepath)

        self.Topic_1 = tk.Label(top)
        self.Topic_1.place(relx=0.05, rely=0.156, height=29, width=164)
        self.Topic_1.configure(activebackground="#ffffff")
        self.Topic_1.configure(activeforeground="#fd0006")
        self.Topic_1.configure(background="#ffffff")
        self.Topic_1.configure(disabledforeground="#a3a3a3")
        self.Topic_1.configure(font="-family {Showcard Gothic} -size 17")
        self.Topic_1.configure(foreground="#ff2227")
        self.Topic_1.configure(highlightbackground="#d9d9d9")
        self.Topic_1.configure(highlightcolor="black")
        self.Topic_1.configure(text='''YouTube Link''')

        self.btnpaste_1 = tk.Button(top)
        self.btnpaste_1.place(relx=0.633, rely=0.422, height=64, width=147)
        self.btnpaste_1.configure(activebackground="#ececec")
        self.btnpaste_1.configure(activeforeground="#000000")
        self.btnpaste_1.configure(background="#1abe07")
        self.btnpaste_1.configure(disabledforeground="#4646ff")
        self.btnpaste_1.configure(font="-family {Showcard Gothic} -size 16")
        self.btnpaste_1.configure(foreground="#ffffff")
        self.btnpaste_1.configure(highlightbackground="#d2dcdf")
        self.btnpaste_1.configure(highlightcolor="#000000")
        self.btnpaste_1.configure(pady="0")
        self.btnpaste_1.configure(text='''+ Paste''')
        self.btnpaste_1.configure(text='''Browse ''')
        self.btnpaste_1.configure(command=paste_filepath)

        self.Topic_1_1 = tk.Label(top)
        self.Topic_1_1.place(relx=0.067, rely=0.378, height=28, width=124)
        self.Topic_1_1.configure(activebackground="#ffffff")
        self.Topic_1_1.configure(activeforeground="#fd0006")
        self.Topic_1_1.configure(background="#ffffff")
        self.Topic_1_1.configure(disabledforeground="#a3a3a3")
        self.Topic_1_1.configure(font="-family {Showcard Gothic} -size 17")
        self.Topic_1_1.configure(foreground="#ff2227")
        self.Topic_1_1.configure(highlightbackground="#d9d9d9")
        self.Topic_1_1.configure(highlightcolor="black")
        self.Topic_1_1.configure(text='''File Path''')

        self.p1080 = tk.Radiobutton(top)
        self.p1080.place(relx=0.633, rely=0.6, relheight=0.056, relwidth=0.18)
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
        self.p1080.configure(variable=self.vidrf)
        self.p1080.configure(value=1)

        self.p720 = tk.Radiobutton(top)
        self.p720.place(relx=0.633, rely=0.666, relheight=0.056, relwidth=0.18)
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
        self.p720.configure(variable=self.vidrf)
        self.p720.configure(value=2)

        self.p480 = tk.Radiobutton(top)
        self.p480.place(relx=0.633, rely=0.734, relheight=0.054, relwidth=0.18)
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
        self.p480.configure(variable=self.vidrf)
        self.p480.configure(value=3)

        self.p360 = tk.Radiobutton(top)
        self.p360.place(relx=0.633, rely=0.8, relheight=0.056, relwidth=0.18)
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
        self.p360.configure(variable=self.vidrf)
        self.p360.configure(value=4)

        self.p240 = tk.Radiobutton(top)
        self.p240.place(relx=0.633, rely=0.866, relheight=0.056, relwidth=0.18)
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
        self.p240.configure(variable=self.vidrf)
        self.p240.configure(value=5)

        self.p144 = tk.Radiobutton(top)
        self.p144.place(relx=0.633, rely=0.934, relheight=0.054, relwidth=0.18)
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
        self.p144.configure(variable=self.vidrf)
        self.p144.configure(value=6)

        self.fmp3 = tk.Radiobutton(top)
        self.fmp3.place(relx=0.833, rely=0.6, relheight=0.056, relwidth=0.147)
        self.fmp3.configure(activebackground="#ececec")
        self.fmp3.configure(activeforeground="#000000")
        self.fmp3.configure(background="#ffffff")
        self.fmp3.configure(disabledforeground="#a3a3a3")
        self.fmp3.configure(font="-family {Showcard Gothic} -size 9")
        self.fmp3.configure(foreground="#000000")
        self.fmp3.configure(highlightbackground="#d9d9d9")
        self.fmp3.configure(highlightcolor="black")
        self.fmp3.configure(justify='left')
        self.fmp3.configure(text='''MP3''')
        self.fmp3.configure(variable=self.vidrf)
        self.fmp3.configure(value=7)

        self.fmp3_hq = tk.Radiobutton(top)
        self.fmp3_hq.place(relx=0.833, rely=0.666, relheight=0.056
                , relwidth=0.147)
        self.fmp3_hq.configure(activebackground="#ececec")
        self.fmp3_hq.configure(activeforeground="#000000")
        self.fmp3_hq.configure(background="#ffffff")
        self.fmp3_hq.configure(disabledforeground="#a3a3a3")
        self.fmp3_hq.configure(font="-family {Showcard Gothic} -size 9")
        self.fmp3_hq.configure(foreground="#000000")
        self.fmp3_hq.configure(highlightbackground="#d9d9d9")
        self.fmp3_hq.configure(highlightcolor="black")
        self.fmp3_hq.configure(justify='left')
        self.fmp3_hq.configure(text='''MP3 - HQ''')
        self.fmp3_hq.configure(variable=self.vidrf)
        self.fmp3_hq.configure(value=8)

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.817, rely=0.622,  relheight=0.356)
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
        self.sub_menu.add_command(
                label="Browse Save Path",
                command=menubar_paste_filepath)
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
                label="Why Free?",
                command=others_why_free)
        self.sub_menu1.add_command(
                label="Credits",
                command=others_credits)
        self.sub_menu1.add_command(
                label="Contributors",
                command=others_contributors)
        self.sub_menu1.add_command(
                label="Privacy Policy",
                command=others_privacy_policy)
        self.sub_menu1.add_command(
                label="Help",
                command=others_help)

        self.TSeparator1_1 = ttk.Separator(top)
        self.TSeparator1_1.place(relx=0.625, rely=0.62,  relheight=0.356)
        self.TSeparator1_1.configure(orient="vertical")

        self.Lcreditsbottom = tk.Label(top)
        self.Lcreditsbottom.place(relx=0.067, rely=0.863, height=38, width=304)
        self.Lcreditsbottom.configure(activebackground="#f9f9f9")
        self.Lcreditsbottom.configure(activeforeground="black")
        self.Lcreditsbottom.configure(background="#ffffff")
        self.Lcreditsbottom.configure(disabledforeground="#a3a3a3")
        self.Lcreditsbottom.configure(foreground="#000000")
        self.Lcreditsbottom.configure(highlightbackground="#d9d9d9")
        self.Lcreditsbottom.configure(highlightcolor="black")
        self.Lcreditsbottom.configure(text='''YouTube Video Downloader by ZeaCeR#5641 - v0.1''')



if __name__ == '__main__':
    vp_start_gui()



