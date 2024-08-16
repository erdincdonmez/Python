import os, time

while True:
    open("DENEME","w")
    time.sleep(.5)
    os.rename("DENEME","DENEMEEEE SİLMEEEE")
    time.sleep(.5)
    os.remove("DENEMEEEE SİLMEEEE")
    time.sleep(.5)