import time
import webbrowser

i = 0
while i < 3:
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    # print("open browser")
    i += 1
