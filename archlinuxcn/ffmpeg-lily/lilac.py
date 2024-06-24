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

    elif line.startswith('depends=('):
      state = 'depends'
    elif state == 'depends' and line == ')':
      line = '''  ffmpeg=$epoch:$pkgver\n''' + line + '\nconflicts=(ffmpeg)'
      state = 'out'

    elif line.startswith('prepare('):
      state = 'prepare'
    elif state == 'prepare' and line.startswith('}'):
      line = '  patch -Np1 -i ../FFmpeg-devel-v4-avcodec-vaapi_encode-add-customized-surface-alignment.diff\n' + line
      state = 'out'

    elif line.startswith('source=('):
      state = 'source'
    elif state == 'source' and line == ')':
      line = '  FFmpeg-devel-v4-avcodec-vaapi_encode-add-customized-surface-alignment.diff\n' + line
      state = 'out'

    elif line.startswith('b2sums='):
      state = 'b2sums'
    elif state == 'b2sums' and line.endswith(')'):
      line = line.replace(')', '\n        136c870cc4f9a235c8bca377a698df84c9856205020c76e90242bc75a660c23af67e6bd6c0b4b70d0b41bbdebf827735831181ef25ad84ecfb6750d2517a7fd2)')
      state = 'out'

    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
