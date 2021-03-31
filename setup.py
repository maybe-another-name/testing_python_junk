from setuptools import setup, find_packages

setup(
    name='testing-python-stuff',
    version='0.1.0',
    packages=find_packages(),
    package_data={'python_stuff': ['resources/*']},
    install_requires=['wheel'],
    entry_points = {
        'console_scripts': ['stuff=python_stuff.python_resource_loading_from_command:main']
    }
)
