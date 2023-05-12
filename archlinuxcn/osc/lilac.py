#!/usr/bin/python3

def pre_build():
    aur_pre_build(maintainers=['Thaodan'])
    add_depends(['python-cryptography', 'python-urllib3'])
