import sys
import time
import os

def main():
    temp = int(sys.argv[1])
    for i in range(temp):
        os.system("./tmp36raw")
        time.sleep(1)
    
if __name__ == '__main__':
    main()
