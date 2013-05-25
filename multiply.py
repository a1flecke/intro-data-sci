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
    for j in range(0,5):
      if(record[0] == 'a'):
        mr.emit_intermediate((record[1],j), record)
      else:
        mr.emit_intermediate((j,record[2]), record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence
    #print name, list_of_values

    #print name, list_of_values
    #print 'key=',key
    matrix_a = {}
    matrix_b = {}

    for l in list_of_values:
      mat_key = (l[1],l[2])
      if(l[0] == 'a'):
        #print 'adding a[',mat_key,']=',l[3]
        matrix_a[mat_key] = l[3]
      else:
        #print 'adding b[',mat_key,']=',l[3]
        matrix_b[mat_key] = l[3]
    #print 'end of ',key, ' max_j=',max_j

    #print list_of_values

    matrix_sum = 0
    for j in range(0,5):
      a = matrix_a.get((key[0],j),0)
      b = matrix_b.get((j, key[1]),0)
      #do C[i,j] = C[i,j] + A[i,k] * B[k,j]
      #print 'looking at a[',key[0],',',j,']=',a
      #print 'looking at b[',j,',',key[1],']=',b
      matrix_sum +=  a*b 
    #print 'c[',(key),']=',matrix_sum
    #exit()
    if matrix_sum != 0:
      mr.emit((key[0],key[1],matrix_sum))



# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
