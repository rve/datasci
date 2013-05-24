import MapReduce
import json
import sys

# Map function
# mr - MapReduce object
# data - json object formatted as a string
mr = MapReduce.MapReduce()
def mapper(data):

    qid = data[1]
    mr.emit_intermediate(qid, data)


# Reduce function
# mr - MapReduce object
# key - key generated from map phse, associated to list_of_values
# list_of_values - values generated from map phase, associated to key
def reducer(qid, data):

    # output item (only for reducer)
    if len(data) >= 2:
        for line in data:
            if line[0] == "order":
                order = line
        for line in data:
            if line[0] == "line_item":
                mr.emit(order + line)

def main():
    # Assumes first argument is a file of json objects formatted as strings, 
    #one per line.
    mr.execute(open(sys.argv[1]), mapper, reducer)

if __name__ == '__main__':
    main()
