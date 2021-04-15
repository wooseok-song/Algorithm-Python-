import sys


while True:
    try:
        a,b=map(int,sys.stdin.readline().strip().split())
        print(a+b)
    except:
        break