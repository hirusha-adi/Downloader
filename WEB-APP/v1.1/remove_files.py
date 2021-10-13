import os
import time
from threading import Thread

def remove_other_files():
    while True:
        for filename in os.listdir(os.getcwd()):
            if filename.endswith('.py') or (filename in ("static", "templates", "log")):
                print(filename)
            else:
                os.system(f"rm -rf {filename}")
        time.sleep(300)

def run_rof():
    t = Thread(target=remove_other_files)
    t.start()

