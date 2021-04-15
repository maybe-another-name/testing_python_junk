import tarfile
import sys

def process(input_stream, output_stream):
  filterable = False
  try:
    filterable = is_tar_filterable(input_stream)		  
  except:
    output_stream.write(b'error-filtering')
  if filterable:
    output_stream.write(b'filterable-as-bytes')
  else:
    output_stream.write(b'not-filterable-as-bytes')

def is_tar_filterable(input_stream=None):
  tar_content = tarfile.open(fileobj=input_stream, mode='r|*')

  for tar_info in tar_content.getmembers():
    if tar_info.name == "readme.md":
      return True

  return False

def main():
  filter_from_std_in()


def filter_from_std_in():    
  process(input_stream=sys.stdin.buffer, output_stream=sys.stdout.buffer)


if __name__ == "__main__":
  main()