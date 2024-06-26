import os
import numpy as np

# Here is the method for extracting security patterns of overflow.

def detectOF(filepath):

    target=[]
    try:
        f=open(filepath,'r')
    except:
        print("empty contract file!")
        
    lines=f.readlines()
    flag = True

    for line in lines:
        if len(line.strip())>0 and line!='\n':
            if line.strip().startswith("/*"):
                flag = False
                continue
            elif line.strip().startswith("*/"):
                flag = True
                continue
            elif not line.strip().startswith("//") and flag:
                end=line.find("//")
                if '+' in line or '-' in line or '/' in line or '*' in line:
                    if line.find('+')>end or line.find('-')>end or line.find('/')>end or line.find('*')>end:
                        target.append(line.strip())
    return target
