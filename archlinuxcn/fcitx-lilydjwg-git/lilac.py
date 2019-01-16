# Trimmed lilac.py
#!/usr/bin/env python3

import os
import subprocess
import atexit
import time

from lilaclib import *

#build_prefix = 'extra-x86_64'
p = None
repo_dir = 'fcitx-repo'

def bye_git_daemon():
  global p
  if p:
    p.terminate()
  p = None

atexit.register(bye_git_daemon)

def pre_build():
  global p

  if not os.path.isdir(repo_dir):
    os.mkdir(repo_dir)
    run_cmd(["git", "clone", "-b", "lilydjwg", "git@github.com:lilydjwg/fcitx.git", repo_dir], use_pty=True)
    with at_dir(repo_dir):
      run_cmd(["git", "remote", "add", "upstream", "https://gitlab.com/fcitx/fcitx.git"])

  with at_dir(repo_dir):
    run_cmd(["git", "reset", "--hard"])
    git_pull()
    run_cmd(["git", "fetch", "upstream"], use_pty=True)
    run_cmd(["git", "merge", "--no-edit", "upstream/master"])

  cmd = ["git", "daemon", "--export-all", "--reuseaddr", "--base-path=.", "--listen=127.0.0.1", "--",
         "./" + repo_dir]
  p = subprocess.Popen(cmd)
  if p.poll():
    raise subprocess.CalledProcessError(p.returncode, cmd, '(not captured)')

  time.sleep(1) # wait a while for git daemon
  vcs_update()

def post_build_always(*, success=None, **kwargs):
  bye_git_daemon()
  if success:
    with at_dir(repo_dir):
      run_cmd(["git", "push", "origin", "lilydjwg"], use_pty=True)
    git_add_files('PKGBUILD')
    git_commit()

#if __name__ == '__main__':
#  single_main()
