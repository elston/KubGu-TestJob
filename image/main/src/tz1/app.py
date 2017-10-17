#!/usr/bin/env python
import logging, argparse

def get_flor(n, m):
    # ..
    val_1 =  sum([x for x in range(1,n)])
    # ...
    return val_1 + m

def get_matrix_item(n, m, o):
    # ..
    val_1 =  sum([x**2 for x in range(1,n)])
    val_2 =  (n * (m - 1))
    # ..
    return val_1 + val_2 + o

def get_matrix_x(n, m):
    return [get_matrix_item(n, m, o) for o in  range(1, n+1)]

def get_matrix_xy(n, room):
    return [get_matrix_x(n, m) for m in range(1,n+1)]

def main(room):
    # ..
    n = 1
    # while n <= 5:
    while True:        
        # ..
        matrix_xy = get_matrix_xy(n, room)
        # print(n, matrix_xy)
        # ...
        for i in range(0,n):
            vi = matrix_xy[i]
            for j in range(0,len(vi)):
                vj = vi[j]
                if vj == room:
                    return n,i+1,j+1
        # ..
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
        n,i,j = res
        print(get_flor(n,i),j)
        exit(0)
    # ..
    print('Fail')
