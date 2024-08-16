import os, time

while True:
    os.mkdir("DENEME")
    time.sleep(.5)
    os.rename("DENEME","DENEMEEEE SİLMEEEE")
    time.sleep(.5)
    os.rmdir("DENEMEEEE SİLMEEEE")
    time.sleep(.5)