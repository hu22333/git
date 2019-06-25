from sys import argv
from os.path import exists

script,from_file,to_file = argv

print(f"copying form {from_file} to {to_file}")

#we could do these two on one line,how?
in_file = open(from_file)
indata=in_file.read()

print(f"Thz input file is {len(indata)}bytes long")

print("Ready,hit RETURN to contrinue,CTRL-C to about.")
input()

out_file=open(to_file, 'w')
out_file.write(indata)

print("Alright,all done.")

out_file.close()
in_file.close()
