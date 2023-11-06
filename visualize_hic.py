#!/home/eaststar0/miniconda3/bin/python
  
import sys 
import os
from tadlib.visualize.heatmaps import *

mcool = sys.argv[1]
#loop = sys.argv[2]
#tad = sys.argv[3]

res=10000

plot_window = 1000000


chrom = 'chr22'
start=22401099
end=24553399

print(f'{chrom}:{start}-{end}')

vis = Triangle(f'{mcool}::/resolutions/{res}', chrom, start, end, None)
vis.matrix_plot()
#vis.plot_loops(loop)
#vis.plot_TAD(tad, linewidth=1.5)
#vis.plot_TAD(tad, linewidth=1.5)

vis.outfig(mcool.split('/')[-1].replace('.mcool', f'.vis.{res}.png'))



