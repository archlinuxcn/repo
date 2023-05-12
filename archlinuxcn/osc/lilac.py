#!/usr/bin/python3

def pre_build():
    add_depends(['python-cryptography', 'python-urllib3'])
    aur_pre_build(maintainers=['Thaodan'])
