import pkg_resources


def main():
    # https://stackoverflow.com/questions/6028000/how-to-read-a-static-file-from-inside-a-python-package
    # works as script, but opens the file in binary mode
    # also works when installed with pip as a console_script (requires that the data be registered in setup.py)
    resource_package = __name__
    resource_path = '/'.join(('resources', 'some-special-text.txt'))
    resource_as_binary_file = pkg_resources.resource_stream(
        resource_package, resource_path)
    resource_filename = pkg_resources.resource_filename(
        resource_package, resource_path)

    print("file binary contents: ", resource_as_binary_file.readline())

    with open(resource_filename) as file:
        print("file file contents: ", file.readline())


if __name__ == "__main__":
    main()
