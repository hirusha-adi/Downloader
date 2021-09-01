# from pytube import *
# import os


# def FUCKING_DOWNLOAD_ONE_VIDEO(qualityvid, urlvid):
#     print(f"[*] Recieved a download quality of {qualityvid} to {urlvid}")
#     try:
#             yt = YouTube(urlvid)
#     except VideoUnavailable:
#             print("[!!] VIDEO UNAVAILABLE!")
#             return
#     except Exception as e:
#             print("Error", e)
#             return
#     print("[+] Object Initiated")
#     print(f"\nExtracting Information: \n[+]Title: {yt.title} \n[+]Thumnail URL: {yt.thumbnail_url} \n[+]Author: {yt.author} \n[+]Channel ID: {yt.channel_id} \n[+]Channel URL: {yt.channel_url} \n[+]Video Length: {yt.length} \n[+]Published Date:{yt.publish_date} \n[+]Age Restricted: {yt.age_restricted} \n[+]Video URL: {urlvid} \n[+]Video Description: {yt.description}")
#     try:
#             with open(f"{yt.title} - Information.txt", "w") as fileinfotxt:
#                     fileinfotxt.write(f"[+]Title: {yt.title} \n[+]Thumnail URL: {yt.thumbnail_url} \n[+]Author: {yt.author} \n[+]Channel ID: {yt.channel_id} \n[+]Channel URL: {yt.channel_url} \n[+]Video Length: {yt.length} \n[+]Published Date:{yt.publish_date} \n[+]Age Restricted: {yt.age_restricted} \n[+]Video URL: {urlvid} \n[+]Video Description: {yt.description}")
#     except:
#             with open(f"{yt.title.replace('|', 'x').replace('?', 'x').replace('>', 'x').replace('<', 'x').replace(':', 'x').replace(';', 'x')} - Information.txt", "w") as fileinfotxt:
#                     fileinfotxt.write(f"[+]Title: {yt.title} \n[+]Thumnail URL: {yt.thumbnail_url} \n[+]Author: {yt.author} \n[+]Channel ID: {yt.channel_id} \n[+]Channel URL: {yt.channel_url} \n[+]Video Length: {yt.length} \n[+]Published Date:{yt.publish_date} \n[+]Age Restricted: {yt.age_restricted} \n[+]Video URL: {urlvid} \n[+]Video Description: {yt.description}")
#     print(f"[+] Wrote Information to {yt.title} - Information.txt")
#     print("\n[*] Trying to download subtitles/captions")
#     try:
#             caption = yt.captions.get_by_language_code('en')
#             print("[+] Successfully loaded subtitles/captions")
#             try:
#                     with open(f"{yt.title}.srt", "w") as filesrt:
#                             filesrt.write(caption.generate_srt_captions())
#             except OSError:
#                     with open(f"{yt.title.replace('|', 'x').replace('?', 'x').replace('>', 'x').replace('<', 'x').replace(':', 'x').replace(';', 'x')}.srt", "w") as filesrt:
#                             filesrt.write(caption.generate_srt_captions())
#             print("[+] Created a .srt file!")
#     except:
#             print("[-] Unable to download subtitles")
#     all_audio_qualities_tup = ("32kbps", "64kbps", "128kbps", "160kbps", "192kbps", "240kbps", "256kbps", "320kbps")
    
#     if qualityvid in all_audio_qualities_tup:
#             print("\n[*] Trying to downlod the audio")
#             try:
#                     video = yt.streams.filter(only_audio=True).filter(abr=f"{qualityvid}").first().download()
#                     print(f"[+] File downloaded successfully!\n{video}")
#             except:
#                     print("[-] An Error has occured!")
#                     print("[*] Trying to download with the highest available quality for the audio")
#                     try:
#                             video = yt.streams.filter(only_audio=True).first().download()
#                             print(f"[+] File downloaded successfully!\n{video}")
#                     except:
#                             print("[-] Failed!")
#                             print("[*] Trying to download with the lowest available quality for the audio")
#                             try:    
#                                     video = yt.streams.filter(only_audio=True).last().download()
#                                     print(f"[+] File downloaded successfully!\n{video}")
#                             except:
#                                     print("[!!] FAILED")
#     else:
#             print("\n[*] Trying to downlod the video")
#             try:
#                     video = yt.streams.filter(res=f"{qualityvid}").filter(progressive=True).first().download()
#                     print(f"[+] File downloaded successfully!\n{video}")
#             except:
#                     print("[-] An Error has occured!")
#                     print("[*] Trying to download with the highest available quality for the video")
#                     try:
#                             video = yt.streams.filter(progressive=True).get_highest_resolution().download()
#                             print(f"[+] File downloaded successfully!\n{video}")
#                     except:
#                             print("[-] Failed!")
#                             print("[*] Trying to download with the lowest available quality for the video")
#                             try:    
#                                     video = yt.streams.filter(progressive=True).get_highest_resolution()
#                                     print(f"[+] File downloaded successfully!\n{video}")
#                             except:
#                                     print("[!!] FAILED")


                                    