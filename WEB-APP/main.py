#!/bin/python3
import os
import platform
from flask import Flask, render_template, request
from flask import url_for, redirect, send_file, session
from pytube import YouTube
from requests import get as reqget
from remove_files import run_rof
try:
    from youtubesearchpython import VideosSearch
except:
    if platform.system().lower().startswith('win'):
        os.system("pip install youtube-search-python")
    else:
        os.system("pip3 install youtube-search-python")
    from youtubesearchpython import VideosSearch


true = "True"
app = Flask(__name__)
app.config['SECRET_KEY'] = "Demo"


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['link'] = request.form.get('url')

        youtube_world_list = ("www.youtube.com", "youtube.com", "youtube", "youtu.be") # for link validation
        if (str(session['link']).lower().split("/")[:3][-1]) in youtube_world_list:
            try:
                url = YouTube(session['link'])
                return render_template("youtube.html", url=url)   

            except Exception as pyerr:
                return render_template("failed.html", pyerr=pyerr)
  
        elif (str(session['link']).lower().startswith('http')) and (str(session['link']).lower() not in youtube_world_list):
            try:
                data = reqget(session['link']).content
                filename = str(session['link']).lower().split("/")[-2:-1]
                with open(filename, "wb") as file:
                    file.write(data)
                return send_file(filename, as_attachment=True)
            except Exception as pyerr:
                return render_template("failed.html", pyerr=pyerr)
        
        else:
            try:
                videosSearch = VideosSearch(f'{session["link"]}', limit = 1)
                mainresult = videosSearch.result()["result"]
                video_index = mainresult[0]
                video_link = video_index["link"]
                url = YouTube(video_link)
                return render_template("youtube.html", url=url)   

            except Exception as pyerr:
                return render_template("failed.html", pyerr=pyerr)
    
    
    return render_template("index.html")


@app.route("/home", methods=['GET'])
def home():
    return redirect(url_for('index'))


@app.route("/youtube", methods=['GET', 'POST'])
def download_video():
    if request.method == 'POST':
        try:
            url = YouTube(session['link'])
            itag = request.form.get('itag')
            video = url.streams.get_by_itag(itag)
        
        except Exception as pyerr:
            return render_template("failed.html", pyerr=pyerr)
        
        filename = video.download()
        return send_file(filename, as_attachment=True)
        
    return redirect(url_for('index'))


@app.route("/failed", methods=['GET'])
def show_error_message():
    return render_template("failed.html")



if __name__ == "__main__":
    run_rof()
    app.run('0.0.0.0', port=8080, debug=True)


