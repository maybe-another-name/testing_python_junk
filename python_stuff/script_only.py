import sys
import tarfile
import io


def filter_from_std_in():
    input_stream_bytes = sys.stdin.buffer.read()
    input_stream_bytes_copy = input_stream_bytes[:]

    filterable = False
    try:
        filterable = is_tar_filterable(
            input_stream=io.BytesIO(input_stream_bytes))
    except:
        sys.stdout.buffer.write(b'error-filtering')
    if filterable:
        sys.stdout.buffer.write(b'filterable-as-bytes')
    else:
        sys.stdout.buffer.write(b'not-filterable-as-bytes')


def is_tar_filterable(input_stream=None):
    tar_content = tarfile.open(fileobj=input_stream, mode='r|*')

    for tar_info in tar_content.getmembers():
        if tar_info.name == "readme.md":
            return True

    return False


filter_from_std_in()
