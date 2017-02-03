import webbrowser
import time

total_breaks = 5
count = 1

while(count<=total_breaks):
  time.sleep(3*60*60)
  webbrowser.open("https://www.youtube.com")
  count = count+1
