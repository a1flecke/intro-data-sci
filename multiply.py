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
    if(record[0] == 'a'):
      mr.emit_intermediate(record[1], record)
    else:
      mr.emit_intermediate(record[2], record)
      mr.emit_intermediate(record[1], record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence
    j = key

    #print name, list_of_values

    #print name, list_of_values
    matrix_a = {}
    matrix_b = {}
    for l in list_of_values:
      if(l[0] == 'a'):
        print 'a', l
        matrix_a[(l[1],l[2])] = l[3]
      else:
        print 'b', l
        matrix_b[(l[2],l[1])] = l[3]
    print 'end of ',j
    matrixSum = 0
    for a in matrix_a:
      matrixSum+= matrix_a[a] * matrix_b.get(a, 0)







# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
