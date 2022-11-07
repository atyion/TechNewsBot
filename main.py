from parser import *
import time
oldtime = ""
if __name__ == "__main__":
    while True:
        time.sleep(60)
        if(parser()[3]!=oldtime):
            print(parser())
            oldtime = parser()[3]
