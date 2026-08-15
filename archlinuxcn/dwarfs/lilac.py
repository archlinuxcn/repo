#!/usr/bin/env python3
from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['KokaKiwi'])
    for line in edit_file('PKGBUILD'):
        line: str
        if '--exclude-regex' in line and line.endswith("'"):
            print(line[:-1] + "|mkdwarfs_log_mem_usage_test\\.log_memory_usage'")
        else:
            print(line)
