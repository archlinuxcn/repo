#!/usr/bin/python3

from lilaclib import *

def pre_build():
    run_cmd(['git', 'clean', '-xdf', '.'])
    aur_pre_build(maintainers=['ptr1337','sir_lucjan'])

    for line in edit_file('auto-cpu-optimization.sh'):
        if line.startswith('MARCH=$'):
            line = 'MARCH=CONFIG_GENERIC_CPU3'
        print(line)

    run_cmd(['updpkgsums'])
