# Maintainer: Andy Weidenbaum <archbaum@gmail.com>

pkgname=voltron-git
pkgver=20160417
pkgrel=1
pkgdesc="UI for GDB, LLDB and Vivisect's VDB"
arch=('any')
depends=('python'
         'python-blessed'
         'python-flask'
         'python-flask-restful'
         'python-pygments'
         'python-requests'
         'python-requests-unixsocket'
         'python-scruffington')
makedepends=('git' 'python-setuptools')
optdepends=('gdb: GDB'
            'lldb: LLDB'
            'vivisect: VDB')
url="https://github.com/snare/voltron"
license=('Beerware')
options=('!emptydirs')
source=(git+https://github.com/snare/voltron
        git+https://github.com/snare/voltron.wiki)
sha256sums=('SKIP' 'SKIP')
provides=('voltron')
conflicts=('voltron')

pkgver() {
  cd ${pkgname%-git}
  git log -1 --format="%cd" --date=short | sed "s|-||g"
}

build() {
  cd ${pkgname%-git}

  msg2 'Building...'
  python setup.py build
}

package() {
  cd ${pkgname%-git}

  msg2 'Installing documentation...'
  install -Dm 644 README.md -t "$pkgdir/usr/share/doc/${pkgname%-git}"
  cp -dpr --no-preserve=ownership "$srcdir/voltron.wiki" \
    "$pkgdir/usr/share/doc/${pkgname%-git}/wiki"

  msg2 'Installing...'
  python setup.py install --root="$pkgdir" --optimize=1

  msg2 'Cleaning up pkgdir...'
  find "$pkgdir" -type d -name .git -exec rm -r '{}' +
  find "$pkgdir" -type f -name .gitignore -exec rm -r '{}' +
}
