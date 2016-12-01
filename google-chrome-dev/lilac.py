#!/usr/bin/env python3

from lilaclib import *
import os

build_prefix = 'extra-x86_64'
post_build = aur_post_build

_pkg_name = 'google-chrome-dev'

dotinstall = '''
note() {
    printf "${blue}==>${yellow} NOTE:${bold} $1${all_off}\n"
}

all_off="$(tput sgr0)"
bold="${all_off}$(tput bold)"
blue="${bold}$(tput setaf 4)"
yellow="${bold}$(tput setaf 3)"

post_install() {
    note "Custom flags should be put directly in: ~/.config/chrome-flags.conf"
    note "The launcher is called: 'google-chrome-unstable'"
}

post_upgrade() {
    post_install
}
'''

def pre_build():
  aur_pre_build()
  install_file = '%s.install' % _pkg_name
  try:
    os.unlink(install_file)
  except FileNotFoundError:
    return
  with open(install_file, 'wb') as f:
    f.write(dotinstall.encode())

if __name__ == '__main__':
  single_main(build_prefix)

# vim: set ts=2 sw=2 et:
