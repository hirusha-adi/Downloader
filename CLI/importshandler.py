import os, platform

def ALL():
    try:
            import webbrowser
    except ImportError:
            if platform.system().lower().startswith('win'):
                    os.system("pip install webbrowser")
            else:
                    os.system("pip3 install webbrowser")
            # import webbrowser

    try:
            import clipboard
    except ImportError:
            if platform.system().lower().startswith('win'):
                    os.system("pip install clipboard")
            else:
                    os.system("pip3 install clipboard")
            # import clipboard

    try:
            import pytube
    except ImportError:
            if platform.system().lower().startswith('win'):
                    os.system("pip install pytube")
            else:
                    os.system("pip3 install pytube")
            # from pytube import *

