#!/usr/bin/env python

import sys
import nibabel as nib
import pandas

#just dump input image header to output.txt
print("HI1")
print(list(sys.argv))
img=nib.load(sys.argv[1])
f=open("output.txt", "w")
print("HI!")
f.write(str(img.header))
f.close()