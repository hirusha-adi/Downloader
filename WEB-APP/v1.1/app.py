#!/bin/python3
import os
from flask import Flask, render_template, request
from flask import url_for, redirect, send_file, session
from pytube import YouTube


true = "True"
app = Flask(__name__)
app.config['SECRET_KEY'] = "Demo"


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['link'] = request.form.get('url')

        # youtube_world_list = ("www.youtube.com", "youtube.com", "youtube", "youtu.be") # for link validation
        # if (str(session['link']).lower().split("/")[:3][-1]) in youtube_world_list:
            
  
        # if str(session['link']).lower().startswith('http'):
        #     pass
        try:
            print(session['link'])
            url = YouTube(session['link'])
            return render_template("youtube.html", url=url)
        
        except:
            return render_template("failed.html")
    
    return render_template("index.html")


@app.route("/youtube", methods=['GET', 'POST'])
def download_video():
    if request.method == 'POST':
        try:
            url = YouTube(session['link'])
            itag = request.form.get('itag')
            video = url.streams.get_by_itag(itag)
        
        except:
            return render_template("failed.html")
        
        filename = video.download()
        return send_file(filename, as_attachment=True)

    return redirect(url_for('index'))


@app.route("/failed", methods=['GET'])
def show_error_message():
    return render_template("failed.html")



if __name__ == "__main__":
    app.run('0.0.0.0', port=8080, debug=True)


