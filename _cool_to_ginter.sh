#!/usr/bin/bash

# raw count
cool=$1
hicConvertFormat -m $cool \
         --inputFormat cool --outputFormat ginteractions --load_raw_values \
	           --outFileName ${mcool}_10kb_contacts.raw_values.ginteractions --resolutions 10000



