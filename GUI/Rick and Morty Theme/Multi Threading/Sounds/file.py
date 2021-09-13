import os
import base64 as bb
os.listdir()

with open("im_rick_from_c137_no_harm_peace.mp3", "rb") as f1:
    f1c = f1.read()
    f1cbb = bb.b64encode(f1c)

with open("im_rick_from_c137_no_harm_peace.txt", "wb") as f2:
    f2.write(f1cbb)

with open("test.mp3", "wb") as f3:
    f3.write(bb.b64decode(f1cbb))

