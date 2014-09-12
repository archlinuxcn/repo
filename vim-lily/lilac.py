#!/usr/bin/env python3

import os

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  if not os.path.isdir('vim'):
    os.mkdir('vim')
    with at_dir('vim'):
      run_cmd(["git", "clone", "-b", "all", "git@github.com:lilydjwg/vim.git"])
      run_cmd(["git", "remote", "add", "upstream", "git@github.com:vim-jp/vim.git"])
  with at_dir('vim'):
    run_cmd(["git", "reset", "--hard"])
    run_cmd(["git", "fetch", "uptream"])
    run_cmd(["git", "merge", "uptream/master"])

def post_build():
  with at_dir('vim'):
    run_cmd(["git", "push", "origin", "all"])

if __name__ == '__main__':
  single_main()
