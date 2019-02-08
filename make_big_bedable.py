#!/usr/bin/env python3
import sys
super_hot = { 'heat': 'super', 'cutoff': 990, 'color': '249,0,144' }
red_hot = { 'heat': 'red', 'cutoff': 900, 'color': '255,1,0' }
medium = { 'heat': 'medium', 'cutoff': 800, 'color': '239,172,23' }
mild = { 'heat': 'mild', 'cutoff': 0, 'color': '194,195,103' }

def which_hotness( score ):
    if score > super_hot['cutoff']:
        return super_hot
    if score > red_hot['cutoff']:
        return red_hot
    if score > medium['cutoff']:
        return medium
    return mild

infile = open( sys.argv[1] )

counts = {}


for i,line in enumerate(infile):
    if line.startswith('#'): continue

    fields = line.strip().split()
    chrom = fields[0]
    chromStart = fields[1]
    chromEnd = fields[2]
    thickStart = fields[6]
    thickEnd = fields[7]
    score = fields[-1]
    strand = fields[5]
    
    hotness = which_hotness(int(score))
    color = hotness['color']
    heat = hotness['heat']

    if heat not in counts: 
        counts[heat] = 1
    else:
        counts[heat] += 1

    name = "%s_%d" % (heat,counts[heat])

    print(chrom, chromStart, chromEnd, name, score, strand, thickStart, thickEnd, color, sep="\t")
    

print(counts, file=sys.stderr)
