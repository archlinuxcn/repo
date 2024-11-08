from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('ffmpeg')

  state = 'out'
  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgname='):
      line = 'pkgname=ffmpeg-lily'
    elif line.startswith('pkgdesc='):
      line = line[:-1] + " (with AMD HEVC VAAPI alignment patch)'"

    elif line.startswith('provides=('):
      state = 'provides'
    elif state == 'provides' and line == ')':
      line = '''  ffmpeg=$epoch:$pkgver\n''' + line + '\nconflicts=(ffmpeg)'
      state = 'out'

    elif line.startswith('prepare('):
      state = 'prepare'
    elif state == 'prepare' and line.startswith('}'):
      line = '  patch -Np1 -i ../0001-AMD-VAAPI-H265-encode-dimemsion-fix.patch\n' + line
      state = 'out'

    elif line.startswith('source=('):
      state = 'source'
    elif state == 'source' and line == ')':
      line = '  0001-AMD-VAAPI-H265-encode-dimemsion-fix.patch\n' + line
      state = 'out'

    elif line.startswith('b2sums='):
      state = 'b2sums'
    elif state == 'b2sums' and line.endswith(')'):
      line = line.replace(')', '\n        ef0ab4810b612683123ee082483e94afda07b8179b8ad846b9af442f48ea31cd8ecea3519fea7271a765089d544e5708ddf6ffc67c80504313dfbd033bb85230)')
      state = 'out'

    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
