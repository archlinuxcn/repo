#!/usr/bin/env python3

import os
import subprocess
import atexit
import time

from lilaclib import (
  run_cmd, at_dir, git_pull, vcs_update,
  update_pkgrel, git_add_files, git_commit,
  single_main,
)

p = None
repo_dir = 'vim'

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
    run_cmd(["git", "clone", "-b", "all", "git@github.com:lilydjwg/vim.git", repo_dir], use_pty=True)
    with at_dir(repo_dir):
      run_cmd(["git", "remote", "add", "-f", "upstream", "git@github.com:vim/vim.git"])

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

  try:
    time.sleep(1) # wait a while for git daemon
    vcs_update()
  except RuntimeError:
    # only runtime updated; source remains the same
    update_pkgrel()

def post_build_always(*, success=None, **kwargs):
  bye_git_daemon()
  if success:
    with at_dir(repo_dir):
      run_cmd(["git", "push", "origin", "all"], use_pty=True)
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
  single_main()
