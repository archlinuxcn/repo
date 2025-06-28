# Trimmed lilac.py
#!/usr/bin/env python3
from lilaclib import *
import datetime

#build_prefix = 'extra-x86_64'

def pre_build():
    if str(datetime.datetime.now())[:8] < '20180604':
        run_cmd('rm -rf dnsmasq-china-list'.split(' '))

    aur_pre_build(maintainers=['felixonmars', 'lilac'])

#post_build = aur_post_build

#if __name__ == '__main__':
#  single_main(build_prefix)
