from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('wget')

  state = 'start'
  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgname='):
      line = 'pkgname=wget-lily'
    elif line.startswith('optdepends=('):
      line = line + '''
conflicts=('wget')
provides=("wget=$pkgver")'''

    elif line.startswith('prepare('):
      state = 'prepare'
    elif state == 'prepare' and line.startswith('}'):
      line = '  patch -p1 -i "${srcdir}/wget.patch"\n' + line
      state = ''

    elif line.startswith('source=('):
      if line.endswith(')'):
        line = line.replace(')', ' wget.patch)')
        state = ''
      else:
        state = 'source'
    elif state == 'source' and line.endswith(')'):
      line = line.replace(')', ' wget.patch)')
      state = ''

    elif line.startswith('sha256sums='):
      state = 'sha256sums'
    elif state == 'sha256sums' and line.endswith(')'):
      line = line.replace(')', ' aa28cf8532f6b7cc1fe689eb253b0453102990eb725a6583704ca4f3e665c9b0)')
      state = ''

    elif line.startswith('b2sums='):
      state = 'b2sums'
    elif state == 'b2sums' and line.endswith(')'):
      line = line.replace(')', ' c6a292c1be5606c007d1dcd25f02b3760ac98e86f2c1de30b50847b65c5ecfdb5cd89a482ab1e6a5b5978d38057c21d671b72ec45f10f6e59c5596519cecdf2e)')
      state = ''

    if '${pkgname}' in line:
      line = line.replace('${pkgname}', 'wget')

    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()

#if __name__ == '__main__':
#  single_main()
