#!/usr/bin/env python3

from lilaclib import *
import subprocess

def pre_build():
  update_pkgver_and_pkgrel(_G.newver.lstrip('v'))
  cmd = "curl https://download.slicer.org/ | grep bitstream | cut -d '\"' -f 2"
  newstr = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
  newstr = newstr.split('\n')[2].replace('/bitstream/', '').replace('/bitstream/', '')

  cmd = "grep bitstream PKGBUILD|cut -f 5 -d \'/\'"
  oldstr = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')[0:-2]

  if oldstr == newstr:
    raise RuntimeError("URL is not updated yet.")
  cmd = f"sed -i \'/bitstream/s/{oldstr}/{newstr}/\' PKGBUILD"
  subprocess.run(cmd, shell=True)

def post_build():
  git_add_files('PKGBUILD')
  git_commit()
# vim:set ts=2 sw=2 et:

