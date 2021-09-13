# #########################
# Made by ZeaCeR#5641
# a.k.a Hirusha Adikari
# For any issue, please contact me!
# #########################

from playsound import playsound
import homewindow, images
from threading import Thread

def RUN_HOME():
    homewindow.window.mainloop()

try:
    # try:
    #     images.CREATE_ALL_IMAGES()
    # except:
    #     pass

    thr1 = Thread(target=playsound, args=("assets\\im_rick_from_c137_no_harm_peace.mp3",))
    thr1.start()
    RUN_HOME()

except Exception as e:
    print("Error:", e)

finally:
    images.DELETE_ALL()
    # pass