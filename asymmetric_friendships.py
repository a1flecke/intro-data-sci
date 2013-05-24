import MapReduce
import sys
import copy

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    #print 'LOOKING AT: ', record
    #print 'Sending it to ', record[0]
    #print 'Sending it to ', record[1]
    mr.emit_intermediate(record[0], record)
    mr.emit_intermediate(record[1], record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence
    name = key

    #print name, list_of_values

    #print name, list_of_values

    for l in list_of_values:
      inverse = [l[1], l[0]]
      #print 'NAME: ',name, 'inverse: ',inverse, list_of_values
      if inverse not in list_of_values and l[0] == name:
        mr.emit((l[0],l[1]))
        mr.emit((l[1],l[0]))







# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
