import sys
import tarfile

# this works when i echo some text into it... and also when i cat a text file to it...
input_file = sys.stdin.read()
#print(input_file)
sys.stdout.write(input_file)