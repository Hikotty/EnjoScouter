import os

tmp = 0
os.system("afplay " + "sound/level2.mp3")
while(1):
    tmp+=1
    if(tmp == 100):
        os.kill()
os.system("afplay " + "sound/level3.mp3")
