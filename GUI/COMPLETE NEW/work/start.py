import homewindow, images

try:
    homewindow.window.mainloop()
finally:
    images.DELETE_ALL()

