#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  pkgver, commit = _G.newver.split('@')
  pkgver = pkgver.strip()
  commit = commit.strip()
  url = f"https://github.com/JuliaBinaryWrappers/LEMON_jll.jl/blob/{commit}/README.md"
  r = s.get(url)
  r.raise_for_status()
  readme = r.content
  m = re.search("https://github\\.com/JuliaPackaging/Yggdrasil/blob/([0-9a-f]*)/L", readme)
  src_commit = m[1]
  for line in edit_file('PKGBUILD'):
    if line.startswith('_src_commit='):
      line = f'_src_commit={src_commit}'
    print(line)
  update_pkgver_and_pkgrel(pkgver)
