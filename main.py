import datetime
import time


def main():
    flag=0
    while True:
        if (datetime.datetime.now().hour==20):
            if(flag==0):
                print('helloooo')
                flag+=1
        else:
            flag=0
        time.sleep(5)

main()
