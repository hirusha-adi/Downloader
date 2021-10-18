# How this works?

- If there is something that im not sure for it to work, i create a new CLI version and check weather it is. If it works, i will add it to the GUI version.
- `X.Y.Z` - The `Z` will not always be a new version, it is just a patch for `X.Y`

# Downlaoder v0.9 - CLI

- Update (Completely automatic, checks for updates and if there is a new version, it will download the new file to the current working directory,if there is no update, nothing will be downloaded) - this can be selected via the home menu

# Downloader v0.8 - GUI

- Fixed a huge bug when downloading a video with " or ' in the video title ([Github Issue](https://github.com/hirusha-adi/Downloader/issues/4))
- Fixed a issue in file naming (now it follow all windows file naming standards)
- Both of the above issues was reported by discord user: `ᴍɪᴋᴇʏ#9509`

# Downloader v0.7 - GUI

- Downloading video information video subtitles (still, English only) is made optional via checkboxes in the GUI
- Better formatted output in the console
- Formatted Code

# Downloader v0.6.5 - GUI

- Fixed a huge bug found in `v0.6`

# Downloader v0.6 - GUI

- YouTube Search implemented in GUI
- You can directly paste a link or you can type the query to search the video/channel/playlist and then, download it
- NOTE: That anything which is starting with `http` is considered a link and will not be searched in YouTube

# Downlaoder v0.5 - CLI

- First time implementing YouTube Search
- This was made possible by: [youtube-search-python](https://pypi.org/project/youtube-search-python/)
- YouTube Search is another option in the main menu

# Downloader v0.4.1 - GUI

- This will play some Rick and Morty sounds effects when interacting with the GUI
- This is resource heavy, therefore this will no longer be in upcoming versions
- Idea by discord user: `OkSheBroken#7960`

# Downloader v0.4 - GUI

- Switched from PAGE to a completely custom GUI
- The GUI is rick and morty themed
- The same features as of `v0.3`

# Downloader v0.3 - GUI

- GUI improvements

# Downloader v0.2 - GUI

- The GUI is made with PAGE (tcl/tk)
- Just the basic implementation of the CLI using a GUI
- Same features as of `v0.1`

# Downloader v0.1 - CLI

- This is the very first version of the Downloader
- You can download youtube playlists, channels, videos
- Will give you video information
- Will give you subtitles for each video, the file will be empty if there are no english subtitles uploaded by the video uploader
- Download things from other links (the links MUST be DIRECT, or else, this will download the html file and save it)
