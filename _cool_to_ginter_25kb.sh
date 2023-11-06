#!/usr/bin/bash

# raw count
mcool=$1
hicConvertFormat=/data2/home/song7602/eaststar0/miniconda3/bin/hicConvertFormat
$hicConvertFormat -m ${mcool}::/resolutions/25000 --inputFormat cool --outputFormat ginteractions --load_raw_values --outFileName ${mcool}_25kb_contacts.raw_values.ginteractions --resolutions 25000



