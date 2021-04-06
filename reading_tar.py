import tarfile
import sys

# this works
with tarfile.open("one_file.tar") as tar_file:
    print(tar_file.getmembers())

# and so does this
input_file = open("one_file.tar", mode='rb')
with tarfile.open(fileobj=input_file) as tar_file:
    print(tar_file.getmembers())

# as well as this (run with cat one_file.tar | python reading_tar.py inside venv)
with tarfile.open(fileobj=sys.stdin.buffer, mode='r|*') as tar_file:
    print(tar_file.getmembers())