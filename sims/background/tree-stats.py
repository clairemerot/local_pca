#!/usr/bin/env python3
description = '''
Compute mean divergence between populations in windows along the genome.
'''

import gzip, csv
import sys, os, math
import msprime
import argparse

parser = argparse.ArgumentParser(description=description)
parser.add_argument('--treefile', '-t', type=str, 
        help="Name of the tree sequence file output by msprime.")
parser.add_argument('--samples_file', '-s', type=str, 
        help="Name of the tsv containing population information about the samples.")
parser.add_argument('--window_size', '-w', type=float, 
        help="Width of the (regularly spaced) windows.")
parser.add_argument('--n_window', '-n', type=int, 
        help="Number of (regularly spaced) windows.")
parser.add_argument('--outfile', '-o', type=str, 
        help="Output file name.")

args = parser.parse_args()

ts = msprime.load(args.treefile)

pops = {}

with open(args.samples_file, newline='') as csvfile:
    thereader = csv.DictReader(csvfile, delimiter='\t')
    assert(thereader.fieldnames == ['id', 'flags', 'population', 'time'])
    for x in thereader:
        if not x['population'] in pops:
            pops[x['population']] = []
        pops[x['population']] += [x['id']]

leaf_sets = [list(map(int,u)) for u in pops.values()]
pop_names = list(pops.keys())

output_names = ["_".join([pop_names[i],pop_names[j]]) for i in range(len(pop_names))
                        for j in range(i,len(pop_names))]

if args.n_window is not None:
    if args.window_size is not None:
        raise ValueError("Can't specify both number of windows and window size.")
    else:
        args.window_size = ts.sequence_length / args.n_window
else:
    args.n_window = math.ceil(ts.sequence_length / args.window_size)

windows = [args.window_size * k for k in range(args.n_window + 1)]

tmrcas = ts.get_mean_tmrca(leaf_sets, windows)

with open(args.outfile, "w", newline="") as outfile:
    writer = csv.writer(outfile, delimiter="\t")
    writer.writerow(["start", "end"] + output_names)
    for k in range(len(tmrcas)):
        writer.writerow([windows[k], windows[k+1]] + tmrcas[k])

outfile.close()
