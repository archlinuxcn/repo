from lilaclib import *


def pre_build():
    aur_pre_build(maintainers=['loathingkernel'])
    add_makedepends(['python-virtualenv'])
    add_makedepends(['python-pip'])
    for line in edit_file('PKGBUILD'):
        if 'afdko' in line:
            line = line.replace('afdko','')
            print(line)
        elif 'prepare()' in line:
            print(line)
            print("[ -d build_venv ] && rm -rf build_venv\n")
            print('virtualenv --app-data "$srcdir"/build_venv/cache --no-wheel build_venv\n')
            print('source build_venv/bin/activate\n')
            print('pip install --no-cache-dir afdko\n')
        else:
            print(line)

