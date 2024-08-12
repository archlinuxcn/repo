from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('obs-studio')

  state = 'out'
  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgname='):
      line = 'pkgname=obs-studio-lily'
    elif line.startswith('pkgdesc='):
      line = line[:-1] + ' (with websocket support)' + line[-1]
    elif '-DENABLE_WEBSOCKET=OFF' in line:
      line = line.replace('OFF', 'ON')
    elif '-DENABLE_BROWSER=OFF' in line:
      line = line.replace('OFF', 'ON')
    elif line.startswith('makedepends='):
      line = line.replace(')', " 'websocketpp' 'asio' 'qrcodegencpp-cmake')")
      line = line + '\nprovides=(obs-studio=$pkgver)\nconflicts=(obs-studio)'

    elif line.startswith('optdepends=('):
      state = 'optdepends'
    elif state == 'optdepends' and line.endswith(')'):
      line = line.replace(')', "\n            'qrcodegencpp-cmake: websocket support')")
      state = 'out'

    line = line.replace('$pkgname', 'obs-studio')

    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
