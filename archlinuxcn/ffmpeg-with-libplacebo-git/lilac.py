from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('ffmpeg')
  add_provides(['ffmpeg'])
  add_conflicts(['ffmpeg'])
  add_depends(['libplacebo-git'])
  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgname='):
      line = 'pkgname=ffmpeg-with-libplacebo-git'
    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
