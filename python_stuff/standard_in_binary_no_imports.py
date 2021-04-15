import sys
import tarfile
import io


def main():
  filter_from_std_in()


def filter_from_std_in():
  input_stream_bytes = sys.stdin.buffer.read()
  input_stream_bytes_copy = input_stream_bytes[:]
  if test_tar(input_stream=io.BytesIO(input_stream_bytes)):
      sys.stdout.buffer.write(input_stream_bytes_copy)    

def test_tar(input_stream=None, input_file=None):
  if (input_stream):
      tar_content = tarfile.open(fileobj=input_stream, mode='r|*')
  if (input_file):
      tar_content = tarfile.open(fileobj=input_file)

  for tar_info in tar_content.getmembers():
      if tar_info.name == "readme.md":
          return True

  return False


if __name__ == "__main__":
  main()
