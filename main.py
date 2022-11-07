from parser import *
import time
import telegram.ext
oldtime = ""
if __name__ == "__main__":
    while True:
        time.sleep(60)
        if(parser()[3]!=oldtime):
            print(parser())
            oldtime = parser()[3]
