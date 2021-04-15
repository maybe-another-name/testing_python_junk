from org.apache.nifi.processor.io import StreamCallback


class TarFilterStreamCallback(StreamCallback):
    def __init__(self):
        pass

    def process(self, inputStream, outputStream) -> bool:
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


flowFile = session.get()
if (flowFile != None):
    flowFile = session.write(flowFile, TarFilterStreamCallback())
