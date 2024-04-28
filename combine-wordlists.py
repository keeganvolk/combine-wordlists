import sys
import argparse
p=argparse.ArgumentParser(description="",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
p.add_argument("[output file]",help="File name to output to")
p.add_argument("[input files]",nargs=argparse.REMAINDER,help="Names of wordlist files to combine")
args=p.parse_args()
a=vars(args)
outstring=''
for i in a["[input files]"]:
 with open(i) as file:
  outstring+=file.read()
with open(a["[output file]"],'w') as file:
 file.write(outstring)
