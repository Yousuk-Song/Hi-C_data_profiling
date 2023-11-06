#!/data2/home/song7602/miniconda3/envs/py38/bin/python
  
import sys 
import os
import subprocess

res = 10000
mcool = sys.argv[1]
cool = f'{mcool}::/resolutions/{res}'

p1 = subprocess.Popen(['peakachu','depth', '-p', cool],stdout = subprocess.PIPE)
depth_info = p1.communicate()[0].decode("utf-8").split('\n')

model_numb = ''
for i in depth_info[-2].split('suggested model: ')[-1].split():
        model_numb += i
p1.stdout.close()

training_set = f'{sys.path[0]}/training_sets/high-confidence.{model_numb}.10kb.w6.pkl'


os.system(f'peakachu score_genome -r {res} --balance -p {cool} -O {mcool.replace(".mcool", f".genome-scores.{res}bp.bedpe")} -m {training_set}')


os.system(f'peakachu pool -r {res} -i {mcool.replace(".mcool", f".genome-scores.{res}bp.bedpe")} -o {mcool.replace(".mcool", f".genome-loops.0.95.{res}bp.bedpe")} -t 0.9')


