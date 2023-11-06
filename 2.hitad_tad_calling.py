#!/data2/home/song7602/miniconda3/envs/py38/bin/python
  
import sys 
import os
#from tadlib.visualize.heatmaps import *

mcool = sys.argv[1]
res=25000

# prepare metadata
metadata = mcool.split('/')[-1].replace('.mcool', '.metadata.txt')
fo = open(metadata, 'w')
fo.write(f'res:{res}\n')
fo.write(f' rep1:{mcool}::/resolutions/{res}')
fo.close()

hitad_out = metadata.replace(".metadata.txt", f".tad.{res}.txt")
hitad_log = metadata.replace(".metadata.txt", f".{res}.hitad.log")
os.system(f"hitad -O {hitad_out} -d {metadata} --logFile {hitad_log} -W RAW")




