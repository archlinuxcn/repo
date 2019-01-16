# Trimmed lilac.py
#!/usr/bin/env python3

from lilaclib import *

#build_prefix = 'archlinuxcn-x86_64'


def pre_build():
    pypi_pre_build(
        depends=['python', 'python-terminaltables', 'python-tabulate'])

    for line in edit_file('PKGBUILD'):
        if line.startswith('_pkgname='):
            print('_pkgname=%s' % "cli_helpers")
        else:
            print(line)


def post_build():
    pypi_post_build()


#if __name__ == '__main__':
#    single_main()
