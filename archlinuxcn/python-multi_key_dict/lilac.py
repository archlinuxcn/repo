from lilaclib import *

def pre_build():
    aur_pre_build('python-multi_key_dict', maintainers=['synthead'])
    for line in edit_file('PKGBUILD'):
        if line.startswith('arch='):
            line = 'arch=("any")'
        print(line)
