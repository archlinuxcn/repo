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
      line = line.replace(')', '\n        b520886c53d3a1ad2e3eb482058dd38e04df298b89f199c3cc23d498bd9d27d28fa4fffba6262319ec3e2dd7c940a3bc8de701871fc5f200cd4793ffedb76210)')
      state = 'out'

    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
