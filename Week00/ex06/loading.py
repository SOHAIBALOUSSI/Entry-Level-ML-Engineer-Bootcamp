import tqdm
import time
import sys
import os
#ETA: 8.67s [ 23%][=====> ] 233/1000 | elapsed time 2.33s

stime = time.time()

def ft_progress(list : any):   

    listSize = len(list)
    eta = 0
    barlength = 20
    for i in range(listSize):
        persent = (i+1) / listSize*100
        elapsedtime = time.time() - stime
        progress = int(barlength * (i+1) / listSize)
        bar = "=" * progress
        if (progress < barlength): bar+=">"
        if i > 0:
            eta = (elapsedtime/(i+1)) * (listSize - (i+1))
        print(f"ETA: {eta:.02f}s  [{persent:.02f}%][{bar:{' '}<{20}}], {i+1}/{listSize} | elapsed time {elapsedtime:.02f}s", end='\r') 
        yield i


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
