#!/usr/bin/python
import sys


f = open(sys.argv[1])

# skip header
f.readline()
strand = '.'
for i,line in enumerate(f):
    # lines are ordered by number of factors
    score = 1000 *  (1 - (float(i) /35062))

    fields = line.split('\t')
    name = "HOT_%d" % (i)
    chrom = fields[3]
    start = fields[7]
    end = fields[8]
    thickStart = fields[4]
    thickEnd = fields[5]
    core_factors = fields[9]
    ext_factors = fields[10]
    n_core_factors = int( fields[2] )
    n_ext_factors = int( fields[1] )


    # bed_9
    print chrom, start, end, name, int(score), strand, thickStart, thickEnd, "255,0,0"
