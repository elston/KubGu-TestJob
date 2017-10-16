#!/usr/bin/env python
import logging, argparse

def getsum(i):
    if len(i) == 1:
        return 1
    # ...
    return sum(i)

def main(room):
    # ..
    x,n = 1,1
    # while n <= 10:
    while True:        
        # ...
        i = list(range(1,n + 1))
        p1 = [j-1 for j in range(1,len(i)+1)]
        p1min = sum(p1)
        p2 = [j for j in range(1,len(i)+1)]  
        # ...
        print(n, [ p1min + item for item in p2] )
        for m in p2:
            if room == p1min + m:
                return (n,m)
        n += 1




if __name__ == "__main__":
    # ...
    parser = argparse.ArgumentParser(
                        description='Setup defaults')
    # ..
    parser.add_argument('room', 
                        type=int,
                        help='Room number')
    # ..
    arguments = parser.parse_args()
    # ...
    res = main(room=arguments.room)
    if res:
        n,m = res
        print(n,m)
        exit(0)
    # ..
    print('Fail')
