import MapReduce
import json
import sys

# Map function
# mr - MapReduce object
# data - json object formatted as a string
mr = MapReduce.MapReduce()
def mapper(data):

    dna = data[1][:-10]
    mr.emit_intermediate(dna,1)

# Reduce function
# mr - MapReduce object
# key - key generated from map phse, associated to list_of_values
# list_of_values - values generated from map phase, associated to key
def reducer(dna, counts):

    # output item (only for reducer)
    mr.emit(dna)

def main():
    # Assumes first argument is a file of json objects formatted as strings, 
    #one per line.
    mr.execute(open(sys.argv[1]), mapper, reducer)

if __name__ == '__main__':
    main()
