# Getting Started


setup the virtual env

    python3.8 -m venv venv
    source venv/bin/activate

install it

    pip install .

(will have to run it twice for wheel)    

changes often require full uninstall/reinstall

    pip uninstall testing-python-stuff -y
    pip install .


# Running It

The pip install should make it runnable with a command (from inside the virtual env), like so:

    (venv) user@pc:~/git/testing_python_junk$ stuff 
    file binary contents:  b'only the tastiest bits'
    file file contents:  only the tastiest bits