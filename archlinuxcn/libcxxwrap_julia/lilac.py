#!/usr/bin/env python3

from lilaclib import *

def _get_libcxxwrap_commit(commit):
  readme = s.get(f"https://raw.githubusercontent.com/JuliaBinaryWrappers/libcxxwrap_julia_jll.jl/{commit}/README.md").text
  m = re.search("https://github.com/JuliaPackaging/Yggdrasil/blob/([a-z0-9A-Z]*)/L/libcxxwrap_julia/build_tarballs\\.jl", readme)
  build_tarballs = s.get(f"https://raw.githubusercontent.com/JuliaPackaging/Yggdrasil/{m[1]}/L/libcxxwrap_julia/build_tarballs.jl").text
  m = re.search('git_repo, "([a-z0-9A-Z]*)"', build_tarballs)
  return m[1]

def pre_build():
  pkgver, commit = _G.newver.split('@')
  pkgver = pkgver.split('+')[0]
  commit = _get_libcxxwrap_commit(commit)
  for line in edit_file('PKGBUILD'):
    if line.startswith('_commit='):
      line = f'_commit={commit}'
    print(line)
  update_pkgver_and_pkgrel(pkgver.strip())
