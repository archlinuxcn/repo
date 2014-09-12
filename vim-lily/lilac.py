#!/usr/bin/env python3

import os
import subprocess
import atexit

from lilaclib import *

build_prefix = 'extra-x86_64'
p = None

def bye_git_daemon():
  global p
  if p:
    p.terminate()
  p = None

atexit.register(bye_git_daemon)

def pre_build():
  global p
  if not os.path.isdir('vim'):
    os.mkdir('vim')
    run_cmd(["git", "clone", "-b", "all", "git@github.com:lilydjwg/vim.git"], use_pty=True)
    with at_dir('vim'):
      run_cmd(["git", "remote", "add", "upstream", "git@github.com:vim-jp/vim.git"])
  with at_dir('vim'):
    run_cmd(["git", "reset", "--hard"])
    run_cmd(["git", "fetch", "upstream"], use_pty=True)
    run_cmd(["git", "merge", "--no-edit", "upstream/master"])
  cmd = ["git", "daemon", "--export-all", "--reuseaddr", "--base-path=.", "--listen=127.0.0.1", "--", "./vim"]
  p = subprocess.Popen(cmd)
  if p.poll():
    raise subprocess.CalledProcessError(p.returncode, cmd, '(not captured)')

def post_build_always(*, success=None, **kwargs):
  bye_git_daemon()
  if success:
    with at_dir('vim'):
      run_cmd(["git", "push", "origin", "all"], use_pty=True)

if __name__ == '__main__':
  single_main()
