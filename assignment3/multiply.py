import MapReduce
import json
import sys

# Map function
# mr - MapReduce object
# data - json object formatted as a string
mr = MapReduce.MapReduce()
def mapper(data):

    nn = 4

    if data[0] == 'A':
        for k in range(nn):
            i = data[1] #row
            mr.emit_intermediate((i,k), data)
    else:
        for k in range(nn):
            j = data[2] #row
            mr.emit_intermediate((k,j), data)

# Reduce function
# mr - MapReduce object
# key - key generated from map phse, associated to list_of_values
# list_of_values - values generated from map phase, associated to key
def reducer(p, item):

    # output item (only for reducer)
    nn = 4
    i = p[0]
    j = p[1]
    ans = 0
    for k in range(nn):
        tmp_x = 0
        tmp_y = 0
        for v in item:
            if item[0] == 'A':
                if item[1] == i and item[2] == k:
                    tmp_x = item[3]
            else:
                if item[1] == k and item[2] == j:
                    tmp_y = item[3]
        ans += tmp_x * tmp_y
    mr.emit((i, j, ans))

def main():
    # Assumes first argument is a file of json objects formatted as strings, 
    #one per line.
    mr.execute(open(sys.argv[1]), mapper, reducer)

if __name__ == '__main__':
    main()
