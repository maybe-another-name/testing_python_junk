import sys
import tarfile
import pkg_resources

import select


def main():
    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        filter_from_std_in()
    else:
        filter_from_contant()


def filter_from_std_in():
    try:
        input_string = sys.stdin.read()
        if test_string(input_string):
            sys.stdout.write(input_string)
    except:
        # error case
        e = sys.exc_info()[0]
        print(e)
        return -1
    finally:
        pass


def filter_from_contant():
    resource_package = __name__
    resource_path = '/'.join(('resources', 'file-with-matching-content.txt'))
    resource_filename = pkg_resources.resource_filename(
        resource_package, resource_path)

    file_matches = False

    input_string = open(resource_filename).read()

    if test_string(input_string):
        sys.stdout.write(input_string)


def test_string(input_string):
    return input_string.__contains__('hungry')


if __name__ == "__main__":
    main()
