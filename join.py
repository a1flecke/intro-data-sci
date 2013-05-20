import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    record_type = record[0]
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence
    values = [] #need to first grab order, then for each of the remaining, emit
    for l in list_of_values:
      print l
      if l[0] == 'order':
        values += l

    for l in list_of_values:
      if l[0] == 'line_item':
        values += l
    print list(set(values))
    exit()
    mr.emit((values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
