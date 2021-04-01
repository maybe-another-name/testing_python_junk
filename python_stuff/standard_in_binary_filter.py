import sys
import tarfile
import pkg_resources
import io

import select


def main():
    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        filter_from_std_in()
    else:
        filter_from_contant()


def filter_from_std_in():
    input_stream_bytes = sys.stdin.buffer.read()
    input_stream_bytes_copy = input_stream_bytes[:]
    if test_tar(input_stream=io.BytesIO(input_stream_bytes)):
        sys.stdout.buffer.write(input_stream_bytes_copy)    


def filter_from_contant():
    resource_package = __name__
    resource_path = '/'.join(('resources', 'non-matching.tar'))
    resource_filename = pkg_resources.resource_filename(
        resource_package, resource_path)

    input_binary = open(resource_filename, mode='rb')

    if test_tar(input_file=input_binary):
        input_binary.seek(0)
        sys.stdout.buffer.write(input_binary.read())


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
